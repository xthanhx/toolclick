from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import random

from environs import Env
env = Env()
env.read_env()

class toolClick:
    
    data_default = {}
    scr_pos = 0
    ord = 0
    scripts = {}
    st_script = True
    time = time
    browser_window_position = {}
    
    def __init__(self, url = 'https://blog.xes.vn'):
        self.setUp(url)
        
        
    def setUp( self, url):
        self.setup_driver(url)
        self.setup_win_size()                           
        self.setup_win_act_area()
        self.setup_scrolling_distance()
        
         
    def setup_driver(self, url):
        options = Options()
        options.add_argument("--start-maximized")
        os = env.str("OS")
        
        switcher={
                'mac':'chrome-mac',
                'win':'chrome-win',
                'linux':'chrome-linux'
        }
        
        path =  './' + switcher.get(os,"Invalid day of week") + '/chromedriver'
        
        driver = webdriver.Chrome( path ,options=options)
        driver.get(url)
        self.driver = driver
    
    
    def setup_win_size(self):
        self.data_default['win_size'] = self.driver.execute_script('return { height : window.innerHeight, width: window.innerWidth };')
        
        
    def setup_win_act_area(self):
        book_mark_height = 32
        top_bar_height = 72
        total_nav_top_height = top_bar_height + book_mark_height
        browser_window_position = self.driver.get_window_position()
        win_size = self.data_default['win_size']
        
        win_act_area =  {
                            'x':    {  
                                        'start' : browser_window_position['x'],
                                        'end' : browser_window_position['x'] + win_size['width'] 
                                    },
                            
                            'y':    {  
                                        'start' : browser_window_position['y'] + total_nav_top_height,
                                        'end' : browser_window_position['y'] + win_size['width'] 
                                    }
                        }
        
        self.browser_window_position = browser_window_position
        self.data_default['win_act_area'] = win_act_area
    
    
    def setup_scrolling_distance(self):
        win_size = self.data_default['win_size']
        self.move_mouse( win_size['width']/2, win_size['height']/2, 1)
        time.sleep(1)
        pyautogui.scroll(-1)
        time.sleep(1)
        scrolling_distance = self.driver.execute_script('return document.getElementsByTagName("body")[0].scrollTop;')
        self.data_default['scrolling_distance'] = scrolling_distance
    
    
    def get_elements(self, element = ''):
        elements = self.driver.find_elements_by_css_selector(element)
        return elements
    
############################################################ execute ############################################################

    def get_scr_position(self):
        top = self.scr_pos
        end = self.scr_pos + self.data_default['win_size']['height']
        return  {
                    'top' : top,
                    'end' : end
                }
    
    def move_mouse( self, x, y, s = 1):    
        area = self.data_default['win_act_area']

        coor_x = area['x']['start'] + x
        coor_y = area['y']['start'] + y
        
        coor_start_x = area['x']['start']
        coor_start_y = area['y']['start']
        
        coor_end_x = area['x']['end']
        coor_end_y = area['y']['end']
        print('coor_end_y') 
        print(coor_end_y)
        
        print('coor_x') 
        print(coor_x)
        
        print('coor_y') 
        print(coor_y)
        
        print('coor_y') 
        print(coor_y)
            
        if coor_x > coor_end_x - 10:
            coor_x = coor_end_x - 10
        elif coor_x < coor_start_x + 10:
            coor_x = coor_start_x + 10
            
        if coor_y > coor_end_y - 10:
            coor_y = coor_end_y - 10
        elif coor_y < coor_start_y + 10:
            coor_y = coor_start_y + 10
            
        pyautogui.moveTo(coor_x, coor_y, s)
    
    def scrolling( self, distance = 0):
        self.scr_pos += distance
        times = abs(distance)
        if distance<0:
            stt = 1
        else:
            stt = -1
        i = 0
        
        while i < times:
            pyautogui.scroll(stt)
            time.sleep(0.01)
            i += 1
            
    def rand_scr( self, distance = 0):
        self.scr_pos += distance
        times = abs(distance)
        if distance<0:
            stt = 1
        else:
            stt = -1
        e = 0
        while e < times:
            i = 0
            rand_dist = random.randint(5,15)
            e += rand_dist
            
            if e >= times:
                rand_dist = times - (e - rand_dist)
                
            while i < rand_dist:
                pyautogui.scroll(stt)
                time.sleep(0.01)
                i += 1
            self.rand_move_mouse()
        
    def rand_move_mouse( self ):
        area = self.data_default['win_size']
        
        xx = area['width']  - 50
        yy = area['height'] - 50
        
        times = random.randint(2,5)
        i = 0
        
        while i < times:
            x = random.randint( 0, xx)
            y = random.randint( 0, yy)
            print(x,y)
            self.move_mouse( x, y)
            i +=1
    
    def hard_scrolling(self, distance):
        pyautogui.scroll(distance)
        
    def scrolling_down_up( self, times ):
        i = 0
        e = 0
        while i < times:
            i_c = 0
            while i_c < 5:
                pyautogui.scroll(-1)
                time.sleep(0.01)
                i_c += 1
            time.sleep(1)
            i += 1

        time.sleep(2)

        while e < times:
            e_c = 0
            while e_c < 5:
                pyautogui.scroll(1)
                time.sleep(0.01)
                e_c += 1
            time.sleep(1)
            e += 1
    
    
    def sleep(self, s = 1):
        time.sleep(s)
    
    
    def move_click(self, x, y, s = 1):
        self.move_mouse(x, y, s)
        pyautogui.click()

        
    def get_position(self, element, position = 0):
        local = element.location
        size = element.size
        
        position =   {
                    'x' : local['x'] + size['width']/2,
                    'y' : local['y'] + size['height']/2
                }
        return position
    
    
    def cacul_position(self, element_position):
        screen_position = self.get_scr_position()
        
        x = element_position['x']
        y = element_position['y'] - screen_position['end']
        
        position =  {
                        'x' : x,
                        'y' : y
                    }
        return position
        
    def close_browser(self):
        brw_pos = self.browser_window_position
        win_size = self.data_default['win_size']
        x = brw_pos['x'] + win_size['width'] - 15
        y = brw_pos['y'] + 15
        pyautogui.moveTo(x,y,1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.press('space') 
        
    