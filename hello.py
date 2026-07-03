from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Edgeドライバーの起動（自動で探せるならパス指定不要）
driver = webdriver.Edge()

# Googleにアクセス
driver.get("https://www.google.com")

# ページ読み込み待機（オプション）
time.sleep(10)

# 検索ボックスを取得して「こんにちは」と入力
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("こんにちは")
search_box.send_keys(Keys.RETURN)

# 結果表示を少し待つ（任意）
# time.sleep(5)
# driver.
