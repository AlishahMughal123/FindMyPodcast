from selenium import webdriver

url = 'https://www.youtube.com/channel/UCDjjA0esbXFSO8vZ4WkHblQ'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
