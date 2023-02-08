from puissance4 import * 


import pytest
import tkinter as tk
from tkinter import messagebox


class TestGame:
    @pytest.fixture
    def game(self):
        root = tk.Tk()
        game = Game(root)
        return game


    def test_is_winner(self, game):
        game.turn = 1
        game.grid = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0]]
        game.columns = [0,0,0,4,0,0,0]
        assert game.is_winner(3, 3, 1) == True

        game.turn = 2
        game.grid = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,2,0,0],[0,0,0,2,0,0],[0,0,0,2,0,0],[0,0,0,2,0,0]]
        game.columns = [0,0,0,4,0,0,0]
        assert game.is_winner(3, 3, 2) == True

        game.turn = 1
        game.grid = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,2,0,0],[0,0,0,1,0,0],[0,0,0,2,0,0]]
        game.columns = [0,0,0,4,0,0,0]
        assert game.is_winner(3, 3, 1) == False



    def test_is_tie(self, game):
        game.turn = 1
        game.columns = [6, 6, 6, 6, 6, 6, 6]
        game.grid = [[1, 2, 1, 2, 1, 2],
                     [2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2],
                     [2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2],
                     [2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2]]
        assert game.is_tie() == True

    def test_add_disc(self, game):
        game.turn = 1
        game.grid = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        game.columns = [0,0,0,0,0,0,0]
        game.add_disc(1)
        assert game.grid == [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        assert game.columns == [0,0,0,0,0,0,0]
        assert game.turn == 2
