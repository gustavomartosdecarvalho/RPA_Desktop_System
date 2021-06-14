import pyautogui
import os


class GuiHandling:

    def check_element_in_limit_win(self, list_win_pos, pos_x, pos_y):
        if pos_x >= list_win_pos[0]:
            if pos_y >= list_win_pos[1]:
                if pos_x <= (list_win_pos[2] + list_win_pos[0]):
                    if pos_y <= (list_win_pos[3] + list_win_pos[1]):
                        return True
        return False

    def run_app(self, path_app):
        try:
            os.startfile(path_app)
            return True
        except Exception as e:
            print(" - Error opening system: ", e)
            return False

    def limit_win(self):
        try:
            fw = pyautogui.getActiveWindow()
            list_pos = [fw.left, fw.top, fw.width, fw. height]
            return list_pos
        except Exception as e:
            print(" - Error returning system position: ", e)
            return None

    def verify_active_window(self, title_expected):
        try:
            title_active = pyautogui.getActiveWindow().title_active
            if str(title_active) == str(title_expected):
                return True
            else:
                return False
        except Exception as e:
            print(" - Error returning active title: ", e)
            return False

    def left_mouse_click_relative(self, pos_x_rel, pos_y_rel):
        try:
            list_win_pos = self.limit_win()
            if list_win_pos is not None:
                pos_x_abslt = int(list_win_pos[0]) + int(pos_x_rel)
                pos_y_abslt = int(list_win_pos[1]) + int(pos_y_rel)
                if self.check_element_in_limit_win(list_win_pos, pos_x_abslt, pos_y_abslt):
                    pyautogui.click(pos_x_abslt, pos_y_abslt)
                    return True
                return False
        except Exception as e:
            print(" - Error when clicking with the left mouse button : ", e)
            return False

    def press_tab_key(self):
        try:
            pyautogui.press('tab')
            return True
        except Exception as e:
            print(" - Error pressing tab key : ", e)
            return False

    def press_enter_key(self):
        try:
            pyautogui.press('enter')
            return True
        except Exception as e:
            print(" - Error pressing enter key : ", e)
            return False

    def write_text(self, text):
        try:
            pyautogui.write(text)
            return True
        except Exception as e:
            print(" - Error pressing enter key : ", e)
            return False

    def take_screenshot_window(self, path_screenshot):
        try:
            pyautogui.screenshot(path_screenshot)
        except Exception as e:
            print(" - Error taking screenshot : ", e)
            return False

    def close_app(self, name_app):
        try:
            #change to file exe
            os.system('TASKKILL /F /IM ' + name_app)
            return True
        except Exception as e:
            print(" - Error closing system : ", e)
            return False
        


