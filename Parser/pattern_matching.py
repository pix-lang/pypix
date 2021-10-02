import re

if_statement = re.compile(r'if (.*) ({.*})')
while_loop = re.compile(r'while (.*) ({.*})')


def condition_evaluation(pattern: re.Pattern, lexem: str) -> tuple[str, str]:
    # Matching the pattern according to the type of statement
    # and returning the condition and code to be executed(evaluation)
    # Example: lexem = "if (condition) {evaluation}"
    # mo.group(1) = "(condition)"
    # mo.group(2) = "{evaluation}"
    mo = pattern.search(lexem)
    condition = mo.group(1)
    evaluation = mo.group(2)

    # Striping of parenthesis
    # Example: "(condition)" -> "condition"
    condition = condition[1:-1]
    evaluation = evaluation[1:-1]

    return condition, evaluation
