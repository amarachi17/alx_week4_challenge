# Ask the user for different words

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter the final adjective: ")

# Building a template story for the user provided input
story_template = """ On a beautiful {adj1} day, I went to the zoo. I saw a funny {adj2} monkey swinging from the trees. Then, I spotted a majestic {adj3} lion lounging in the sun. What a wild and {adj4} experience! """

# Add variation based on user input
if adjective4.lower() == "exciting":
    story_template += "\nIt was the most exciting days of my life!"
elif adjective4.lower() == "boring":
    story_template += "\nI hope my next visit to the zoo will be more interesting."
else:
    story_template += "\nI will never forget this {adjective4} day at the zoo."
    
# Display the final story
story = story_template.format(adj1=adjective1, adj2=adjective2, adj3=adjective3, adj4=adjective4)
print(story)