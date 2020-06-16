import os

import torch


class ModelStorage:

    def saveModel(directory, total_frames, total_episodes, net, optimizer, memory, loss, environment_name,
                  environment_wrappers,
                  batch_size, gamma, num_atoms, vmin, vmax, target_update, replay_memory_size, num_frames,
                  reward_shapings
                  ):
        """
        Saves output into a file
        """

        # Make path if not yet exists
        if not os.path.exists(directory):
            os.mkdir(directory)

        torch.save({
            'total_frames': total_frames,
            'total_episodes': total_episodes,
            'model_state_dict': net.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'replay_memory': memory,
            'loss': loss,
            'environment_name': environment_name,
            'environment_wrappers': environment_wrappers,
            'batch_size': batch_size,
            'gamma': gamma,
            'num_atoms': num_atoms,
            'vmin': vmin,
            'vmax': vmax,
            'target_update': target_update,
            'replay_memory_size': replay_memory_size,
            'num_frames': num_frames,
            'reward_shapings': reward_shapings
        }, directory + "/target_net-frame-{:07d}".format(total_frames) + ".output")

    def loadModel(path):
        """
        Loads output from a given path
        :param path path to saved output
        :return:
        """
        checkpoint = torch.load(path)

        return checkpoint['total_frames'], \
               checkpoint['total_episodes'], \
               checkpoint['model_state_dict'], \
               checkpoint['optimizer_state_dict'], \
               checkpoint['replay_memory'], \
               checkpoint['loss'], \
               checkpoint['environment_name'], \
               checkpoint['environment_wrappers'], \
               checkpoint['batch_size'], \
               checkpoint['gamma'], \
               checkpoint['num_atoms'], \
               checkpoint['vmin'], \
               checkpoint['vmax'], \
               checkpoint['target_update'], \
               checkpoint['replay_memory_size'], \
               checkpoint['num_frames'], \
               checkpoint['reward_shapings']