
"""
Created on Thu Dec 13 13:36:40 2018

@author: sidar
"""
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

#creating folder (/gif) in location. All files will be downloaded to this path
def downlaodLocation() :
    
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : final_directory}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


def resize():        
    
    try:
    	#open browser and redirict to ezgif.com 
        allFiles= os.listdir()
       # allFiles=['gif', 'graph_cocaine_hr_1999.png', 'graph_cocaine_hr_2000.png', 'graph_cocaine_hr_2001.png', 'graph_cocaine_hr_2002.png', 'graph_cocaine_hr_2003.png', 'graph_cocaine_hr_2004.png', 'graph_cocaine_hr_2005.png', 'graph_cocaine_hr_2006.png', 'graph_cocaine_hr_2007.png', 'graph_cocaine_hr_2008.png', 'graph_cocaine_hr_2009.png', 'graph_cocaine_hr_2010.png', 'graph_cocaine_hr_2011.png', 'graph_cocaine_hr_2012.png', 'graph_cocaine_hr_2013.png', 'graph_cocaine_hr_2014.png', 'graph_cocaine_hr_2015.png', 'graph_cocaine_hr_2016.png']
        allFiles.remove('gif')
        for i in allFiles:
            #click on resize
            driver.find_element_by_xpath("//*[@class='resize']").click()
            #upload image 
            driver.find_element_by_id('new-image').send_keys(os.getcwd()+"/"+i)
            
            driver.find_element_by_xpath("//*[@type='submit']").click()
            # click on optimize
            driver.find_element_by_xpath("//*[@title='Compress image']").click()
            
            driver.find_element_by_xpath("//*[@type='submit']").click()
            time.sleep(5)
            #Save the image
            driver.find_element_by_xpath("//div[@id='output']//a[@class='save']").click()
            time.sleep(7)
            #rename image to proper name
            old_file = os.path.join(final_directory, "ezgif.com-gif-maker.png")
            new_file = os.path.join(final_directory, i)
            os.rename(old_file, new_file)
    except NoSuchElementException:
        print("Error: Element not found")
		
def gif():
    
    try:
        
        allFiles= os.listdir()
        allFiles.remove('gif')
        allFilesPath=""     
        for i in allFiles:
            allFilesPath+= final_directory+'\\'+i+'\n'
        
        allFilesPath= allFilesPath[:-1]
       #click on gif maker
        driver.find_element_by_xpath("//*[@class='gifmaker']").click()       
       # driver.find_element_by_name('files[]').send_keys(final_directory+"\graph_cocaine_hr_1999.png \n"+final_directory+"/graph_cocaine_hr_2000.png \n "+final_directory+"/graph_cocaine_hr_2001.png");
        # upload all resized files to make gif
        driver.find_element_by_name('files[]').send_keys(allFilesPath);
        driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(15)
        #give delay of 40
        driver.find_element_by_id("delay").send_keys(Keys.CONTROL, "a"); 
        driver.find_element_by_id("delay").send_keys('40')   
        #set loop count as 2
        driver.find_element_by_id("loop").send_keys('2')   
        #choose fader and set fader-delay to 2
        driver.find_element_by_xpath("//*[@name='fader']").click()
        driver.find_element_by_id("fader-delay").send_keys(Keys.CONTROL, "a"); 
        driver.find_element_by_id("fader-delay").send_keys('2')   
        #Set fade-frame to 10
        driver.find_element_by_id("fader-frames").send_keys(Keys.CONTROL, "a"); 
        driver.find_element_by_id("fader-frames").send_keys('10')   
        #Make the gif   
        driver.find_element_by_xpath("//*[@name='make-a-gif']").click()
        time.sleep(60)
        #click on Optimize 
        driver.find_element_by_xpath("//*[@title='Compress image']").click()
        #Set lossy to 200
        driver.find_element_by_id("lossy").send_keys(Keys.CONTROL, "a"); 
        driver.find_element_by_id("lossy").send_keys('200')   
        #Click on optimize Gif
        driver.find_element_by_xpath("//*[@name='optimize']").click()
        time.sleep(60)   
        #savethe gif
        driver.find_element_by_xpath("//div[@id='output']//a[@class='save']").click()
        time.sleep(5)
        #Rename gif to specified name 
        old_file = os.path.join(final_directory, "ezgif.com-optimize.gif")
        new_file = os.path.join(final_directory,gifName)
        time.sleep(10)
        os.rename(old_file, new_file)
    
    except NoSuchElementException:
        print("Error: Element not found")

#setting current directory to location of folder  
#os.chdir("C:/Users/sidar/Box/CDC Maps/Visuals/cocaine_br")
os.chdir("C:/Users/floza/Desktop/Kosali Projects/SG_Add Files/Maps/MustAccess")
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'gif')
gifName= "MA_GIF.gif"

os.listdir()

driver = downlaodLocation()
driver.get('https://ezgif.com')
#resize()
gif()
driver.close()
print("finished")
