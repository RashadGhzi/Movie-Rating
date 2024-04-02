## Language and Database Used

- This project is developed using Python programming language. The data is stored in an online PostgreSQL database provided by Railway.

## setup instructions

### 1. ** Clone the Repository: **
First, clone the repository to your local machine using the following command:
- command line: `git clone https://github.com/RashadGhzi/Movie-Rating.git`
Replace <repository_link> with the actual link to the GitHub repository.

### 2. ** Navigate to the Project Directory: **
After the download is complete, navigate to the inner project directory using the cd command:
- command line: `cd <project_directory>`
Replace <project_directory> with the name of the project directory.

### 3. ** Create a Python Virtual Environment: **
Create a Python virtual environment using the following command:
- command line: `python -m venv env`
This will create a virtual environment named env in the project directory.

### 4. ** Activate the Virtual Environment: **
Activate the virtual environment by running the activation script:
- command line on Windows: `.\env\Scripts\activate`
- On macOS and Linux: `source env/bin/activate`

### 5. ** Install Requirements: **
Install the project dependencies listed in the requirements.txt file using pip:
- command line on Windows: `pip install -r requirements.txt`

### 6. ** Run the Project: **
Once the dependencies are installed, you can run the project using the appropriate command for your project (e.g., `python manage.py runserver` for Django projects).

## Note: The movie_rating.json file containing the project's API URLs has been attached for reference.


## Authentication and CSRF Token
### Note: *** This project uses session-based authentication. When making POST requests, ensure that you include the CSRF token in the request headers. For any request without csrftoken, login and registration you must login first. ***


## Assumptions

### Internet Connection:
These setup instructions assume that you have a stable internet connection for cloning the repository from GitHub and installing dependencies using pip.

### Python Installed:
It is assumed that you have Python installed on your system. If not, you can download and install Python from the official Python website (https://www.python.org/).

### Git Installed:
The instructions assume that you have Git installed on your system. If Git is not installed, you can download and install it from the official Git website (https://git-scm.com/).

### Virtual Environment:
The setup instructions assume that you have python-venv installed. If not, you can install it using the following command:
`python -m pip install --user virtualenv`

### Project Dependencies:
It is assumed that the project dependencies are listed in the requirements.txt file. If not, you may need to manually install the required packages based on the project documentation or source code.

## How much of the problem you were able to solve :
- ** I had tried to solve all the problems. **

## Problems faced with incomplete parts (if any) 
- ** I have completed all aspects of the project. If there are any remaining parts, consider them as mistakes. ** 
