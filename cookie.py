from selenium import webdriver
from datetime import datetime

path = r'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

current_date = datetime.now()
current_time = current_date.strftime("%H:%M:%S")
current_time_list = current_time.split(":")
current_time_in_seconds = int(current_time_list[0]) * 3600 + int(current_time_list[1]) * 60 + int(current_time_list[2])


play_game = True
while play_game:

    cookie = driver.find_element_by_id('cookie')
    money_object = driver.find_element_by_id('money')
    money = int(money_object.text)

    buy_cursor = driver.find_element_by_id('buyCursor')
    buy_cursor_price = int(buy_cursor.text.strip().split()[2])
    buy_grandma = driver.find_element_by_id('buyGrandma')
    buy_grandma_price = int(buy_grandma.text.strip().split()[2])
    buy_factory = driver.find_element_by_id('buyFactory')
    buy_factory_price = int(buy_factory.text.strip().split()[2])
    buy_mine = driver.find_element_by_id('buyMine')
    buy_mine_price = 2000
    buy_shipment = driver.find_element_by_id('buyShipment')
    buy_shipment_price = 7000
    buy_alchemy = driver.find_element_by_id('buyAlchemy lab')
    buy_alchemy_price = 50000
    buy_portal = driver.find_element_by_id('buyPortal')
    buy_portal_price = 1000000
    time_machine = driver.find_element_by_id('buyTime machine')
    time_machine_price = 123456789


    def check_money(amount, item_price):
        if amount >= item_price:
            return True


    def click_item(item):
        item.click()


    def clicker_run():
        if check_money(money, time_machine_price):
            click_item(time_machine)
        elif check_money(money, buy_portal_price):
            click_item(buy_portal)
        elif check_money(money, buy_alchemy_price):
            click_item(buy_alchemy)
        elif check_money(money, buy_shipment_price):
            click_item(buy_shipment)
        elif check_money(money, buy_mine_price):
            click_item(buy_mine)
        elif check_money(money, buy_factory_price):
            click_item(buy_factory)
        elif check_money(money, buy_grandma_price):
            click_item(buy_grandma)
        elif check_money(money, buy_cursor_price):
            click_item(buy_cursor)

    def check_time_elapsed():
        global current_time_in_seconds
        elapsed_date = datetime.now()
        elapsed_time = elapsed_date.strftime("%H:%M:%S")
        elapsed_time_list = elapsed_time.split(":")
        elapsed_time_in_seconds = int(elapsed_time_list[0]) * 3600 + int(elapsed_time_list[1]) * 60 + int(
            elapsed_time_list[2])
        if elapsed_time_in_seconds - current_time_in_seconds == 5:
            current_time_in_seconds = elapsed_time_in_seconds
            return True


    click_item(cookie)
    if check_time_elapsed():
        clicker_run()

    if money >= 200:
        play_game = False

driver.close()
