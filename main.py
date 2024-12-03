#!/usr/bin/env python3

from enum import Enum
from random import randint

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Player:
  def __init__(self, paramName: str = "Computer"):
        self.score = 0
        self.name = paramName
        self.choice = 0

  def choose(self):
        if self.name == "Computer":
          # between 1-3 !
          self.choice = randint(1, 3)
        else:
          while True:
              self.choice = int( input(f"1 - {Shape(1).name}\n2 - {Shape(2).name}\n3 - {Shape(3).name}\n\nPlease enter your choice: "), 10 )
              if self.choice in range(1, 4):
                break
              else:
                print("Invalid option. Please try again (rock, paper, scissors): ")

  def setScore(self, paramAddPoint: int):
        self.score += paramAddPoint

  def getScore(self):
        return self.score

class Game:
  def __init__(self, paramPlayername: str = "Player"):
        self.max_round = 3
        self.round = 1
        self.computer = Player()
        self.player = Player(paramPlayername)

  def nextRound(self):
        self.round += 1

  def play(self):
        while (self.round <= self.max_round):
            self.display_round()
            self.player.choose()
            self.computer.choose()
            self.adjust_score()
            self.display_scores()

  def adjust_score(self):
        # rock > scissors
        # paper > rock
        # scissors > paper
        computerChoice = self.computer.choice
        playerChoice = self.player.choice

        if (computerChoice == playerChoice):
            return

        if ((computerChoice == Shape.ROCK.value and playerChoice == Shape.SCISSORS.value) or \
            (computerChoice == Shape.PAPER.value and playerChoice == Shape.ROCK.value) or \
            (computerChoice == Shape.SCISSORS.value and playerChoice == Shape.PAPER.value)):
            self.computer.setScore(1)
        else:
            self.player.setScore(1)
        self.nextRound()

  def determine_winner(self):
        return self.computer.name if self.computer.score > self.player.score else self.player.name

  def display_round(self):
        print(f"\n=== Round {self.round} ===")

  def display_scores(self):
        print(f"\n[{self.player.name} ({self.player.getScore()})] {Shape(self.player.choice).name} --VS-- {Shape(self.computer.choice).name} [Computer ({self.computer.getScore()})]")

if __name__ == "__main__":
    playername = input("Enter playername: ")
    if len(playername) > 0:
      game = Game(playername)
    else:
      game = Game()
    game.play()
    print(f"\n{game.determine_winner()} WON!")
