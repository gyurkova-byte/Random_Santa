from santa_logic import get_participants, match_secret_santa, display_results, display_presents

def main():
    """The main feature of the Secret Santa program."""
    
    # 1. Display the list of gifts 
    display_presents()
    
    # 2. Get the participants' last names
    participant_names = get_participants()

    # 3. Randomly assign a sender and a recipientClick to apply
    santa_matches = match_secret_santa(participant_names)

    # 4. Display results
    display_results(santa_matches)

if __name__ == "__main__":
    main()