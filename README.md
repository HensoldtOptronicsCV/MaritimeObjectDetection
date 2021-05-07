# A Benchmark for Deep Learning Based Object Detection in Maritime Environments

This is the code used to set the Benchmark within the paper "A Benchmark for Deep Learning BasedObject Detection in Maritime Environments" by Moosbauer et al., IEEE CVPR Workshops 2019.
Here is the direct link to the paper: [click me](https://openaccess.thecvf.com/content_CVPRW_2019/papers/PBVS/Moosbauer_A_Benchmark_for_Deep_Learning_Based_Object_Detection_in_Maritime_CVPRW_2019_paper.pdf)

As the used [Detectron-Framework](https://github.com/facebookresearch/Detectron) is deprecated and the results might hard to reproduce, main contribution of this repository are the provided annotations, including the semantic segmentation used for weakly-supervised recursive training.

## Overview of the repository
### detectron/datasets/smd_dataset_evaluator.py
Add-on to the Detectron-Framework that enables evaluation using our evaluation strategy

### EvaluationCode
Necessary code to reproduce our evaluation strategy used within Detectron-Framework.

### WeaklySupervisedRecursiveTraining
Python script that acts as a wrapper to re-initialize trainings following our used weakly-supervised recursive training

## Cite us

If you use any of the findings of our paper, then please cite us:

```
@InProceedings{Moosbauer_2019_CVPR_Workshops,
author = {Moosbauer, Sebastian and Konig, Daniel and Jaekel, Jens and Teutsch, Michael},
title = {A Benchmark for Deep Learning Based Object Detection in Maritime Environments},
booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
month = {June},
year = {2019}
} 
```
