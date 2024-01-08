from automation.find_date_by_day import find_date_by_day
from automation.time_ranges import Ranges
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os




class  todoist(webdriver.Chrome):
    def __init__(self,
                 username : str ,
                 password : str,
                 parent_task_name : str ,
                 find_date = find_date_by_day,
                 driver_path=r"C:\SeleniumDrivers"
                 ):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(todoist, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()
        self.username = username
        self.password = password
        self.parent_task_name = parent_task_name
        self.find_date = find_date
    def go_to_first_page(self):
        
        self.get("https://app.todoist.com")
        time.sleep(2)    
    def login(self):
        username_input =  self.find_element(By.CSS_SELECTOR, 'input[id="element-0"]')
        username_input.send_keys(self.username)
        time.sleep(2)    
        password_input = self.find_element(By.CSS_SELECTOR, 'input[id="element-3"]')
        password_input.send_keys(self.password)
        time.sleep(2)    
        login = self.find_element(By.CSS_SELECTOR,'button[data-gtm-id="start-email-login"]')
        login.click()
        time.sleep(2)    
        
    def Add_project(self):
        
        add_project = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Add project"]')
        add_project.click()
        time.sleep(2)    
        project = self.find_element(By.CSS_SELECTOR, 'input[id="edit_project_modal_field_name"]')
        project.send_keys(self.parent_task_name)
        time.sleep(2)    
        save = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        save.click()
        time.sleep(2)    
        
    def go_to_upcoming_section(self):
        
        self.get("https://app.todoist.com/app/upcoming")
        time.sleep(2)    
        
    def adding_sub_task(self, child_task_name : str):
        
        buttons = self.find_elements(By.CSS_SELECTOR, 'button[data-add-task-navigation-element="true"]')
        
        button_1 = buttons[0]
        button_1.click()
        time.sleep(2)    

        task_name = self.find_element(By.CSS_SELECTOR, 'p[data-placeholder="Task name"]')
        task_name.send_keys(child_task_name)
        
        time.sleep(2)    
    
    def adding_time(self, sub_task_time):
        
        date = self.find_element(By.CSS_SELECTOR, 'div[class="vq8EYsI _2a3b75a1 _509a57b4 e5a9206f _50ba6b6b"]')
        date.click()
        
        time.sleep(2)    
        
        subtask_time = self.find_element(By.CSS_SELECTOR, 'button[class="nKhVnNg _8313bd46 f169a390 _5e45d59f _2a3b75a1 _56a651f6"]')
        subtask_time.click()
        time.sleep(2)    
        
        input_time = self.find_element(By.CSS_SELECTOR, 'input[aria-label="Start time"]')
        input_time.send_keys(sub_task_time)   
        time.sleep(2)    
        
        submit = self.find_element(By.CSS_SELECTOR, 'button[class="_8313bd46 _7a4dbd5f _5e45d59f _2a3b75a1 _56a651f6"]')     
        submit.click()
        time.sleep(2)    
        
    def Adding_date(self, day):
        
        date = self.find_date(day)
        date_web = self.find_element(By.CSS_SELECTOR, f'button[aria-label="{date}"]')
        date_web.click()
        time.sleep(2)    
        
    def insert_child_task_to_parent_task(self):
        inbox = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Select a project"]')
        inbox.click()
        time.sleep(2)    
        
        insertion = self.find_element(By.CSS_SELECTOR, f'li[aria-label="{self.parent_task_name}"]')
        insertion.click()
        time.sleep(2)    
        
    def end(self):
        end = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Add task"]')
        end.click()
        time.sleep(2)    
        
        
        

        
        
        
        

        

