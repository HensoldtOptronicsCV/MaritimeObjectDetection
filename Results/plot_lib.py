import matplotlib.pyplot as plt
import numpy as np


# Mandatory!
def sort_prec_rec(prec, rec):

    prec = [val for val in prec if val > 0]
    rec = [val for val in rec if val > 0]

    rank = np.argsort(rec)
    rec = np.sort(rec)
    prec = [prec[i] for i in rank]

    # if difference of initial and first point is larger than plotting ranges smallest value
    # we drop it for visualization
    # if rec[1] - rec[0] > .4:
    #     prec = prec[1:]
    #     rec = rec[1:]

    return prec, rec


def plot_prec_rec(rec, prec, label, linestyle='-', color=(1, 1, 1)):
    line, = plt.plot(rec[1:], prec[1:], linestyle=linestyle, color=color, label=label)
    plt.axis([0.4, 1, 0.4, 1])
    plt.grid(True, which='both')
    plt.xlabel('recall', fontdict=None, labelpad=None)
    plt.ylabel('precision', fontdict=None, labelpad=None)

    return line


def draw_fscore_lines():
    # f-scores to be drawn (0.4 to 1.0 with stepwidth 0.05)
    f_scores = [i/100. for i in range(45, 100, 5)]
    recall_values = [i/1000. for i in range(400, 1010, 10)]

    # f-score = 2 * (precision * recall) / (precision + recall)
    # => precision = f-score * recall / (2 * r - f)
    for f in f_scores:
        precision_by_fscore = []
        valid_recall_idx = 0
        for r in recall_values:
            # avoid drawing f-score curves for recall values on the poles left side
            if 2*r <= f:
                valid_recall_idx += 1
                continue

            precision_by_fscore.append(f*r/(2*r-f))

        plt.plot(recall_values[valid_recall_idx:], precision_by_fscore, linestyle='--', color=(.5, .5, .5))
        if precision_by_fscore[-1] > 0.4:
            plt.text(recall_values[-1] + .01, precision_by_fscore[-1], str(f), fontsize=12)

    return


# def config(suptitle, ticks=[round(float(i) / 20, 2) for i in range(21)], title=None):
def config(suptitle=None, ticks=None, title=None):
    fig = plt.gcf()
    fig.set_size_inches(14, 14)
    legend = plt.legend(loc='lower left', frameon=True)
    frame = legend.get_frame()
    frame.set_alpha(None)
    frame.set_facecolor((1, 1, 1, 1))
    frame.set_edgecolor((0, 0, 0, 1))

    # avoid errors due to mutable default arguments
    if ticks is None:
        ticks = [.4, .5, .6, .7, .8, .9, 1.]
    plt.xticks(ticks)
    plt.yticks(ticks)
    if suptitle is not None:
        plt.suptitle(suptitle, fontsize=14)
    if title is not None:
        plt.title(title)
    plt.gca().set_aspect('equal', adjustable='box')

    return


def show():
    plt.show()
    return


def savefig(title):
    plt.savefig(title, transparent=True, dpi=600)
    return


def clearfig():
    plt.clf()
    return
