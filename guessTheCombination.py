import requests
import re

numbers = [51, 89, 77, 93, 126, 14, 93, 10]
phrase = [0, 0, 0, 0, 0, 0, 0, 0]

alphabets_in_lowercase=[]
for i in range(97,123):
    alphabets_in_lowercase.append(chr(i))

alphabets_in_capital=[]
for i in range(65,91):
    alphabets_in_capital.append(chr(i))

alphabet = []
for i in range(0, len(alphabets_in_capital)):
    alphabet.append(alphabets_in_lowercase[i])
    alphabet.append(alphabets_in_capital[i])

for i in range(0, len(alphabet)):
    # Create the request object
    req = requests.Request(method='POST', url='http://10.10.48.62/game1/')

    # Add additional headers, query parameters, etc.
    req.data = {'answer': alphabet[i]}

    # Prepare the request
    prepared_req = req.prepare()

    # Send the request
    resp = requests.Session().send(prepared_req)

    # Parse the response
    if resp.status_code == 200:
        data = resp.text
        pattern = r'Your hash:  (\d+)'
        match = re.search(pattern, data)
        if match:
            number = int(match.group(1))
            for j in range(0, len(numbers)):
                if number == numbers[j]:
                    print(f"{number} = {alphabet[i]}")
                    phrase[j] = alphabet[i]
    else:
        print('Request failed with status code: {}'.format(resp.status_code))

print(f"Full phrase: {phrase}")