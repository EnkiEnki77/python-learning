# Sometimes a single execution of a line of code isnt enough to get the desired result. This is where
# loops come into play

# The while loop requires the introduction of extra variables, this makes it quite slow. It resembles a
# conditional operator. It executes a set of statements while a condition is true.

# Condition is checked, if true code is run, and then looped back to condition. If false code block is skipped.

# We need a variable that is reassigned each iteration to bring us closer to condition result of False, so the
# loop can be stopped.
count = 0
while count < 5:
    print(count)
    count += 1

# Otherwise we run into an infinite loop
# while True:
#     print(count)