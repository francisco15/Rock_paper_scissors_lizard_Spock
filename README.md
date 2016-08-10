# Mini-project description - Rock-paper-scissors-lizard-Spock

Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. Each choice wins against two other choices, loses against two other choices and ties against itself. Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory".
While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically determine who wins a round of RPSLS, coding up these rules would require a large number (5x5=25) of 𝚒𝚏/𝚎𝚕𝚒𝚏/𝚎𝚕𝚜e.
clauses. A simpler method for determining the winner is to assign each of the five choices a number:

0 — rock
1 — Spock
2 — paper
3 — lizard
4 — scissors

## Mini-project development process

1. Build a helper function 𝚗𝚊𝚖𝚎_𝚝𝚘_𝚗𝚞𝚖𝚋𝚎𝚛(𝚗𝚊𝚖𝚎) that converts the string 𝚗𝚊𝚖𝚎 into a number between 0 and 4 as described above. This function should use a sequence of 𝚒𝚏/𝚎𝚕𝚒𝚏/𝚎𝚕𝚜𝚎 clauses. You can use conditions of the form 𝚗𝚊𝚖𝚎 == '𝚙𝚊𝚙𝚎𝚛', etc. to distinguish the cases. To make debugging your code easier, we suggest including a final 𝚎𝚕𝚜𝚎 clause that catches cases when 𝚗𝚊𝚖𝚎 does not match any of the five correct input strings and prints an appropriate error message.

2. Next, you should build a second helper function 𝚗𝚞𝚖𝚋𝚎𝚛_𝚝𝚘_𝚗𝚊𝚖𝚎(𝚗𝚞𝚖𝚋𝚎𝚛) that converts a number in the range 0 to 4 into its corresponding name as a string. Again, we suggest including a final 𝚎𝚕𝚜𝚎 clause that catches cases when 𝚗𝚞𝚖𝚋𝚎𝚛 is not in the correct range.

3. Implement the first part of the main function 𝚛𝚙𝚜𝚕𝚜(𝚙𝚕𝚊𝚢𝚎𝚛_𝚌𝚑𝚘𝚒𝚌𝚎). Print out a blank line (to separate consecutive games) followed by a line with an appropriate message describing the player's choice. Then compute the number 𝚙𝚕𝚊𝚢𝚎𝚛_𝚗𝚞𝚖𝚋𝚎𝚛 between 0 and 4 corresponding to the player's choice by calling the helper function 𝚗𝚊𝚖𝚎_𝚝𝚘_𝚗𝚞𝚖𝚋𝚎𝚛() using 𝚙𝚕𝚊𝚢𝚎𝚛_𝚌𝚑𝚘𝚒𝚌𝚎.

4. Implement the second part of 𝚛𝚙𝚜𝚕𝚜() that generates the computer's guess and prints out an appropriate message for that guess. In particular, compute a random number 𝚌𝚘𝚖𝚙_𝚗𝚞𝚖𝚋𝚎𝚛 between 0 and 4 that corresponds to the computer's guess using the function 𝚛𝚊𝚗𝚍𝚘𝚖.𝚛𝚊𝚗𝚍𝚛𝚊𝚗𝚐𝚎(). We suggest experimenting with 𝚛𝚊𝚗𝚍𝚛𝚊𝚗𝚐𝚎 in a separate CodeSkulptor window before deciding on how to call it to make sure that you do not accidently generate numbers in the wrong range. Then compute the name 𝚌𝚘𝚖𝚙_𝚌𝚑𝚘𝚒𝚌𝚎 corresponding to the computer's number using the function 𝚗𝚞𝚖𝚋𝚎𝚛_𝚝𝚘_𝚗𝚊𝚖𝚎() and print an appropriate message with the computer's choice to the console.

5. Implement the last part of 𝚛𝚙𝚜𝚕𝚜() that determines and prints out the winner. Specifically, compute the difference between 𝚌𝚘𝚖𝚙_𝚗𝚞𝚖𝚋𝚎𝚛 and 𝚙𝚕𝚊𝚢𝚎𝚛_𝚗𝚞𝚖𝚋𝚎𝚛 taken modulo five. Then write an 𝚒𝚏/𝚎𝚕𝚒𝚏/𝚎𝚕𝚜𝚎 statement whose conditions test the various possible values of this difference and then prints an appropriate message concerning the winner. If you have trouble deriving the conditions for the clauses of this 𝚒𝚏/𝚎𝚕𝚒𝚏/𝚎𝚕𝚜𝚎 statement
