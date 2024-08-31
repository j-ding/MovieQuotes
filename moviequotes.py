import pandas as pd
import random

quotes_df = pd.read_csv("movie_quotes.csv")

# Select a random quote from the dataframe
random_quote = quotes_df.sample(n=1)

# Create a text widget to display the random quote
quote_display_widget = Text(value=random_quote.iloc[0]['Quote'], description="Movie Quote:")

from ipywidgets import Text, Button, Output

quote_widget = Text(value="", placeholder="Movie Title", description="Movie Title:")
submit_widget = Button(description="Submit")

output_widget = Output()

def check_guess(b):
    user_guess = quote_widget.value.lower()
    random_movie = random_quote.iloc[0]['Movie'].lower()
    if user_guess in random_movie:
        # Increment score
        output_widget.clear_output()
        with output_widget:
            print("Correct! Your score is 1.")
    else:
        # Display incorrect message
        output_widget.clear_output()
        with output_widget:
            print("Incorrect! Try again.")

submit_widget.on_click(check_guess)

# Display the random quote, input field, and submit button
display(quote_display_widget)
display(quote_widget)
display(submit_widget)
display(output_widget)
