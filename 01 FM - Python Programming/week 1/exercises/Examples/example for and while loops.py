print(f"Hello User!")
name= input("Please Enter Your Name Here:")
email= input("PLease Enter Your Email Here:")
cellphone_no= input("Please Enter Your Cellphone Number Here:")
print(f"Hi {name}, Create Your Password Down Bellow.")
secret_password= input("Password:")
print(f"Your secret password is {secret_password}. Please pass the game over to your friend and enjoy the game")
special_word= secret_password
user_guesser= 0

while user_guesser != secret_password:
    user_guesser= input("Guess the secret password:")

    if user_guesser == secret_password:
        print(f"You guessed it. Well done!")
    
    else:
        print(f"Try Again buddy")