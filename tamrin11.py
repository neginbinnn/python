import random
def simple_function(first_name, last_name, guess_age=False):
  full_name = first_name + " " + last_name
  if guess_age:
      age = random.randint(10,40)
  else:
    age = None

  return full_name, age

out = simple_function("jimy", " jmabo", guess_age=False)
print(out)