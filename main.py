
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
通过开发者工具，发现网页的cookie的形式如下，即name=cookie：
Cookie: JSESSIONID=5C3D1B40AF4DE06D9B010BCDCBD110FA
'''#JSESSIONID=C9E4B1DF08217C67B9F69D67EA660AF4
'''
通过selenium打开网页，清除网页保存到本地的cookie，
然后定位到点赞按钮，模拟点击，
循环模拟即可。
'''
urls =['https://faculty.nuist.edu.cn/luojingjia1/zh_CN/index.htm',]#,'https://faculty.nuist.edu.cn/mahongyun/zh_CN/index.htm','https://faculty.nuist.edu.cn/wangxiang1/zh_CN/index.htm',
#'https://faculty.nuist.edu.cn/yanhuiping/zh_CN/index.htm','https://faculty.nuist.edu.cn/xuejiaqing/zh_CN/index.htm','https://faculty.nuist.edu.cn/wukun/zh_CN/index.htm'
#       ,'https://faculty.nuist.edu.cn/pengke/zh_CN/index.htm']

def search():
    try:
        # 待测试网页
        # 打开网页
        driver = webdriver.Chrome()
        for url in urls:
            driver.get(url)

        # 设置等待时间，防止因网速的问题而没有打开网页
            wait = WebDriverWait(driver, 10)

        # 设置循环，自动化点赞
            for i in range(40):
                print('网页初始的cookie:', driver.get_cookies())
                print('\n')
                cookie_name = []

            # 获取网页的cookie,可能有很多个
                cookies = driver.get_cookies()
            # 获取所有的cookie的name
                for cookie in cookies:
                    cookie_name.append(cookie.get('name'))

            # 删除cookie的name 并 打印输出网页的cookie
                for cookie in cookie_name:
                    driver.delete_cookie(name=cookie)

                print('删除cookie:', driver.get_cookies())
                print('\n')

            # 刷新网页
                driver.refresh()

            # 设置睡眠时长，防止系统检测出恶意
                time.sleep(20)

            # 模拟点赞：先定位元素，再模拟点击
                agree = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#_parise_imgobj_u8'))
                )
                agree.click()

            # 打印输出刷新后网页的cookie
                print('刷新网页后的cookie:', driver.get_cookies())
                print('\n')

                print('*'*20)

        driver.close()

    except TimeoutException or WebDriverException:
        # 异常处理，如果出现异常则重新打开网页
        return search()

def main():
    search()

if __name__ == '__main__':
    main()
