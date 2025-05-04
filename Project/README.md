# 🎴 UNO: Terminal-based Card Game in Python
#### Description:

This is a Python terminal-based version of the popular card game UNO.

The game includes:
- One human player and three bots.
- A fully shuffled deck following official UNO card distribution.
- Turn logic that supports Reverse, Skip, Draw Two, Wild, and Wild Draw Four.
- Win condition detection and game-ending logic.
- ASCII art (via pyfiglet) to enhance the game UI.

| File Name         | Description                        |
| ----------------- | ---------------------------------- |
| `project.py`      | Main game logic                    |
| `test_project.py` | Unit tests for game mechanics      |
| `requirements.txt`| Dependencies (`pyfiglet`, `pytest`)|

Design notes:
- Used a list of emoji strings to simulate cards visually.
- Used a global deck and player hands for simplicity in handling shared game state.
- Considered turn-based queue management to handle reverse and skip logic.

The game is text-based but simulates a full round of UNO with bot intelligence for playing matching or Wild cards.



### How to Play the Game

This is a command-line implementation of UNO, designed to simulate a full round between you and three bot players. Here's how the game works in detail:

1. **Starting the Game**:
   - After launching the program, you'll be greeted with a stylized welcome screen.
   - You'll be asked to enter your username.
   - Then, you will be prompted to start the game by pressing `1` or to quit by pressing `q`.

2. **Card Distribution**:
   - You and the three bots will each be dealt 7 cards.
   - A single card from the deck is placed face-up to start the discard pile.

3. **Taking Turns**:
   - The game proceeds in a clockwise direction unless a Reverse card is played.
   - On your turn, you will be shown your cards and asked to:
     - Select a card to play by entering its number, or
     - Enter `0` to draw a card from the deck if you have no playable cards.

4. **Playing Cards**:
   - You can only play a card if it matches the **color** or **type** (number or action) of the top card on the discard pile.
   - Special black cards (Wild and Wild Draw Four) can be played at any time and allow you to choose the next color.

5. **Special Cards**:
   - `Skip`: Skips the next player’s turn.
   - `Reverse`: Reverses the direction of play.
   - `Draw Two`: The next player draws two cards.
   - `Wild`: Lets you choose the next color.
   - `Wild Draw Four`: The next player draws four cards, and you choose the next color.

6. **Bots’ Strategy**:
   - Bots automatically attempt to play matching or wild cards.
   - If no valid card is available, they draw a card.

7. **Winning**:
   - The first player (you or a bot) to play all their cards wins.
   - The game then ends with a victory message in stylized ASCII art.

8. **Other Notes**:
   - The game handles all rule enforcement, including invalid selections and color choosing for Wild cards.
   - It provides prompts, feedback, and visual card representation using emojis for an engaging terminal experience.



## 🎉 Enjoy the Game!

I hope you have fun playing UNO right in your terminal!     🟦🟥🟨🟩
If you have any questions or feedback, I'd love to hear from you. Happy gaming!
