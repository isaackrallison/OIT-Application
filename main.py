
from flask import Flask, render_template, request

app = Flask(__name__)

"""routes the flask app to launch and render the html portion"""
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

"""gets the input from the textbox and converts it"""
@app.route('/post', methods=['POST'])
def convert():

    "gets input and checks validity"
    r_numeral = request.form.get('rNumeral')
    checked = check_input(r_numeral)

    "returns an error mesage if the input is invalid"
    if checked != 0:
        return render_template('index.html', result=checked)

    "converts to a number and back to roman numerals"
    converted = convert_to_numbers(r_numeral, d)
    back_to_roman = convert_numerals(converted,d)

    "sets a boolean value to true if the original and converted back roman numerals match false otherwise"
    conf = ""
    if back_to_roman == r_numeral:
        conf="True"
    else:
        conf="False"

    "updating index.html"
    return render_template('index.html', result=converted, confirmed=conf)

def check_input(numeral):
    """checks if the compnents of the input string are vaild roman numeral charecters"""
    for i in numeral:
        if i not in d:
            return "incorrect input format, please try again "
    return 0

def convert_to_numbers(numeral, d):
    """converts a Roman numeral into a decimal number"""
    count = 0
    total = 0
    gen = generate_symbol(numeral)
    curr = next(gen)
    while count < len(numeral):

        prev, curr = curr, next(gen)
        if d[curr] > d[prev]:
            total += d[curr] - d[prev]
            prev, curr = curr, next(gen)
            count += 2
        else:
            total += d[prev]
            count += 1

    return total


def generate_symbol(numeral):
    """generates the next symbol of the Roman Numeral"""
    for let in numeral:
        yield let
    while True:
        yield 'Zero'

def convert_numerals(num, d):
  """converts back to roman numerals using subtractive notation to ensure accuracy"""
  numeral = ''
  while num > 0:
    index = index_finder(num,d)
    if str(num)[0] == "4":
      numeral += list(d.keys())[index]
      numeral += list(d.keys())[index+1]
      num -= (list(d.values())[index+1] - list(d.values())[index])
    elif str(num)[0] == "9":
      numeral += list(d.keys())[index-1]
      numeral += list(d.keys())[index+1]
      num -= (list(d.values())[index+1] - list(d.values())[index-1])
    else:
      num -= list(d.values())[index]
      numeral += list(d.keys())[index]
  return numeral

def index_finder(num, d):
    """Finds the index of the largest Roman Numeral less than or equal to the number"""
    for i, val in enumerate(d.values()):
        if val > num:
            return i-1
    return -1

"dictionary with all roman numeral values and zero for convert to numbers"
d = {
    'Zero': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

if __name__ == "__main__":
    app.run()