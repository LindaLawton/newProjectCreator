# Python new project creator

I create a lot of new projects for each of my clients and when I am testing things.  My project layout template 
has been the same for years.  I decided to take a page out of the book from a previous client and create my own
script to do this.

use at your own risk

# Add to env path

Add the directory to your PATH: Add the directory containing your script to your system's PATH environment variable.

On Windows:
- Open Control Panel.
- Go to System and Security > System.
- Click on "Advanced system settings" on the left panel.
- Click on the "Environment Variables..." button.
- Under "System variables" or "User variables", find the "Path" variable and click "Edit...".
- Add the path to your directory containing the script (e.g., C:\Users\YourUsername\scripts) to the list of paths.
- Click OK on all windows to close them.

# run it

once added to the env path you can just call it with the name of the new project and it will create a new directory  
right where you are 

    create_project new_project_name