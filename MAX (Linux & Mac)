from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import bs4
from bs4 import BeautifulSoup
import requests
import zipfile
import io


print ("@@@@@@     @@@@@@         @@@@@@@        @@@          @@@")
print ("@@@ @@@   @@@ @@@        @@@   @@@         @@@      @@@")
print ("@@@  @@@ @@@  @@@       @@@     @@@          @@@  @@@ ")
print ("@@@           @@@      @@@  @@@  @@@            @@@ ")
print ("@@@           @@@     @@@         @@@         @@@  @@@")
print ("@@@           @@@    @@@           @@@      @@@      @@@")
print ("@@@           @@@   @@@             @@@   @@@          @@@")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument(
    '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
# Path to the Chrome webdriver that allows selenium to work
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH, options=chrome_options)  # value of driver variable.

driver.get("https://github.com/login")  # website to automate visit


def login(filename, listwords):
    try:
        files = open(filename, 'r')
        str = files.readlines()
        files.close()
        count = 0
        for word in listwords:
            lower = word.lower()
            for sentence in str:
                line = sentence.split()
                for each in line:
                    line2 = each.lower()
                    if lower == line2:
                        count += 1
            print(count)
            if count > 0:
                print("SAVED...")
                str = str[1:]
                # removetable = str.maketrans('', '', '@#%[]') #str.maketrans('remove this', 'with this',
                # 'remove special characters') out_list = [s.translate(removetable) for s in my_list]
                name_me = str[0]
                username = driver.find_element_by_id("login_field")
                username.send_keys(name_me)
            else:
                openfile = open("user.txt", "a")
                user_name = input("ENTER USERNAME : ")
                cred = []
                cred.append(user_name)
                for text in cred:
                    openfile.write("User\n")
                    openfile.write(user_name)
                openfile.close()
                username = driver.find_element_by_id("login_field")
                username.send_keys(user_name)

    except FileExistsError:
        print("NAH NAH")

    sleep(4)

    try:
        files1 = open('password.txt', 'r')
        str1 = files1.readlines()
        files1.close()
        count1 = 0
        for word in listwords:
            lower1 = word.lower()
            for sentence in str1:
                line1 = sentence.split()
                for each in line1:
                    line2 = each.lower()
                    if lower1 == line2:
                        count1 += 1
            print(count1)
            if count1 > 0:
                print("SAVED...")
                str1 = str1[1:]
                # removetable = str.maketrans('', '', '@#%[]') #str.maketrans('remove this', 'with this',
                # 'remove special characters') out_list = [s.translate(removetable) for s in my_list]
                name_me1 = str1[0]
                # print(name_me1)
                password = driver.find_element_by_id("password")
                password.send_keys(name_me1)
            else:
                openfile1 = open("password.txt", "a")
                pass_word = input("ENTER PASSWORD : ")
                cred = []
                cred.append(pass_word)
                for text in cred:
                    openfile1.write("User\n")
                    openfile1.write(pass_word)
                openfile1.close()
                password = driver.find_element_by_id("password")
                password.send_keys(pass_word)

    except FileExistsError:
        print("NAH NAH")

    sleep(4)

    submit = driver.find_element_by_name("commit")
    submit.send_keys(Keys.RETURN)
    sleep(3)


    print("IF YOU HAVE 2 FACTOR AUTHENTICATION SETUP PRESS [Y] KEY. IF NOT HIT [ENTER/RETURN] KEY.")
    two_factor_auth = input("YOUR ANSWER : ")
    if two_factor_auth.lower() == "y":
        driver.get("https://github.com/sessions/two-factor")
        otp = input("ENTER YOUR TWO FACTOR AUTHENTICATION CODE : ")
        otp_key = driver.find_element_by_id("otp")
        otp_key.send_keys(otp)
        verify = driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block']")
        verify.send_keys(Keys.RETURN)
    elif two_factor_auth == "":
        print("MOVING FORWARD...")


