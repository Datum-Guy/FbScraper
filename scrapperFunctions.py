from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class scrapperFunctions:
    def MoveToElement(self, elem,element = None):
        if(element == None):
            element = self.driver
        action = webdriver.common.action_chains.ActionChains(element)
        action.move_to_element(elem)
        # element.click()
        action.perform()

    def ScrollToElement(self, elem,element = None):
        if(element == None):
            element = self.driver
        x = elem.location['x']
        y = elem.location['y'] - 100

        element.execute_script("window.scrollTo("+str(x)+","+str(y)+");")

    def find_elem_by_id_with_wait(self, elem_id, element=None, timeout=10):
        if(element == None):
            element = self.driver
        try:
            elem = WebDriverWait(element, timeout).until(
                lambda x: x.find_element_by_id(elem_id))
            return elem
        except:
            return None

    def find_elem_by_link_text_with_wait(self, elem_id, element=None, timeout=10):
        if(element == None):
            element = self.driver
        try:
            elem = WebDriverWait(element, timeout).until(
                lambda x: x.find_element_by_link_text(elem_id))
            return elem
        except:
            return None

    def find_elem_by_id(self, elem_id, element=None):
        if(element == None):
            element = self.driver
        try:
            elem = element.find_element_by_id(elem_id)
            return elem
        except:
            return None

    def find_elem_by_name(self, elem_name, element=None):
        if(element == None):
            element = self.driver
        try:
            elem = element.find_element_by_name(elem_name)
            return elem
        except:
            return None

    def find_elem_by_class_name_with_wait(self, class_name, element=None, timeout=10):
        if(element == None):
            element = self.driver
        try:
            elem = WebDriverWait(element, timeout).until(
                lambda x: x.find_element_by_class_name(class_name))
            return elem
        except:
            return None

    def find_elems_by_class_name_with_wait(self, class_name, element=None, timeout=10):
        if(element == None):
            element = self.driver
        try:
            elems = WebDriverWait(element, timeout).until(
                lambda x: x.find_elements_by_class_name(class_name))
            return elems
        except:
            return []

    def find_elem_by_class_name(self, class_name, element=None):
        if(element == None):
            element = self.driver
        try:
            elem = element.find_element_by_class_name(class_name)
            return elem
        except:
            return None
    
    def find_elems_by_class_name(self, class_name, element=None):
        if(element == None):
            element = self.driver
        try:
            elems = element.find_elements_by_class_name(class_name)
            return elems
        except:
            return []

    def find_elems_by_id(self, id, element=None):
        if(element == None):
            element = self.driver
        try:
            elems = element.find_elements_by_id(id)
            return elems
        except:
            return []

    def generate_user_id(self, N):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    def infinite_scroll(self):
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return window.scrollY")

        y_idx = 100

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, "+str(y_idx)+");")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            y_idx = y_idx + 200

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return window.scrollY")
            if new_height == last_height:
                break
            last_height = new_height
