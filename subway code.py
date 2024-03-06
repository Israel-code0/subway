import random
import time

def obstacle():
    obstacles = ['train', 'pillar', 'gate', 'signboard']
    return random.choice(obstacles)

def jump():
    return random.random() < 0.5

def game_over():
    print("Game Over! You crashed into an obstacle.")
    print("Your score:", score)
    exit()

def game():
    global score
    score = 0
    print("Welcome to Text-based Subway Surfers!")
    print("Jump over obstacles to survive.")
    print("Press 'j' to jump and 'q' to quit.")

    while True:
        obs = obstacle()
        print("Running... (Score: {})".format(score))
        time.sleep(1)
        
        action = input("Obstacle ahead: {}. Jump? (j/q): ".format(obs))
        if action == 'q':
            print("Game Over! Your final score:", score)
            break
        
        if jump():
            print("You jumped over the", obs)
            score += 1
        else:
            game_over()

if __name__ == "__main__":
    game()
