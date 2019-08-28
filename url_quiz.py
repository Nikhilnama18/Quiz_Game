import requests
from random import shuffle


"""
    This program is about a quiz 

"""


def verify(op, ans):
    """
        Verifyies op and ans are same or not
    """
    if op == ans:
        print("Not bad!")

    else:
        print("Not the answer we think !")


def main():

    response = requests.get("https://opentdb.com/api.php?amount=2&type=multiple")
    x = response.json()

    answers = []
    to_options = []
    for i in range(2):

        print(x["results"][i]["question"])
        answers.append(x["results"][i]["correct_answer"])

        to_options.append(x["results"][i]["correct_answer"])

        for k in range(3):

            to_options.append(x["results"][i]["incorrect_answers"][k])
        shuffle(to_options)
        for n in to_options:
            print(n)

        option = input("Type your answer from the above options:\n")

        verify(option, answers[0])
        answers.clear()
        to_options.clear()
        # print(answers[i])


if __name__ == "__main__":
    main()
