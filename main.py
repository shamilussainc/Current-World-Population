from selenium import webdriver
import time

# create webdriver object
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.worldometers.info/world-population/")
driver.implicitly_wait(10)

end_time = time.time()+30  # seconds
while time.time() <= end_time:
    # scraping values from site
    current_world_population = driver.find_element_by_xpath('//*[@id="maincounter-wrap"]/div/span').text
    # today
    births_today = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div[2]/span').text
    deaths_today = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[3]/div[2]/span').text
    population_growth_today = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[4]/div[2]/span').text
    # This year
    births_this_year = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/span').text
    deaths_this_year = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[3]/div[2]/span').text
    population_growth_this_year = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[4]/div[2]/span').text

    # print current time
    print('###################################################################################')
    print('Current Time : '+time.ctime())
    print('----------------------------------------------------------------------------------')
    # Print Values to console
    print('Current World Population = ' + current_world_population)
    print('Today -> Births = '+births_today+', Deaths = '+deaths_today+', Population Growth = '+population_growth_today)
    print('This year -> Births = '+births_this_year+', Deaths = '+deaths_this_year+', Population Growth = '+population_growth_this_year)
