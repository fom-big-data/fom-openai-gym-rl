import matplotlib
import matplotlib.pyplot as plt
import torch

is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display


class PerformancePlotter:

    def plot_values(values, title, xlabel, ylabel):
        """
        Plots values of a epoch (e.g. duration, loss, reward)
        :param values: values of each episode
        :return:
        """

        plt.figure(2)
        plt.clf()
        durations_t = torch.tensor(values, dtype=torch.float)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.plot(durations_t.numpy())
        # Take 100 episode averages and plot them too
        if len(durations_t) >= 100:
            means = durations_t.unfold(0, 100, 1).mean(1).view(-1)
            means = torch.cat((torch.zeros(99), means))
            plt.plot(means.numpy())

        plt.pause(0.001)  # pause a bit so that plots are updated
        if is_ipython:
            display.clear_output(wait=True)
            display.display(plt.gcf())