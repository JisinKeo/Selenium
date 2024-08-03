import pandas as pd # 데이터 처리를 위한 라이브러리
import time
from tqdm.notebook import tqdm
from selenium import webdriver # 웹 페이지를 자동으로 제어하기 위한 라이브러리
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

dict = {}
number = 100
melonList = []

for i in range(0, number):
    temp = []
    more_info_list = driver.find_elements_by_css_selector('.btn_button_icons.type03.song_info')
    more_info_list[i].click()
    time.sleep(2)

    songName = driver.find_element_by_css_selector('.song_name')
    temp.append(songName.text)
    artistName = driver.find_element_by_css_selector('.artist_name')
    temp.append(artistName.text)

    meta_info = driver.find_element_by_css_selector('.list').text.split('\n')
    temp.append(meta_info[1])
    temp.append(meta_info[3])
    temp.append(meta_info[5])
    temp.append(meta_info[7])
  
    like_count = driver.find_element_by_id('d_like_count')
    temp.append(like_count.text)
    melonList.append(temp)

    driver.get('https://www.melon.com/index.htm')
    time.sleep(2)
    driver.find_element_by_css_selector('.menu_bg.menu01').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.menu_chart.m2').click()
    time.sleep(1)
    driver.find_element_by_id('GN0100').click()

