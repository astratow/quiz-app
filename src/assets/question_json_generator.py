import json

# Supported question types
QUESTION_TYPES = [
    'same-letter-mc',
    'multiple-choice'
]

def prompt(msg, default=None):
    val = input(f"{msg}{' [' + default + ']' if default else ''}: ").strip()
    return val if val else default

def get_same_letter_mc():
    print("\nEnter details for 'same-letter-mc' question:")
    frag1 = prompt("First fragment (e.g. dis [?] urt)")
    frag2 = prompt("Second fragment (e.g. muc [?] ole)")
    options = []
    option_letters = []
    for label in ['A', 'B', 'C', 'D', 'E']:
        letter = prompt(f"Option {label} (letter)")
        options.append(label)
        option_letters.append(letter)
    correct = prompt("Correct letter (must match one of the above)")
    explanation = prompt("Explanation")
    return {
        "type": "same-letter-mc",
        "text": [frag1, frag2],
        "options": options,
        "optionLetters": option_letters,
        "correct": correct,
        "explanation": explanation
    }

def get_multiple_choice():
    print("\nEnter details for 'multiple-choice' question:")
    text = prompt("Question text")
    answers = []
    for i in range(4):
        ans = prompt(f"Option {chr(65+i)}")
        answers.append(ans)
    correct = prompt("Correct answer (must match one of the above exactly)")
    explanation = prompt("Explanation")
    return {
        "type": "multiple-choice",
        "text": text,
        "answers": answers,
        "correct": correct,
        "explanation": explanation
    }

def main():
    questions = []
    print("Quiz Question JSON Generator\n------------------------------")
    while True:
        print("\nSupported types:", ', '.join(QUESTION_TYPES))
        qtype = prompt("Question type", default="same-letter-mc")
        if qtype == 'same-letter-mc':
            q = get_same_letter_mc()
        elif qtype == 'multiple-choice':
            q = get_multiple_choice()
        else:
            print("Unsupported type. Try again.")
            continue
        questions.append(q)
        cont = prompt("Add another question? (y/n)", default="y")
        if cont.lower() != 'y':
            break
    out_file = prompt("Output JSON file name", default="questions.json")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(questions)} questions to {out_file}")

if __name__ == "__main__":
    main()
