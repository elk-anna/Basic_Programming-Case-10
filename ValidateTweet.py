def validate_tweet(input_text):
    if len(input_text) <= 140:
        return input_text
    else:
        return input_text[:140] + "..."

tweet = "A" * 150
print(validate_tweet(tweet))
