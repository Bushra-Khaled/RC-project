<br>

# Patient Booking System 
**<u>Overview:**</u> 
<p>This project is a simple  Booking System that helps doctors to manage thier patient appointments. the system allows the doctors to log in, view all bookings, edit and delete them.</p>
<p>the patient side of the system has a booking form that should be filled by the patient ot help the doctor to minimise thier action on filling the patient information as much as possible.</p>

# Diving more in the system
### Frontend Side
1. Doctor Login / sign up Page  ` / `  

    Allows doctors to log in with their credentials.
    
2. Booking Form Page `/booking`

    Provides a form for patients and doctors to create new bookings.


3. Dashboard Page `/dashboard` 

    Displays a table of all bookings with action buttons for editing, deleting, and adding new bookings.

   1.  Table to Show All Bookings \
   Displays a table with booking details such as patient name, date, and time, ..etc.

   2. Action Buttons 
      1. **Edit:** Redirect the doctors to  the edit page.
      2. **Delete:** Allows doctors to delete a booking.
      3. **Add:** Takes doctors to the booking form page to add a new booking.

4. Simple Edit Page `/edit/booking_id` \
        Allows doctors to edit the details of a specific booking.



### Backend Side
1. Login and Auth Function 
   
    Implements user authentication and login functionality.
2. Create New Booking Function 

    Adds a new booking to the system.
3. Show All Booking Function 
    
    Retrieves and displays all bookings in the dashboard.
4. Delete One Booking Function 

    Removes a specific booking from the system.
5. Edit/Update Booking Function 

    Modifies the details of a specific booking



## Istructions to start:
<p style="color:#000; background-color: #e3c4f0e1; padding: 5px"> <u>Hint:</u> for better view of the table let the width of your screen be between 1750 - 1890 px</p>

### What you need to run the project on local host:
1. Install Python 
2. Install Flask

## 1. Install Python on Windows:

1. Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for Windows.

2. Run the installer, making sure to check the box that says "Add Python to PATH" during the installation process.

3. Click "Install Now" and follow the installation wizard.

4. Once the installation is complete, open the Command Prompt and check the Python version:
    ```bash
    python --version
    ```

   or for Python 3:
    ```bash
    python3 --version
    ```


## 2. Install Python on macOS:

#### <b><u>Method 1:</u></b>  Using Homebrew (recommended):

1. Open the Terminal (you can find it using Spotlight by pressing `Cmd + Space` and then typing "Terminal").

2. Install Homebrew if you don't have it:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. Install Python using Homebrew:
    ```bash
    brew install python
    ```

4. Verify the installation:
    ```bash
    python3 --version
    ```

#### <b><u>Method 2:</u></b> Using the Python installer:

1. Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for macOS.

2. Open the downloaded package and follow the installation instructions.

3. Verify the installation by opening the Terminal and checking the Python version:
    ```bash
    python3 --version
    ``` 

## Install Flask:

1. Open the Terminal or Command Prompt.

2. Install Flask using pip:
    ```bash
    pip install Flask
    ```

3. Verify the Flask installation:
    ```bash
    flask --version
    ```
<br>
<br>

# How to Run

### <u>**Clone and Run Instructions:**</u>

### 1. Clone the Repository:

```bash
git clone https://github.com/Bushra-Khaled/RC-project.git
```
### 2. Navigate to the Project Directory:
```bash
cd RC-project
```
### 3. Run the Flask Application:
```bash
flask --app form.py run
```


<br>
<br>
<br>

Use it with pleasure <3 :) 