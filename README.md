# card_count
Card counting project which allows for better odds on the game BlackJack
Normally house edge is 0.5% but with this card counting (hi-low) strategy you have a 0.5% edge over the house

`Divide the running count by the number of decks remaining, to get what is known as the "True Count."`

## The running count?
The running count assign a point value to each rank, as follows

# Card Counting Reference Table

| Card Rank | Running Count Value |
|:---------:|:------------------:|
| 2         | +1                 |
| 3         | +1                 |
| 4         | +1                 |
| 5         | +1                 |
| 6         | +1                 |
| 7         | 0                  |
| 8         | 0                  |
| 9         | 0                  |
| 10        | -1                 |
| J         | -1                 |
| Q         | -1                 |
| K         | -1                 |
| A         | -1                 |

## Description
This table represents the Hi-Lo card counting system used in Blackjack:
- Low cards (2-6): Add 1 to the running count
- Neutral cards (7-9): Add 0 to the running count
- High cards (10-A): Subtract 1 from the running count

To get the true count, divide the running count by the number of decks remaining
