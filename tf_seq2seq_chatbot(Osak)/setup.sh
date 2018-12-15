#!/usr/bin/env bash

# create and own the directories to store results locally
save_dir='/home/marlboro/wht/tf_seq2seq_traj_Osak'
sudo mkdir -p $save_dir'/data/'
sudo mkdir -p $save_dir'/nn_models/'
sudo mkdir -p $save_dir'/results/'
sudo chown -R "$USER" $save_dir

# copy train and test data with proper naming
data_dir='tf_seq2seq_chatbot/data/train/20170328Osak_random_num5'
cp $data_dir'/Osakchat_train.txt' $save_dir'/data/chat.in'
cp $data_dir'/Osakchat_test.txt' $save_dir'/data/chat_test.in'
cp $data_dir'/Osakchat.txt' $save_dir'/data/chatvoc.in'