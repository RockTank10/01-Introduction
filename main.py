#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

print("Hello there! Would you like to learn more about me?")
answer=input(": ")
answer=answer.lower()
if answer=="yes":
    print("""My name is Nolan McIntire. My current favorite game would be League
of Legends though it would be hard to choose my favorite game of all time. When it
comes to the class I am really only concerned with the amount of work, but I think
I should be fine. I am excited about the a few new games coming out soon as well
as a few of my classes. My stackoverflow id number is 11991293. The URL to my
github profile is https://github.com/RockTank10""")

else:
    print("Ok, I see how it is...")

print("Have a good day!")
