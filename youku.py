# coding=utf-8

from selenium import webdriver
import os,time,random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 引入 chromedriver 浏览器驱动
chromedriver = "/usr/local/bin/81_0_4044_138"
os.environ["webdriver.chrome.driver"] = chromedriver

# 实例化浏览器
browser = webdriver.Chrome(chromedriver)

# 设置浏览器需要打开的 url
url = "https://www.youku.com/"
# 打开url 
browser.get(url)


# timeout = WebDriverWait(browser, 10)
# uerCenter = browser.find_element_by_id("uerCenter")


# 鼠标操作 demo
# u_record=browser.find_element_by_xpath('//*[@id="uerCenter"]/div[2]/div/div[1]/a')
# ActionChains(browser).move_to_element(u_record).perform()


browser.find_element_by_xpath('//*[@id="uerCenter"]/div[6]/div[1]/div/div/div/div[5]/button').click()
tel = input('请输入手机号码: ')



# 进入登录iframe
browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="alibaba-login-box"]'))
# 输入手机
browser.find_element_by_xpath('//*[@id="fm-sms-login-id"]').send_keys(tel)

time.sleep(1)
# 点击获取验证码
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/div[3]/a').click()
try:
    huakuai = browser.find_element_by_xpath('//*[@id="nc_1_n1z"]')
    print("找到滑块元素")
except:
    print("没有找到滑块元素")
    pass
else:
    action = ActionChains(browser)
    # time.sleep(1)
    action.click_and_hold(huakuai).perform()#循环的次数自己控制

    for index in range(10):
        print("index:%d" %index)
        try:
            action.move_by_offset(10, 0).perform()  # 平行移动鼠标
            browser.save_screenshot('login-screeshot-i-' + str(index) + '.png')
        except Exception as e:
            print(e)
            break
        if (index == 17):
            action.release()
            # time.sleep(1)
            # browser.save_screenshot('login-screeshot-i-' + str(index) + '.png')
        # else:
            # sleeptime = random.randint(0,2)
            # print("延迟%d秒" %sleeptime)
            # time.sleep(sleeptime)
print("滑块移动完成")
yzm = input('请输入验证码: ')

browser.find_element_by_xpath('//*[@id="fm-smscode"]').send_keys(yzm)

# 登录
browser.find_element_by_xpath('//*[@id="login-form"]/div[7]/button').click()





# 关闭浏览器
# browser.quit()