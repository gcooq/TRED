#!/usr/bin/env bash

# create and own the directories to store results locally
save_dir='/home/marlboro/wht/tf_seq2seq_geolife_traj/'
sudo mkdir -p $save_dir'/data/'
sudo mkdir -p $save_dir'/nn_models/'
sudo mkdir -p $save_dir'/results/'
sudo chown -R "$USER" $save_dir

# copy train and test data with proper naming
data_dir='tf_seq2seq_chatbot/data/train/20170329_random_num2'
cp $data_dir'/geolife_beijing_trajectory_train.txt' $save_dir'/data/chat.in'
cp $data_dir'/geolife_beijing_trajectory_chat_withcon' $save_dir'/data/chatvoc.in'
cp $data_dir'/geolife_beijing_trajectory_test.txt' $save_dir'/data/chat_test.in'