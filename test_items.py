import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_can_see_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"),"The 'Add to basket' button was not found"
