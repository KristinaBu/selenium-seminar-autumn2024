from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'li.js-show-search > a')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'li.js-search-input input[name="query"]')
    FOUND_NAME = (By.CSS_SELECTOR, 'p.realname .accent')
    FOUND_LAST_NAME = (By.XPATH, "//p[@class='realname']/span[2]/span/span[@class='accent']")
    SCHEDULE_BUTTON = (By.CSS_SELECTOR, 'li.technopark__menu__item_162 > a')
    SEMESTER_BUTTON = (By.CSS_SELECTOR, 'li.intervalItem[intervalid="semester"] > a')
    CALENDAR_TABLE = (By.CSS_SELECTOR, "table.calendar-month")
    SCHEDULE_ITEM = (By.CSS_SELECTOR, 'tr.schedule-timetable__item.lessonItem')
    SCHEDULE_ITEM_DATE = (By.CSS_SELECTOR, 'td.schedule-timetable__item__date strong')
    SCHEDULE_ITEM_ROOM = (By.CSS_SELECTOR, 'span.schedule-auditorium')
    SCHEDULE_ITEM_ID = (By.ID, 'schedule_item_1729544400')
    AUTH_HEADER_BUTTON = (By.CLASS_NAME, 'gtm-auth-header-btn')
    SIGNUP_MODAL_LINK = (By.CLASS_NAME, 'gtm-signup-modal-link')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'gtm-login-btn')

class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass
