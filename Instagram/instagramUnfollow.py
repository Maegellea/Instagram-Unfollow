
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from userInformation import username, password



class Insta:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = ""
        self.following = ""
        self.nonFollowers = []
        self.driver = webdriver.Firefox()


    def signIn(self):
        url = "https://www.instagram.com"
        self.driver.get(url)
        sleep(2.5)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.username)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        sleep(4)
        self.driver.get("https://www.instagram.com/{}/".format(self.username))
        sleep(2)
        self.getFollowers()

    def getFollowers(self):
        action = webdriver.ActionChains(self.driver)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[2]/ul').click()

        while True:
            count1 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/ul/div").find_elements(By.TAG_NAME,"li"))
            action.key_down(Keys.END).key_up(Keys.END).perform()
            sleep(0.75)
            count2 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/ul/div").find_elements(By.TAG_NAME,"li"))

            if count1 == count2:
                sleep(1)
                count1 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/ul/div").find_elements(By.TAG_NAME,"li"))
                action.key_down(Keys.END).key_up(Keys.END).perform()
                sleep(1)
                count2 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/ul/div").find_elements(By.TAG_NAME,"li"))
                if count1 == count2:
                    break

        li = self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/ul/div").find_elements(By.TAG_NAME,"li")

        for element in li:
            followers = element.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            self.followers += followers[25:]
        
        self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[1]/div/div[2]/button").click()
        sleep(1)

        self.followers = self.followers.strip("/")
        self.followersList = self.followers.split("//")
        self.getFollowing()
    
    
    def getFollowing(self):
        action = webdriver.ActionChains(self.driver)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/ul').click()

        while True:
            count1 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/ul/div").find_elements(By.TAG_NAME,"li"))
            action.key_down(Keys.END).key_up(Keys.END).perform()
            sleep(0.75)
            count2 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/ul/div").find_elements(By.TAG_NAME,"li"))

            if count1 == count2:
                sleep(2)
                count1 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/ul/div").find_elements(By.TAG_NAME,"li"))
                action.key_down(Keys.END).key_up(Keys.END).perform()
                sleep(1)
                count2 = len(self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/ul/div").find_elements(By.TAG_NAME,"li"))
                if count1 == count2:
                    break

        li = self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/ul/div").find_elements(By.TAG_NAME,"li")

        for element in li:
            following = element.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            self.following += following[25:]

        self.following = self.following.strip("/")
        self.followingList = self.following.split("//")
        self.compare()

    def compare(self):
        following = self.followingList
        followers = self.followersList 

        for user in following:
            if user not in followers:
                self.nonFollowers.append(user)


user = Insta(username,password)

user.signIn()

print(user.nonFollowers)
print(f"{len(user.nonFollowers)} person is not following you")


