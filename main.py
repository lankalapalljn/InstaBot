"""
Developed by Jayanth Lankalapalli 
Last updated 7/20/2020


Program was created to allow a user to enter in their Instagram Username and Password so that the bot created can login to their account and be able to collect a list of all of the
user's followers and also like all the posts of each of their followers.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class InstaBot:
    
    def __init__ (self,username,password): #constructor 
        self.password = password #password is the password entered by the user
        self.username = username #username is the username entered by the user
        self.bot = webdriver.Chrome('./chromedriver') #using chrome web driver

    def login(self): #login method
        bot = self.bot #create a bot driver from the constructor so you can use it to find elements and also load up websites
        bot.get("https://www.instagram.com/") #loads you to the instagram login screeen
        time.sleep(4) #sleep 4 so the page loads and renders

        userEmail = bot.find_element_by_name('username').send_keys(self.username) #enters in your username
        userPass = bot.find_element_by_name('password').send_keys(self.password) #enters in your password
        time.sleep(1)

        bot.find_element_by_name('password').send_keys(Keys.RETURN) #
        time.sleep(3)

    def find_followers(self, num): #find a way to find the number of followers for the account
      
        bot = self.bot
        bot.get("https://www.instagram.com/"+ self.username)
        time.sleep(1)
        
        follcount = bot.find_element_by_css_selector('ul li a')
        tempText = ((follcount.text))
        k = 0
        out = ''
        while(k<len(tempText)):
            if(tempText[k].isdigit()):
                out = out + tempText[k]
                k+=1
            else:
                break
        print("followers i have: " + out)

        bot.find_element_by_css_selector('ul li a').click()
        time.sleep(2)
        follList = bot.find_element_by_class_name('isgrP')
        i = 0
        followerArray = []

        

        while(i<(int(out))): #to make the list of followers scroll down so more of your followers appear to add to an array, can change the 20 to be higher but right now i can get a max of 132 follower into the array
            bot.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', follList)
            time.sleep(.1)
            i += 1 

        followers = bot.find_elements_by_class_name('FPmhX')
        for person in followers:
            if(person not in followerArray):
                followerArray.append(person.text)

        print(followerArray)    
        print(len(followerArray))  
        self.followers = followerArray      

            
            
    

    
        

        
    
    def like_Followers_posts(self):
        bot = self.bot
        f = 0
        while(f < len(self.followers)):
            bot.get("https://www.instagram.com/" + self.followers[f])
            time.sleep(2)
            fincount = bot.find_element_by_class_name("g47SY")
            count = int(fincount.text) #found number of posts on the account
            print(count) #prints number of posts on account
        #add an if statement to only continue with liking if they have at least 1 post
            i = 0
            if(count > 0): #if there is at least 1 post, this is a do while loop 
                bot.find_element_by_class_name("_9AhH0").click() #click on recent post on account
                time.sleep(.5)
                bot.find_element_by_class_name('fr66n').click() #the like button
                time.sleep(.2)
                i+=1 #increment i
            while(i < count): #more than 1 post
                bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click() #next arrow button to go to next post
                time.sleep(.5)
                bot.find_element_by_class_name('fr66n').click()
                time.sleep(.3)
                i+=1
            f+=1
        bot.get("https://www.instagram.com/" + self.username)
           
    



user = input("Enter Instagram username: ") #allows for different users to use the bot, they enter in their username and password
passw = input("Enter Instagram password: ")

igB = InstaBot(user, passw) #generates the bot and it launches
igB.login() #logs on to the account provided
igB.find_followers(5) #creates an array of all the followers that follow the account
igB.like_Followers_posts() #hits the like button on every post for each of the accounts followers

#create a menu of options for user to be able to follow a ton of people, like their friends posts etc.
#NOTES FOR FIXES
# Find a way to identify if the post is already liked (DOUBLE TAP INSTEAD OF HITTING THE LIKE BUTTON)
# Find a way to also creata an array for people following the account
# Add mass commenting on posts
# Add mass DM-ing people on an array list
# Create a while loop menu option(number for user to enter)
#
#
#
#
#
#
#
#
