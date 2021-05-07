import plot_lib as eval_plot
import json
import os
from pathlib import Path

filepathes = [Path("evaluation_files/MRCNN/recursive/eval.json"),
              Path("evaluation_files/MRCNN/re-init/eval.json"),
              Path("evaluation_files/MRCNN/w_o_segmentation/eval.json"),
              Path("evaluation_files/FRCNN/eval.json")]

titles_fscore_03 = ["(5) MRCNN recursive f-scr.: 0.844",
                    "(4) MRCNN re-init f-scr.: 0.848",
                    "(2) MRCNN w/o seg. f-scr.: 0.875",
                    "(1) FRCNN f-scr.: 0.854"]
titles_fscore_05 = ["(5) MRCNN recursive f-scr.: 0.758",
                    "(4) MRCNN re-init f-scr.: 0.772",
                    "(2) MRCNN w/o seg. f-scr.: 0.797",
                    "(1) FRCNN f-scr.: 0.773"]

colors = [(0, .8, 0), (.72, .39, .92), (0, 0, .8), (.9, 0, 0)]

for i, p in enumerate(filepathes):
    with open(p, 'r') as j:
        data = json.load(j)

    prec, rec = eval_plot.sort_prec_rec(data['evaluation']['prec']['0.3'], data['evaluation']['rec']['0.3'])
    print("0.3: ", max([2*p*r/(p+r) for p, r in zip(prec, rec)]))
    eval_plot.plot_prec_rec(rec, prec, titles_fscore_03[i], linestyle='--', color=colors[i])

# plot empty curve for space between 0.3 f-score and 0.5 f-score curves
eval_plot.plot_prec_rec([], [], label=" ")

for i, p in enumerate(filepathes):
    with open(p, 'r') as j:
        data = json.load(j)

    prec, rec = eval_plot.sort_prec_rec(data['evaluation']['prec']['0.5'], data['evaluation']['rec']['0.5'])
    print("0.5: ", max([2*p*r/(p+r) for p, r in zip(prec, rec)]))
    eval_plot.plot_prec_rec(rec, prec, titles_fscore_05[i], color=colors[i])

eval_plot.draw_fscore_lines()
eval_plot.config()

# eval_plot.savefig(filepath + data['name'] + '.svg')
eval_plot.show()


