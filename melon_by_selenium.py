from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 웹드라이버 설정 및 초기화
driver = webdriver.Chrome(ChromeDriverManager().install())

# 데이터 수집용 변수 초기화
dict = {}
number = 100
melonList = []

# 멜론 메인 페이지로 이동
try:
    driver.get('https://www.melon.com/index.htm')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.menu_bg.menu01')))
except TimeoutException:
    print("메인 페이지 로딩이 오래 걸립니다!")
    driver.quit()

# 차트 페이지로 이동
try:
    driver.find_element_by_css_selector('.menu_bg.menu01').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.menu_chart.m2')))
    driver.find_element_by_css_selector('.menu_chart.m2').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'GN0100')))
    driver.find_element_by_id('GN0100').click()
except TimeoutException:
    print("차트 로딩이 오래 걸립니다!")
    driver.quit()

for i in range(0, number):
    temp = []
    try:
        # 곡 상세 정보 클릭
        more_info_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.btn_button_icons.type03.song_info'))
        )
        more_info_list[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.song_name')))
    except TimeoutException:
        print(f"노래 {i+1}의 상세 정보를 로딩하는 데 오래 걸립니다!")
        driver.quit()

    try:
        # 곡 정보 추출
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
    except TimeoutException:
        print(f"노래 {i+1}의 정보를 추출하는 데 오래 걸립니다!")
        driver.quit()

    try:
        # 메인 페이지로 돌아가기
        driver.get('https://www.melon.com/index.htm')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.menu_bg.menu01')))
        driver.find_element_by_css_selector('.menu_bg.menu01').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.menu_chart.m2')))
        driver.find_element_by_css_selector('.menu_chart.m2').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'GN0100')))
        driver.find_element_by_id('GN0100').click()
    except TimeoutException:
        print("메인 페이지로 돌아가는 데 오래 걸립니다!")
        driver.quit()

# 결과 출력
print(melonList)

# 웹드라이버 종료
driver.quit()
