from toolClick import toolClick
import webbrowser

url = 'https://blog.xes.vn'

tool = toolClick(url)
class_element_1 = '.section-post-slider .post-slider-additional-content .tw-flex img'
element_1 = tool.get_elements(class_element_1)[0]
position_1 = tool.get_position(element_1)

tool.driver.find_element_by_css_selector(class_element_1).click()

class_element_2 = '.tw-block.hover_tw-no-underline.tw-bg-surface.tw-p-8'

height_page = tool.driver.execute_script('return document.getElementsByTagName("body")[0].scrollHeight')

tool.scrolling(height_page/tool.data_default['scrolling_distance'])

height_page = tool.driver.execute_script('return document.getElementsByTagName("body")[0].scrollHeight')

element_2 = tool.get_elements(class_element_2)[0]
position_2 = tool.get_position(element_2)

win_act_area_y = tool.data_default['win_act_area']['y']

total_height_page = height_page + win_act_area_y['end'] - win_act_area_y['start']

position_scrolling_up = int(((win_act_area_y['end'] - win_act_area_y['start'])/3 - position_2['y'] )/ tool.data_default['scrolling_distance'])

tool.scrolling(-1*position_scrolling_up)

element_2 = tool.get_elements(class_element_2)[0]
position_2 = tool.get_position(element_2)

tool.move_click( position_2['x'], position_2['y'], 1)

tool.time.sleep(1)
tool.driver.close()

# # ==========================================================================================================================================================

i = 0
while i < 100:
    webbrowser.get("firefox").open(url)

    tool.time.sleep(2)
    tool.move_click( position_1['x'], position_1['y']+32)
    tool.time.sleep(2)
    e = 0
    while e < 20:
        tool.rand_scr(200)
        tool.hard_scrolling(-100)
        tool.scrolling(-1*position_scrolling_up)
        tool.move_click( position_2['x'], position_2['y']+100, 1)
        e+=1
    
    tool.close_browser()
    i=+1