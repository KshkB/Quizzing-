# Quizzing game

This repository contains two quizzing games: 

- general game (`game1.py`);
- bombardment game (`bombardment.py`).

Both games call on the freely available API from the [Open Trivia Database](https://opentdb.com/).
The API token is found in the `generate_token` module.

A brief description of each game is given below.

## General game

In the general game, the player is asked to choose:

- a category (10 available);
- difficulty of questions (easy, medium or hard);
- a number of questions to answer.

The game then sources and presents random questions from the specified category and difficulty level. 
After answering all the questions, the percentage of correct questions is calculated and displayed, along with the quiz answers.

### Categories

The categories from which questions are sourced are:

- general knowledge;
- science and nature;
- computers science;
- mathematics;
- mythology;
- geography;
- history;
- politics;
- art;
- animals.

There are more categories in the Open Trivia Database.  

## Bombardment

There is less autonomy in the bombardment game which, as the name suggests, consists of the player being bombarded by quiz questions.
In the bombardment game, the player can only choose the difficulty level of quiz questions. The questions come from any of the 10 categories.
During the game the player is asked to answer one quiz question after another, *ad infinitum* (or, until the quiz database has been exhausted).
The player can choose to tap out after each question, whence the game ends and their performance is reported.
