def greet():
  import random
  hello=random.choice(["Hello", "Hi", "Hey", "Greetings"])
  print(hello)
  return hello
greet()