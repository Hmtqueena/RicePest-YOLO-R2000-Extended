# GCP-YOLO-R2000-Extended

This repository provides supporting dataset resources, annotation records, dataset split information and source records for the GCP-YOLO study.

## Overview

R2000-Extended was constructed for rice pest detection under complex field-oriented image conditions. It extends the original R2000 rice pest dataset with an independent supplementary public-source test set.

The original R2000 dataset is available from the original repository:

https://github.com/awsomespark/R2000

To respect the original data terms, the original R2000 images and labels are not redistributed in this repository. Users should obtain the original R2000 dataset from the repository above and follow its original data terms.

## Dataset Split

In this study, the original R2000 images were split into training and validation sets at a ratio of 3:1 using a fixed random seed of 42. The supplementary public-source images were used as an independent test set.

| Split | Source | Number of images |
|---|---|---:|
| Training | Original R2000 dataset | 1518 |
| Validation | Original R2000 dataset | 506 |
| Test | Supplementary public-source images | 504 |

R2000-Extended contains 2528 images in total, corresponding approximately to a 6:2:2 training/validation/test ratio.

Progressive data expansion was applied only to the training set. The validation and independent test sets were not augmented.

## Supplementary Test Images

The supplementary test set contains 504 public-source images. Among them, 461 images were obtained from GBIF occurrence downloads, and 43 images were selected from the unannotated portion of the public IP102 dataset to improve category coverage after manual screening.

All supplementary test images were manually reviewed and annotated in this study using Labelme. The annotations were converted into YOLO-compatible bounding-box format.

The supplementary test images and related resources are available from the GitHub Release:

**R2000-Extended-datasets**

## Relationship to IP102 Evaluation

The 43 IP102-derived images included in R2000-Extended were selected from the unannotated portion of IP102 and used only as part of the independent supplementary test set.

The IP102 cross-dataset evaluation reported in the paper used an annotated IP102 subset that was separate from these 43 images.

## Repository Contents

| File | Description |
|---|---|
| `README.md` | Description of R2000-Extended and repository usage |
| `supplementary_test_sources_by_class.csv` | Category-level source summary for supplementary test images, including GBIF source records and licence information |
| `scripts_prepare_r2000_train_val_split.py` | Script for reproducing the training/validation split of the original R2000 dataset |
| `.gitignore` | Git ignore file |

## Data Availability

The data that support the findings of this study are openly available in this repository. The original R2000 dataset is available from https://github.com/awsomespark/R2000 and is not redistributed here. Images from GBIF and IP102 remain subject to their original licences and citation requirements.

## Citation and Licence

Please cite the original R2000 dataset, GBIF occurrence records and IP102 dataset where appropriate. GBIF citation information, download records and licence details are provided in `supplementary_test_sources_by_class.csv`.

This repository provides supporting research resources for the GCP-YOLO study. Users should follow the original licences and terms of all source datasets.
