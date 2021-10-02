import re

if_statement = re.compile(r'if (.*) ({.*})')
while_loop = re.compile(r'while (.*) ({.*})')


def condition_evaluation(pattern: re.Pattern, lexem: str) -> tuple[str, str]:
    mo = pattern.search(lexem)
    condition = mo.group(1)
    evaluation = mo.group(2)

    return condition, evaluation
