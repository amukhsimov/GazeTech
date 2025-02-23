# ETH-XGaze-tech
This repository is an extended version of the [ETH-XGaze official implementation](https://github.com/xucong-zhang/ETH-XGaze) to train gaze estimation models on ETH-XGaze. This framework serves to create baselines and [benchmark new full face or multi-region gaze estimation models](#benchmark-your-own-model). It allows loading single face image or multi-region (face and eye) images for different models flexibly.

<br/>

# Set-up

## 1. Dataset
Please refer to our [data normalization repository](https://github.com/X-Shi/Data-Normalization-Gaze-Estimation) for downloading and pre-processing the multi-region ETH-XGaze dataset. After that, specify the path to the dataset at *--data_dir* in **config.py**. This directory should contain **/train** and **/test** where the h5 files are placed. 

## 2. Environment
This code base is tested on the Linux system. We recommend the paradigm of creating a Conda environment first:
`conda create --name gaze_env` and then install the dependencies in the Conda environment: `pip install -r requirements.txt`. You could also install the dependencies directly via the previous pip command. 

<br/>

# Train

## 1. Weights and Biases
We recommend the use of [Weights and Biases](https://wandb.ai/) (wandb) to view the learning curves and more. To use it, please first log in and remove `mode="disabled"` at L22 in **main.py**. You can then access the learning curves and other training results on the web while your model is being trained.

## 2. Start training example
`python main.py --model_name multi_region_res50 --epochs 30`

You can find more hyperparameters and their descriptions in **config.py**. 

<br/>

# Evaluation

## 1. Predict
To evaluate a model's performance, first, specify the model path at *--pre_trained_model_path*, please make sure the other training and model hyperparameters are consistent with the hyperparameters your model was trained with. Especially, the default stride in this repository is set to 2. If you use the pre-trained "multi_share_eye_res50_stride1_epoch30" model, you should change the "in_stride" parameter in the "gaze_network" of "multi_region_res50_share_eyenet.py" file to 1. Then run `python main.py --is_train False`. 

## 2. Obtain gaze error
You are supposed to see a txt file called **within_eva_results.txt** after finishing testing. Put this file in a folder and zip it, the upload it to the [Codalab page](https://codalab.lisn.upsaclay.fr/competitions/7423) for testing results on ETH-XGaze. 

<br/>

# Benchmark your own model
First, give your model a name, then specify whether your model needs a single face image and multi-region images in *get_load_mode* in **main.py**. Initialize your model at L60-77 in **trainer.py**. The forward pass is performed from L160 and L230 in **trainer.py**. 

<br/>

# Pre-trained models
Please find the pre-trained multi-region models at this [link](https://drive.google.com/drive/folders/1v8TGgP2ahDQHZyQAHf_k0V7uvm6aXY06?usp=sharing). \
Please find the pre-trained face input [PoolFormer](https://arxiv.org/abs/2111.11418) model at this [link](https://drive.google.com/drive/folders/1kIibMDek8k4FvWAvsNM6Gfvu8s99UMWD?usp=sharing).


<br/>

# Miscellaneous

If you would like to draw a gaze arrow, please refer to the [demo.py](https://github.com/xucong-zhang/ETH-XGaze/blob/master/demo.py) of the ETH-XGaze official implementation. 

<br/>

# Citation
If you use results or models from our work, please consider citing our paper: 

    @misc{wang2023investigation,
          title={Investigation of Architectures and Receptive Fields for Appearance-based Gaze Estimation}, 
          author={Yunhan Wang and Xiangwei Shi and Shalini De Mello and Hyung Jin Chang and Xucong Zhang},
          year={2023},
          eprint={2308.09593},
          archivePrefix={arXiv},
          primaryClass={cs.CV}
    }
<br/>
If you use the ETH-XGaze dataset, please cite the dataset paper:

    @inproceedings{Zhang2020ETHXGaze,
      author    = {Xucong Zhang and Seonwook Park and Thabo Beeler and Derek Bradley and Siyu Tang and Otmar Hilliges},
      title     = {ETH-XGaze: A Large Scale Dataset for Gaze Estimation under Extreme Head Pose and Gaze Variation},
      year      = {2020},
      booktitle = {European Conference on Computer Vision (ECCV)}
    }

<br/>


