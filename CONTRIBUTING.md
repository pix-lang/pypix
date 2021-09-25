# Contributing to PyPix
  - First of all, thank you for wanting to improve pypix!
  - The `README.md` file has the basic setup to start working on PyPix 
  - Please read this file entirely to make sure you are following all the rules :)
  - The first rule when wanting to add something is either open an issue in Github, or ask to solve someone elses issue.
  - Name your branch according to the issue number, example: `feature/issue-1002`
  - When done with your changes, please run the mentioned below tests to make sure that everything else still works.
 
## Prerequisite Knowledge
  - Incase you feel like contributing to PyPix but are unaware of how much you need to know,
  - PyPix code contributions would normally require knowledge on how lexical analysis works and decent knowledge at Python
  - Having worked with larger open source repositories and contrited to them is very important
  - Knowing Python conventions and format as per PEP8 -> https://www.python.org/dev/peps/pep-0008/

## File structure
  - There are many files involved in PyPix and this can make you feel overwhelmed but dont worry :)
  - When posting an issue(which is a must) you can always ask what relevant files you would need to look at
  - But generally, this is the basic file structure:
  - `Parser/` The Parser folder has the required programs to convert Pix files to meaningful commands.
  - The important files in this directory are 

## Testing 
  - Unsure if what you added may have potentially ruined everything else?
  - Done worry, go ahead and in the `pypix/` directory run `python -m unittest discover -s Tests/`
  - If all passes and you get `OK` at the end, great! You can now make a PR.
