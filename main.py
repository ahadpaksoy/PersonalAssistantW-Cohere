import set_timer
import nlp_tagging

def main():
    user_command = "Set a timer for 10 minutes"
    setted_timer = nlp_tagging.set_timer(user_command)
    print(setted_timer) 

if __name__ == "__main__":
    main()