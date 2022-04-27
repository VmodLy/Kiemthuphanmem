from selenium.webdriver.common.by import By



class MainPageLocators(object):
    LOGO = (By.ID, 'lzd-logo-content')
    SEARCH = (By.XPATH, "//input[@id='q']")
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
  






