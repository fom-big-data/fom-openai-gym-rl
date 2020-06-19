import os

import numpy as np


class PerformanceLogger:

    def log_parameters(directory, batch_size, gamma, eps_start, eps_end, eps_decay, num_atoms, vmin, vmax,
                       target_update, replay_memory_size, num_frames,
                       reward_pong_player_racket_hits_ball,
                       reward_pong_player_racket_covers_ball,
                       reward_pong_player_racket_close_to_ball_linear,
                       reward_pong_player_racket_close_to_ball_quadratic,
                       reward_pong_opponent_racket_hits_ball,
                       reward_pong_opponent_racket_covers_ball,
                       reward_pong_opponent_racket_close_to_ball_linear,
                       reward_pong_opponent_racket_close_to_ball_quadratic,
                       reward_breakout_player_racket_hits_ball,
                       reward_breakout_player_racket_covers_ball,
                       reward_breakout_player_racket_close_to_ball_linear,
                       reward_breakout_player_racket_close_to_ball_quadratic,
                       reward_spaceinvaders_player_avoids_line_of_fire,
                       reward_freeway_chicken_vertical_position):
        # Make path if not yet exists
        if not os.path.exists(directory):
            os.mkdir(directory)

        line = "BATCH_SIZE=" + str(batch_size) \
               + "\nGAMMA=" + str(gamma) \
               + "\nEPS_START=" + str(eps_start) \
               + "\nEPS_END=" + str(eps_end) \
               + "\nEPS_DECAY=" + str(eps_decay) \
               + "\nNUM_ATOMS=" + str(num_atoms) \
               + "\nVMIN=" + str(vmin) \
               + "\nVMAX=" + str(vmax) \
               + "\nTARGET_UPDATE=" + str(target_update) \
               + "\nREPLAY_MEMORY_SIZE=" + str(replay_memory_size) \
               + "\nNUM_FRAMES=" + str(num_frames) \
               + "\nREWARD_PONG_PLAYER_RACKET_HITS_BALL=" + str(reward_pong_player_racket_hits_ball) \
               + "\nREWARD_PONG_PLAYER_RACKET_COVERS_BALL=" + str(reward_pong_player_racket_covers_ball) \
               + "\nREWARD_PONG_PLAYER_RACKET_CLOSE_TO_BALL_LINEAR=" + str(
            reward_pong_player_racket_close_to_ball_linear) \
               + "\nREWARD_PONG_PLAYER_RACKET_CLOSE_TO_BALL_QUADRATIC=" + str(
            reward_pong_player_racket_close_to_ball_quadratic) \
               + "\nREWARD_PONG_OPPONENT_RACKET_HITS_BALL=" + str(reward_pong_opponent_racket_hits_ball) \
               + "\nREWARD_PONG_OPPONENT_RACKET_COVERS_BALL=" + str(reward_pong_opponent_racket_covers_ball) \
               + "\nREWARD_PONG_OPPONENT_RACKET_CLOSE_TO_BALL_LINEAR=" + str(
            reward_pong_opponent_racket_close_to_ball_linear) \
               + "\nREWARD_PONG_OPPONENT_RACKET_CLOSE_TO_BALL_QUADRATIC=" + str(
            reward_pong_opponent_racket_close_to_ball_quadratic) \
               + "\nREWARD_BREAKOUT_PLAYER_RACKET_HITS_BALL=" + str(reward_breakout_player_racket_hits_ball) \
               + "\nREWARD_BREAKOUT_PLAYER_RACKET_COVERS_BALL=" + str(reward_breakout_player_racket_covers_ball) \
               + "\nREWARD_BREAKOUT_PLAYER_RACKET_CLOSE_TO_BALL_LINEAR=" + str(
            reward_breakout_player_racket_close_to_ball_linear) \
               + "\nREWARD_BREAKOUT_PLAYER_RACKET_CLOSE_TO_BALL_QUADRATIC=" + str(
            reward_breakout_player_racket_close_to_ball_quadratic) \
               + "\nREWARD_SPACEINVADERS_PLAYER_AVOIDS_LINE_OF_FIRE=" + str(
            reward_spaceinvaders_player_avoids_line_of_fire) \
               + "\nREWARD_FREEWAY_CHICKEN_VERTICAL_POSITION=" + str(reward_freeway_chicken_vertical_position)

        # Print log
        print(line)

        # Write log into file
        log_file = open(directory + "/parameters.txt", "a")
        log_file.write(line + "\n")
        log_file.close()

    def log_episode(directory, total_episodes, total_frames, total_duration, total_original_rewards,
                    total_shaped_rewards, episode_frames, episode_original_reward,
                    episode_shaped_reward, episode_loss, episode_duration):
        # Make path if not yet exists
        if not os.path.exists(directory):
            os.mkdir(directory)

        avg_frames_per_minute = total_frames / (total_duration / 60)
        # avg_episodes_per_minute = total_episodes / (total_duration / 60)
        avg_original_reward_per_episode = np.mean(total_original_rewards[-50:])
        avg_shaped_reward_per_episode = np.mean(total_shaped_rewards[-50:])

        line = ("{: 5d}".format(total_episodes)
                + " {: 5d}".format(episode_frames) + "f"
                + " {: 4d}".format(round(episode_duration)) + "s"
                + " {: 4d}".format(round(avg_frames_per_minute)) + "f/min"
                + "     "
                + " reward {: 3f}".format(round(episode_original_reward, 2))
                + " reward(shaped) {: 3f}".format(round(episode_shaped_reward, 2))
                + " avg reward per episode {: 3f}".format(round(avg_original_reward_per_episode, 2))
                + " avg reward(shaped) per episode {: 3f}".format(round(avg_shaped_reward_per_episode, 2))
                + " loss " + str(round(episode_loss, 4)))

        # Print log
        print(line)

        # Write log into file
        log_file = open(directory + "/log.txt", "a")
        log_file.write(line + "\n")
        log_file.close()
