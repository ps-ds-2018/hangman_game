def print_hangman(wrong_guesses):
    hangman_stages = [
        "",  
        "___\n  |  \n  O  ",  
        "___\n  |  \n  O  \n  |  ",  
        "___\n  |  \n  O  \n /|  ",  
        "___\n  |  \n  O  \n /|\\ ",  
        "___\n  |  \n  O  \n /|\\ \n /   ",  
        "___\n  |  \n  O  \n /|\\ \n / \\ \nOops, you died!"  
    ]
    print(hangman_stages[wrong_guesses])
