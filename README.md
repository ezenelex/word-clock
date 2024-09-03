![alt text](https://github.com/ezenelex/word-clock/blob/master/image.jpg?raw=true)

This repo is meant as a backup and showcase of my work. It is not intended to be a guide for re-creation.

Explanation

This device displays the time using words instead of numbers. All the letters and their arrangements required to tell any time in five minute intervals are placed in a grid. Behind each letter is an individually addressable WS2812B LED, which is used to illuminate words. 

The code constantly checks the current time and compares it to the currently displayed time. If there is a discrepancy of more than 5 minutes, the display must update.

To update the display, the current time must be broken down from a pure millisecond value into hours and minutes of the correct time zone. Once these values are obtained, they must be matched with the correct pixels to light up the correct words needed to display that specific time. (e.g. "It is twenty five minutes to twelve oclock")
