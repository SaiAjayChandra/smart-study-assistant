answers = {
    "what is python": "Python is a programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is json": "JSON is a format used to store and exchange data.",
    "what is api": "An API allows different programs to communicate.",
    "what is a dictionary": "A dictionary stores data as key-value pairs."
}
while True:
      print("Smart Study Assistant")
      print("1) Ask a Question")
      print("2) View Chat History")
      print("3) Exit")
      try:
          option = int(input("Please enter an option:"))
    
          if option == 1:
              question = input("Ask your question:").lower().strip().replace("?", "")
              if question in answers:
                    answer = answers[question]
                    print(answer)
              else:
                    answer = "Sorry, I don't know that yet."
                    print(answer)
              with open("chat_history.txt","a") as file:
                        file.write("User: " + question + "\n")
                        file.write("Bot: " + answer + "\n\n")
          elif option ==2:
               
               try:
                    with open ("chat_history.txt", "r") as file:
                        content = file.read()
                        print(content)
               except FileNotFoundError:
                       print('Sorry no search history recorded yet')
          elif option == 3:
               print('Thank you. Good Bye')
               break
          else:
              print('Invalid option. Try again')
      except ValueError:
             print('Enter a Valid option in integer numbers')
            
          