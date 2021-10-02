import re

if_statement = re.compile(r'if (.*) ({.*})')
while_loop = re.compile(r'while (.*) ({.*})')

code = """
if (condition) {evaluation} 

if (condition two) {evaluation} 

while (condition) {evaluation}
"""

matches = if_statement.findall(code)
print(matches)


