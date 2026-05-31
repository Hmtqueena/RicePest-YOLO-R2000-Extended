# RicePest-YOLO-R2000-Extended

This repository provides supporting dataset resources for the RicePest-YOLO study.

## Overview

R2000-Extended was constructed for fine-grained rice pest detection under field-oriented image conditions. It is based on the original R2000 rice pest dataset and a supplementary public-source test set.

The original R2000 dataset is available from the original repository:

https://github.com/awsomespark/R2000

The original R2000 images and labels are not redistributed in this repository. Users should obtain the original R2000 dataset from the repository above and follow the original data terms.

## Dataset split

In this study, the original R2000 images were split into training and validation sets at a ratio of 3:1. The supplementary public-source images were used as an independent test set.

The final split was:

| Split | Source | Number of images |
|---|---|---:|
| Training | Original R2000 dataset | 1518 |
| Validation | Original R2000 dataset | 506 |
| Test | Supplementary public-source images | 504 |

This corresponds approximately to a 6:2:2 training/validation/test ratio.

Progressive data expansion was applied only to the training set. The validation and test sets were not augmented.

## Supplementary test images

The supplementary test set contains 504 public-source images. Among them, 461 images were obtained from GBIF occurrence downloads, and 43 images were selected from the public IP102 dataset to maintain category coverage for pest classes with insufficient GBIF images after manual screening.

The supplementary test images are available from the GitHub Release:

**R2000-Extended-datasets**

Release asset:

```text
R2000-Extended.zip
