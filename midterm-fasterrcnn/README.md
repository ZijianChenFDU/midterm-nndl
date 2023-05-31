# DATA 620004 Homework 2 Task 2 Part 1 Object Detection using Faster-RCNN

## Download the data

- [Data address](https://pan.baidu.com/s/1U58gZamTpjgRJypFfC5vLg?pwd=xb4y)(code: xb4y)

  - Please unzip the 7z file in the VOCdevkit folder.

  - execute `python voc_annotations.py` in the command line to get the ground truth coordinates of the anchors, which will be saved in the `2007_train.txt` and `2007_val.txt` in the main directory.
  
  - Although the prefix is "2007", our original data has incorporated the data of VOC 2012.
  
  - Since part of our code is rewritten from someone else's code, there may be some variable names and file names with the suffix "_val" that represent the "validation set" that we have not modified. In fact, there is no verification set, and the data of the verification set has been copied into the data of the training set in our data.


## Download the models

- In order to save time, please first download this model ([Baidu Cloud](https://pan.baidu.com/s/1BeIFQ9loEj98k1q-uTi2zw?pwd=fkcz), code: fkcz) and put it in the `model data` directory.

- The trained model ([Baidu Cloud](https://pan.baidu.com/s/1pFtsPfBsqQa-NokJBxEkAw?pwd=r73e), code: r73e). Please put it in the `logs` directory. If you only need to predict, please download the `last_epoch_weights.pth`. If you want to reproduce the calculation procedure of mAP, you should download al the `.pth` files starting with `ep`.


## Executing pipeline

- Training:  `python train.py`
  - The loss results available for `tensorboard` will be saved inside a folder starting with "loss" the `logs` sub-directory.
  - The model is saved in the `logs` folder, and we set the parameters to be saved every 5 epochs for subsequent calculation of mAP.

- Prediction: `python predict.py` (You will be prompted to input the location of the picture to be predicted).

  - To get the first-stage proposal, you can run `predict.py` after uncommenting lines 166-172 in `frcnn.py` in the **main directory**.

- Calculate mAP: `python epoch_map_writer.py`. The result will be saved in the `map` sub-folder of `logs`.
