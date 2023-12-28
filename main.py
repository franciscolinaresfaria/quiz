def asking(question: str, answer: str):
  data = input(question)
  if data.lower() == answer:
    return True


def consent(question: str, answer: str):
  data = input(question)
  if data.lower() == answer:
    return "Okay! Let's play :) "
  else:
    quit()


score = 0

questions = {
    "¿What CPU stands for? ": "central proccess unit",
    "What GPU stands for? ": "graphics proccess unit",
    "What RAM stands for? ": "random access memory",
    "What PSU stands for? ": "power supply",
    "Who is the bonitost cat in the world? ": "piquito",
    "Who is the bonitast cat in the world? ": "chiquitina",
}
print("Welcome to my computer quiz!")

print(consent("Do you want to play: ", "yes"))

for question, answer in questions.items():
  if asking(question, answer):
    score += 1
    print("Correct!")
  else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 6) * 100) + "%.")
