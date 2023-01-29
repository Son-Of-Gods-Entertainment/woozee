

# -*- coding: utf-8 -*-
import numpy as np
import copy


class Gomoku(object):
    def __init__(self, board_size=15):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size))
        self.player = 1  # 1表示黑棋，2表示白棋
        self.step = 0
        self.score = 0

    def play_a_step(self):
        if self.step == 0:
            self.board[7, 7] = 1
            self.step += 1
            return self.board
        else:
            self.gen_next_step()
            self.step += 1
            return self.board

    def gen_next_step(self):
        if self.player == 1:  # 黑棋
            next_step = self.negamax(self.board, self.player, 3)
            self.board[next_step[0], next_step[1]] = 1
            self.player = 2
        else:
            next_step = self.negamax(self.board, self.player, 3)
            self.board[next_step[0], next_step[1]] = 2
            self.player = 1

    def check_winner(self):
        # 检查横向
        for i in range(self.board_size):
            for j in range(self.board_size - 4):
                if self.board[i, j] != 0:
                    if (self.board[i, j] == self.board[i, j + 1] == self.board[i, j + 2] ==
                            self.board[i, j + 3] == self.board[i, j + 4]):
                        return self.board[i, j]
        # 检查纵向
        for i in range(self.board_size - 4):
            for j in range(self.board_size):
                if self.board[i, j] != 0:
                    if (self.board[i, j] == self.board[i + 1, j] == self.board[i + 2, j] ==
                            self.board[i + 3, j] == self.board[i + 4, j]):
                        return self.board[i, j]
        # 检查左斜线
        for i in range(self.board_size - 4):
            for j in range(self.board_size - 4):
                if self.board[i, j] != 0:
                    if (self.board[i, j] == self.board[i + 1, j + 1] == self.board[i + 2, j + 2] ==
                            self.board[i + 3, j + 3] == self.board[i + 4, j + 4]):
                        return self.board[i, j]
        # 检查右斜线
        for i in range(self.board_size - 4):
            for j in range(4, self.board_size):
                if self.board[i, j] != 0:
                    if (self.board[i, j] == self.board[i + 1, j - 1] == self.board[i + 2, j - 2] ==
                            self.board[i + 3, j - 3] == self.board[i + 4, j - 4]):
                        return self.board[i, j]
        return 0  # 无人获胜

    def negamax(self, board, player, depth):
        empty_list = np.argwhere(board == 0)
        if len(empty_list) == 0:  # 无空格可落子，返回当前分数
            return 0
        elif depth == 0:  # 已达到搜索深度，返回当
if(result.code == 0){
//清空表单
					$("#name").val("");
					$("#name").focus();
				}
			
		});
	});
});
