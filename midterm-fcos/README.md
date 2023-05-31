# DATA620004 Homework 2 Task 2 Part 2 Object Detection using FCOS

## Download the data

- The same as the above Faster-RCNN project.


## Download the models 

- In order to save time, please first download this model ([Baidu Cloud](https://pan.baidu.com/s/1raWewk8ByTETxKmHfISdFw?pwd=wyii), code: wyii) and put it in the `model data` directory.

- The trained model ([Baidu Cloud](https://pan.baidu.com/s/1muROgP7y2UCDpFnjvfUiKA?pwd=qwwt), code: qwwt). Please put it in the `logs` directory. If you only need to predict, please download the `last_epoch_weights.pth`. If you want to reproduce the calculation procedure of mAP, you should download al the `.pth` files starting with `ep`.


## Executing pipeline

- Training:  `python train.py`
  - The loss results available for `tensorboard` will be saved inside a folder starting with "loss" the `logs` sub-directory
  - The model is saved in the `logs` folder, and we set the parameters to be saved every 5 epochs for subsequent calculation of mAP.

- Prediction: `python predict.py` (You will be prompted to input the location of the picture to be predicted)

- Calculating mAP: `python draw_map_tensorboard.py`
  - **Note**: You must change the `logdir` variable in the program for your own log directory!!!
