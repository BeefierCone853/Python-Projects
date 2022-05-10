# *Password Generator*

Python project which generates and saves passwords. When the password is created it is automatically copied to the
clipboard. The project was created using **tkinter**, **random**, **pyperclip** and **json** imports. 
It has the following functions :  
### *generate_password*
- generates a password which is a combination of letters, symbols and numbers
- called when the **"Generate Password"** button is clicked

### *save*:
- saves a password into a json file (along with the entered e-mail)
- called when the **"Add"** button is clicked

### *search*:
- searches for the e-mail and password for the entered website
- called when the **"Search"** button is clicked
- if the the entered website cannot be found or there is no json file an error is raised
