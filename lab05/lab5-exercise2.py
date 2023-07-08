import requests
import json 

url ="https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges =response.json()

print(challenges)
print("___________________________________________________________________")
# We are copying the json response to data and parsing it in loop.
# We then evaluate each of the problem using pythons eval function.
data = challenges

print("Name : Alok Kumar Reddy")
print("Blazer ID: aboyapal")
for problem in data:
    problem_text = problem['problem']
    problem_text = problem_text.replace('?', '')  # We remove the question mark to avoid data or compatibility errors here
    
    # Evaluate the problem and get the answer
    answer = eval(problem_text)
    
    print(f"Problem: {problem_text}")
    print(f"Answer: {answer}")
    print()
print("___________________________________________________________________")

