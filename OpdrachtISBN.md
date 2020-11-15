# HogeschoolRotterdam
Opdracht Hogeschool Rotterdam(ISBN10 checker)
Analysis 1, 2021
Assignment Analysis 1, 2020/2021, Period 1
ISBN-10
summative assignment
Assignment objectives - Evaluate the ability to apply concepts learned in Analysis 1 (numeral systems,
Boolean logic, sets, algorithms) to problem solving.
Problem introduction
Humans are prone to make mistakes. When dealing with numbers, especially with long
sequences of numbers, we may accidentally miss a digit, duplicate another, swap the order
of adjacent digits, and so on. In some cases, those mistakes could be much more costly than
the others. For example, if you add 0 by mistake when paying your rent, it could alter the total
from 1000 € to 10000 €. Or if you want to transfer some money from your account to another
and you mistype one digit, your money could end up with a complete stranger.
Fortunately, there are fail safes to prevent, or at least minimize, such occurrences, and those
are often used in computing for error detection. One of those is checksum, which is a
calculated value used to determine the validity of data.
The International Standard Book Number (ISBN) is one such example. It is a numerical book
identifier and is unique for each book. Currently there are ISBN-10 and ISBN-13 versions, each
containing 10 or 13 digits respectively. In this assignment, we will focus on ISBN-10.
ISBN-10 became a world-wide standard in 1972. A 10-digit ISBN consists of 4 elements:
- A group element,
- A publisher prefix,
- A title element, and
- A check digit.
Example: ISBN 1-85375-390-4.
The elements of the code are separated by spaces or hyphens. The sizes of the first three
parts are variable, but together they are always 9 characters long. The first 9 digits (here:
185375390x) are actually codes, while the last one (xxxxxxxxx4) is used for checking if the
other digits are correct, hence its name – check digit.
The check digit is a value needed to be added to the control number so that it is divisible by
11. The control number is made of the first 9 digits (group, published and title) and is the sum
of the 1st digit multiplied by 10, plus the 2nd digit multiplied by 9, plus the 3rd digit multiplied
by 8, … , plus the 9th digit multiplied by 2.
For our example (1-85375-390-4), control number = 1x10 + 8x9 + 5x8 + 3x7 + 7x6 + 5x5 + 3x4
+9x3 +0x2 = 249.
control number / 11 = 249 / 11 = 22 R 7
check digit = 11 – 7 = 4
Test: (control number + check digit) / 11 = (249 + 4) / 11 = 253 / 11 = 23 (R 0)
Note: Since ISBN-10 uses a modulo-11 checksum, there are cases when the check digit is
actually 10. In that case, character X is used as check digit (X as Roman numeral for 10).
Problem statement
Read ISBN-10 from the standard input. Do not add any additional text to the user. Perform
the check to assure that the input is exactly 10 characters. If not, print “INPUT ERROR” and
exit the program. Also, the input should contain only digits, character ‘X’ (capital) and
character ‘.’ (dot). If any other character appears in the input, also print “INPUT ERROR” and
exit the program.
You are guaranteed that the input will contain either no ‘.’ (dots) or a single ‘.’ (dot). If the
input contains no ‘.’ (dots), then you should validate the given ISBN code using the rule
explained in the paragraph above. If the code is valid, then print “VALID” (all capitals). If the
code is not valid, then print “INVALID” (all capitals).
A single ‘.’ represents a missing ISBN character, and if given in the input, then you should use
the same rule to determine what should be the correct character in that position. Output the
correct character as string type.
Do not give any other output than what is described here.
Example input and output:
Input is given in BLUE. Required output is given in RED.
Case 1:
1853753903
INVALID
Case 2:
1853753904
VALID
Case 3:
185375390
INPUT ERROR
Case 4:
ISBN 1-8537-5390-4
INPUT ERROR
Case 5:
1-8537-5390-4
INPUT ERROR
Case 6:
18.3753904
5
Case 7:
1853753.04
9
Case 8:
005692013X
VALID
Case 9:
.05692013X
0
Case 10:
005692013.
X
Deliverables and working in groups - ZIP file containing:
o Source code (Python)
o Group info* (only if working in group)
Students are required to submit the source code of their solution implemented in Python.
Solution must be in a single file. No external libraries can be used (i.e. it must work on any
computer with standard Python 3 installation).
The flowchart is not required for this assignment, but it can be submitted.
The assignment can be completed by a student alone, or in a group of maximum two students
(if the student met the requirements to work in a group).
If a student is working alone, the student should submit one ZIP file containing source code
in Python. The name of the zip file should be in the following format: studentnumber.zip
If working in a group, only one group member submits the assignment. The ZIP file should
apply the rules mentioned above, PLUS it must include .txt file containing information about
members of the team (first row: student_number1 first_name1 last_name1, second row:
student_number2 first_name2 last_name2). The name of the zip archive is expected to be
in the following format: studentnumber1_studentnumber2.zip
In case of submitting via Microsoft Teams, one student (“lead”) makes the submission – sends
the zip file. The other group member(s) (“partner(s)”) must also make the submission, but
instead of sending the zip file, attaches a .txt file with information about the “lead” - the group
leader that made the submission (student number, first, last name).
Incomplete and improper submissions will be rejected!
Grading
The assignment will be evaluated as either PASS or FAIL. To get points for Analysis 1 course,
student must pass the summative assignment together with passing the exam.
Students will receive feedback from the teacher via Microsoft Teams Assignments (or any
other channel if specifically announced by the teacher).
In order to PASS the assignment must:
- Comply with format: Have input and output formatted exactly according to the
instructions given above. Printing text in the wrong line will result in the assignment
being rejected.
- Produce correct answer: For every test case (test cases are not shared) the algorithm
must give the correct answer. If one of the answers is incorrect, the assignment will
be rejected.
Deadlines
The students are required to submit the assignment before the midnight of November 15th
(Sunday). Submissions after the deadline will be rejected.
Students will receive the feedback from their teacher no later than December 7th.
