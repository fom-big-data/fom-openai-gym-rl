#! /bin/bash
export RUN_NAME=$(basename "$0")

export TELEGRAM_CONFIG_FILE="telegram.config"
export ENVIRONMENT_ID="PongNoFrameskip-v4"
export BATCH_SIZE=32
export LEARNING_RATE=0.0001
export GAMMA=0.99

export EPS_START=1.0
export EPS_END=0.01
export EPS_DECAY=10_000

export NUM_ATOMS=51
export VMIN=-10
export VMAX=10

export ETA=0.0
export BETA=0.0
export LAMBDA1=0.0

export NORMALIZE_SHAPED_REWARD=False
export REWARD_SHAPING_DROPOUT_RATE=0.75

export TARGET_UPDATE_RATE=10
export MODEL_SAVE_RATE=10
export EPISODE_LOG_RATE=10

export REPLAY_MEMORY_SIZE=100_000
export NUM_FRAMES=3_000_000

export REWARD_PONG_PLAYER_RACKET_COVERS_BALL=0.5
export REWARD_PONG_OPPONENT_RACKET_HITS_BALL=-0.5
export REWARD_POTENTIAL_BASED=0.0

./gcloud_atari_rainbow_dqn.py &
