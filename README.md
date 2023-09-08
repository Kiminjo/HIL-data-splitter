# HIL-data-splitter

This repository is responsible for organizing data in the form of Human in the loop (HIL). 

As of September 8, 2023, this repository has been code-implemented to suit the Mobile Phone Defect Segmentation Dataset provided by Kaggle.

If there is a case where HIL needs to be done using other data in the future, I plan to modify the code more generally.

<br>

## How to Use
1. Download data on kaggle and put it on data directory     
download mobile phone defect data from below URL.
https://www.kaggle.com/datasets/girish17019/mobile-phone-defect-segmentation-dataset           

2. Run main.py 
    ```
    python main.py \
        --data data/mobile_data \
        --classes oil scratch stain \
        --save_path results/
    ```
    change parsers on your case.