#open-cv tutorial

## Python tips learned
1. Start a virtual environment
> python3 -m venv venv/
2. Activate the virtual environment
> source venv/bin/activate
3. Install dependencies based on dependencies file
> pip3 install -r dependencies.txt
4. Check dependencies on virtual environment
> pip3 list
5. Update dependencies file with new packages
> pip3 freeze > dependencies.txt
6. Deactivate the virtual environment
> deactivate
7. Generate pylint file
> pylint --generate-rcfile > .pylintrc