def repo():
    link = input(
        "[view] VIEW REPOSITORY\n[new] MAKE NEW REPOSITORY\n[update] UPDATE REPOSITORY\n[project] NEW PROJECT : ")

    newrepo = "new"
    update = "update"
    proj = "project"
    vi = "view"
    continued_all = True

    while continued_all:

        if link == newrepo:
            driver.get("https://github.com/new")  # New Repo URL
            reposit = input("Enter The New Repository Name : ")  # enter new repo name
            reposit_descrip = input("Enter The Repository Description : ")  # enter repo description
            repo_name = driver.find_element_by_id("repository_name")  # find repo name
            repo_name.send_keys(reposit)  # sending the input for repo name
            repo_description = driver.find_element_by_id("repository_description")  # find repo description
            repo_description.send_keys(reposit_descrip)  # sending the input for repo description
            choice = input("public for Public Option,private for Private Option : ")
            public = "public"  # var storing value
            private = "private"  # var storing value
            if choice == public:
                public_option = driver.find_element_by_id(
                    "repository_visibility_public")  # id of public radio button field
                public_option.click()
            elif choice == private:
                private_option = driver.find_element_by_id(
                    "repository_visibility_private")  # id of private radio button field
                private_option.click()
            statement = True  # var storing value
            none_input = ""  # var storing value
            while statement:  # while loop
                input1 = input("Do You Need README.md ? Type y for YES, if NO leave blank and hit ENTER/RETURN : ")
                if input1.lower() == none_input:  # if statement
                    print("NO README.md")
                else:
                    readme_select = driver.find_element_by_id("repository_auto_init")  # README checkbox id
                    readme_select.click()
                    print("README.md Selected")
                input2 = input("Do you need gitignore ? Type y for YES, if NO leave blank and hit ENTER/RETURN : ")
                if input2.lower() == none_input:
                    print("GITIGNORE not selected")
                else:
                    gitig_select = driver.find_element_by_id(
                        "repository_gitignore_template_toggle")  # GITIGNORE checkbox id
                    gitig_select.click()
                    print("GitIgnore Selected. Select from options on GUI. [WAITING FOR 6 SECONDS]...")
                    sleep(10)
                input3 = input("Do you need License ? Type y for YES, if NO leave blank and hit ENTER/RETURN : ")
                if input3.lower() == none_input:
                    print("LICENSE not selected")
                else:
                    license_select = driver.find_element_by_id(
                        "repository_gitignore_template_toggle")  # LICENSE checkbox id
                    license_select.click()
                    print("LICENSE Selected. Select from options on GUI. [WAITING FOR 6 SECONDS]...")
                    sleep(10)

                statement = False
            driver.find_element_by_xpath("//button[@class='btn btn-primary first-in-line']").click()  # submit field
            # submit = driver.find_element_by_link_text("Create repository")
            # submit.click()
            continued_all = False
        # <--------------------------------------------------------------------------------------------------------------------------------------------->
        elif link == update:
            driver.get("https://github.com/new/import")
            url = input("Enter Clone URL")
            rep = input("Enter Repository Name")
            clone_url = driver.find_element_by_id("vcs_url")
            clone_url.send_keys(url)
            reponame = driver.find_element_by_id("repository_name")
            reponame.send_keys(rep)
            choice = input("Public for Public Option,Private for Private Option : ")
            public1 = "public"
            private1 = "private"
            if choice == public1:
                public_option1 = driver.find_element_by_id("repository_visibility_public")
                public_option1.click()
            if choice == private1:
                private_option1 = driver.find_element_by_id("repository_visibility_private")
                private_option1.click()

            continuation = True
            none_input1 = ""
            cancel = "c"
            imp = "b"
            while continuation:
                bc = input("Type C to cancel , Type B to begin import")
                if bc.lower() == cancel:
                    print("You have cancelled the operation")
                    cancel_imp = driver.find_element_by_xpath("//a[@class='float-right btn btn-invisible']")
                    cancel_imp.send_keys(Keys.RETURN)
                    continuation = False
                elif bc.lower() == imp:
                    import_repo = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
                    import_repo.send_keys(Keys.RETURN)
                    print("[IMPORTING...]")
                    hello = False
                else:
                    continuation = True
            continued_all = False
        # <------------------------------------------------------------------------------------------------------------------------------------------------------------------>

        elif link == proj:
            driver.get("https://github.com/new/project")
            proj_name = input("Enter A Project Name : ")
            proj_des = input("Enter The Project Description : ")
            project = driver.find_element_by_id("project_name")
            project.send_keys(proj_name)
            project_desc = driver.find_element_by_id("project_body")
            project_desc.send_keys(proj_des)
            print(
                "[ bk ] = Basic Kanban \n [ ak ] = Advanced Kanban \n [ akr ] = Advanced Kanban Review \n [ bgt ] = "
                "Bug Triage \n If nothing entered None will be selected")
            template = input("Enter A Template : ")
            basick = "bk"
            advancedk = "ak"
            advancedkr = "akr"
            none = ""
            bugtriage = "bgt"
            if template == basick:
                first_exec = driver.find_element_by_xpath(
                    "//summary[@class='btn select-menu-button text-center flex-auto']")
                first_exec.click()
                basic = driver.find_element_by_xpath("//label[@class='select-menu-item'][2]")
                basic.click()
            elif template == advancedk:
                first_exec = driver.find_element_by_xpath(
                    "//summary[@class='btn select-menu-button text-center flex-auto']")
                first_exec.click()
                advanced = driver.find_element_by_xpath("//label[@class='select-menu-item'][3]")
                advanced.click()
            elif template == advancedkr:
                first_exec = driver.find_element_by_xpath(
                    "//summary[@class='btn select-menu-button text-center flex-auto']")
                first_exec.click()
                advanced_review = driver.find_element_by_xpath("//label[@class='select-menu-item'][4]")
                advanced_review.click()
            elif template == bugtriage:
                first_exec = driver.find_element_by_xpath(
                    "//summary[@class='btn select-menu-button text-center flex-auto']")
                first_exec.click()
                bugt = driver.find_element_by_xpath("//label[@class='select-menu-item'][5]")
                bugt.click()
            elif template == none:
                first_exec = driver.find_element_by_xpath(
                    "//summary[@class='btn select-menu-button text-center flex-auto']")
                first_exec.click()
                none_temp = driver.find_element_by_xpath("//label[@class='select-menu-item'][1]")
                none_temp.click()
            else:
                print("YOUR SUBMISSION WILL BE INVALID")

            pubpriv = input("Enter [public] for Public or [private] for Private")
            public2 = "public"
            private2 = "private"
            character11 = True

            while character11:
                if pubpriv.lower() == public2:
                    public_entry = driver.find_element_by_xpath("//input[@id='project_public_true']")
                    public_entry.click()
                    character11 = False
                elif pubpriv.lower() == private2:
                    private_entry = driver.find_element_by_xpath("//input[@id='project_public_false']")
                    private_entry.click()
                    character11 = False
                else:
                    character11 = True
            html = "https://github.com/{mention}?tab=repositories".format(mention=input("Enter GITHUB username : "))
            # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
            # like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
            counter = 0
            soup = requests.get(html).text
            soup1 = BeautifulSoup(soup, 'lxml')
            for p in soup1.find_all('a', itemprop="name codeRepository"):
                counter += 1
                print(p.text)
            Repo_name = input("Enter Repository Name : ")
            repo_name_send = driver.find_element_by_xpath(
                "//input[@class='form-control auto-search-input input-contrast mr-0 js-project-create-linked-repo-search']")
            repo_name_send.send_keys(Repo_name)
            proceed = driver.find_element_by_xpath(
                "//button[@class='btn btn-primary flex-auto float-none float-md-left']")
            proceed.click()
            continued_all = False
        elif link == vi:
            html1 = "https://github.com/{mention}?tab=repositories".format(mention=input("Enter GITHUB username : "))
            driver.get(html1)
            soup = requests.get(html1).text
            soup1 = BeautifulSoup(soup, 'lxml')
            print("[GETTING REPOSITORY NAMES.....]")
            for p in soup1.find_all('a', itemprop="name codeRepository"):
                print(p.text)

            print("Do You Want To Clone any Repository ? Enter [yes] for heading to the repo. Enter [no] to quit "
                      "the process : ")
            answer = input("Enter your Yes or No : ")

            if answer.lower() == "yes":
                clone_repo = driver.get("https://github.com/et1909/{repo_repo}/archive/master.zip".format(repo_repo=input("Enter Repository Name : ")))
                r = requests.get(clone_repo,stream=True)  # request get means it fetches the url and stream allows the connection
                # to be opened so that the programmer can execute code even after the request is sent.
                z = zipfile.ZipFile(io.BytesIO(r.content))  # zipfile is the module calling ZipFile which opens the zip file in
                # read and write format.
                z.extractall(path="C:\\Program Files)")  # extractall extracts the zip file to the current working
                # directory when the dev has not mentioned the path.
            elif answer.lower() == "no":
                print("QUITING....")
            continued_all = False

        else:
            print("Enter Proper Character : ")


# <---------------------------------GIT COMMIT---------------------------------------------------------->
#
# import subprocess
#
# subprocess.call(['sh', './automate.sh'])
#
# <------------------------------------------------------------------------------------------------------>
login("user.txt", ["User"])
repo()
