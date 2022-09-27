from selenium.webdriver.common.by import By
from crawler import driver


def get_abstract(browser):
    res_list = browser.find_elements(by=By.CSS_SELECTOR, value="[class='item abstract']")
    result = browser.execute_script("return arguments[0].textContent", res_list[0])
    # 删除 result 中的前缀
    return result[20:]


if __name__ == '__main__':
    url = 'https://ojs.aaai.org/index.php/AAAI/article/view/4686'
    print(get_abstract(driver.init_driver(url)))