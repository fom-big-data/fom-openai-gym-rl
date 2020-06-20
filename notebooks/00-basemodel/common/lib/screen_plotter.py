import os
from email.utils import formatdate

import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision.transforms as T


class ScreenPlotter:

    def display_screen_plot(total_frames, env, title, device):
        """
         Plots current state of the screen
        :param total_frames: number of frames since the beginning
        :param env: environment to extract screen from
        :param title: title
        :param device: device
        :return:
        """

        plt = ScreenPlotter.generate_plot(env, title, device)

        plt.show()

    def save_screen_plot(directory, total_frames, env, title, device):
        """
        Saves current state of the screen as png file
        :param directory to save plot in
        :param total_frames: number of frames since the beginning
        :param env: environment to extract screen from
        :param title: title
        :param device: device
        :return:
        """

        # Make path if not yet exists
        if not os.path.exists(directory):
            os.mkdir(directory)

        plt = ScreenPlotter.generate_plot(env, title, device)

        plt.savefig(fname=directory + "/" + str(title) + "-frame-{:07d}".format(total_frames) + ".png",
                    format="png",
                    metadata={
                        "Title": str(title) + "-frame-{:07d}".format(total_frames),
                        "Author": "Daniel Pleuss, Clemens Voehringer, Patrick Schmidt, Florian Schwanz",
                        "Creation Time": formatdate(timeval=None, localtime=False, usegmt=True),
                        "Description": "Plot of " + str(title)
                    })

    def generate_plot(env, title, device):
        """
        Generates plot of a screen
        :param env: environment to extract screen from
        :param title: title
        :param device: device
        :return: plot
        """

        resize = T.Compose([T.ToPILImage(),
                            # T.Resize(40, interpolation=Image.CUBIC),
                            T.ToTensor()])

        screen = env.render(mode='rgb_array').transpose((2, 0, 1))

        # Convert to float, rescale, convert to torch tensor
        # (this doesn't require a copy)
        screen = np.ascontiguousarray(screen, dtype=np.float32) / 255
        screen = torch.from_numpy(screen)
        # Resize, and add a batch dimension (BCHW)
        screen = resize(screen).unsqueeze(0).to(device)

        plt.figure()
        plt.imshow(screen.cpu().squeeze(0).permute(1, 2, 0).numpy(),
                   interpolation='none')
        plt.title(title)
        return plt