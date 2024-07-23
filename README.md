**LOTTO GAME**

The game Lotto is a game of chance where each bettor selects six different numbers. If those numbers match the drawn numbers, the bettor wins the accumulated prize for that round.

Consists of simulating a drawing of the mentioned game and informing the winners. For this, six whole numbers between 0 and 41 will be randomly generated, which must not be repeated. Once these winning numbers are obtained, the file "apuestas.txt" containing the bets for that round will be processed. The file is in CSV format and each line contains the following data:

<ID(of tthe bettor)>;<agency(code)>;<No 1>;<No 2>;<No 3>;<No 4>;<No 5>;<No 6>

Example: 34151620;31814;40;0;22;5;19;8

The program generates the winning numbers, process the betting file, and determine the bettors who matched 6 numbers. If there are none, it searchs for bettors with 5 matches, then 4, etc., until at least one winner is found. This variant is known as "Must Win". It displays the drawn numbers and print a list of winners (ID number and agency code), ordered in ascending order by the bettor's ID number and agency code as a secondary key.

The program also shows a list of participating agencies and the number of bettors who chose each of them. This list will be ordered from highest to lowest according to the number of bettors each agency has.

As an example, a betting file with 100,000 records called "apuestas.txt" is provided. Keep in mind that the program works for this or any other file that respects the indicated format, regardless of the number of records.
