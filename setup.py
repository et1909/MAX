import platform
import requests, zipfile, io
import subprocess


def setup():
    open("user.txt", "w")  # opens a file for username
    open("password.txt", "w")  # opens a file for password

    print(
        "THIS SETUP FILE WILL INSTALL SELENIUM WEBDRIVER FOR CHROME. IF YOU AGREE PRESS [Y] TO ACCEPT AND [N] TO DECLINE")

    my_system = platform.uname()  # uname consists of all the info about the system that the module is running on.

    system_info = my_system.system  # prints the system os

    if system_info == "Windows":
        print("HELLO")
        file_url = "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip"  # heads to the file url
        r = requests.get(file_url, stream=True)  # request get means it fetches the url and stream allows the connection
        # to be opened so that the programmer can execute code even after the request is sent.
        z = zipfile.ZipFile(io.BytesIO(r.content))  # zipfile is the module calling ZipFile which opens the zip file in
        # read and write format.
        z.extractall(path="C:\\Program Files (x86)")  # extractall extracts the zip file to the current working
        # directory when the dev has not mentioned the path.
        subprocess.run("pip install selenium")
        subprocess.run("pip install beautifulsoup4")
        subprocess.run("pip install lxml")
    elif system_info == "Linux":
        print("HELLO")
        file_url = "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip"  # heads to the file url
        r = requests.get(file_url, stream=True)  # request get means it fetches the url and stream allows the connection
        # to be opened so that the programmer can execute code even after the request is sent.
        z = zipfile.ZipFile(io.BytesIO(r.content))  # zipfile is the module calling ZipFile which opens the zip file in
        # read and write format.
        z.extractall(path="/usr/local/bin")  # extractall extracts the zip file to the current working
        # directory when the dev has not mentioned the path.
        subprocess.run(["pip" ,"install" ,"selenium"])
        subprocess.run(["pip" ,"install" ,"beautifulsoup4"])
        subprocess.run(["pip", "install" ,"lxml"])
    elif system_info == "Darwin":
        print("HELLO")
        file_url = "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_mac64.zip"  # heads to the file url
        r = requests.get(file_url, stream=True)  # request get means it fetches the url and stream allows the connection
        # to be opened so that the programmer can execute code even after the request is sent.
        z = zipfile.ZipFile(io.BytesIO(r.content))  # zipfile is the module calling ZipFile which opens the zip file in
        # read and write format.
        z.extractall(path="/usr/local/bin")  # extractall extracts the zip file to the current working
        # directory when the dev has not mentioned the path.
        subprocess.run(["pip" ,"install" ,"selenium"])
        subprocess.run(["pip" ,"install" ,"beautifulsoup4"])
        subprocess.run(["pip", "install" ,"lxml"])
    else:
        print(
            "SYSTEM NOT RECOGNIZED. ENSURE THAT THE SYSTEM IS EITHER [Windows]/[Linux]/[MacOS]. \n CONTACT DEVELOPER FOR MORE INFO")

    print("SETUP FOR MAX IS COMPLETE YOU CAN NOW RUN THE AUTOMATE_FINAL.PY")


setup()
