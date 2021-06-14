from src.gui_handling import GuiHandling
from src.email_service import EmailService

import time

class MainService:
    def __init__(self):
        # > Declare classes
        self.gui_handling = GuiHandling()
        self.email_service = EmailService()

    # >
    # > Main Method
    # >
    def start_execution(self): 
        if not self.open_system():
            return False
        if not self.fill_form():
            return False
        if self.analysis_response():
            if not self.send_evidences():
                return False
        if not self.close_app():
            return False
        # > If everthing is ok return true
        return True

    # >
    # > Rules Methods
    # >
    def open_system(self): 
        print(" - Open the system")
        self.gui_handling.run_app("PUT path_app")
        time.sleep(1)
        return True

    def fill_form(self):
        # > Verify the active window
        if not self.gui_handling.verify_active_window('PUT title_expected'):
            return False
        # > Set initial System 
        if not self.gui_handling.write_text('AF_LIB'):
            return False
        # > Press Tab button
        if not self.gui_handling.press_tab_key():
            return False
        # > Set Number of the Process
        if not self.gui_handling.write_text('50'):
            return False
        # > Click mouse button
        if not self.gui_handling.left_mouse_click_relative('PUT pos_x_rel', 'PUT pos_y_rel'):
            return False
        time.sleep(1)
        return True
        
    def analysis_response(self):
        # > Need to create the method
        return True

    def send_evidences(self):
        evidence_path = 'PUT path_screenshot'
        # > take screenshot and save
        if not self.gui_handling.take_screenshot_window(evidence_path):
            return False
        # > send email
        if not self.email_service.send_html_email(evidence_path):
            return False
        return True
        
    def close_app(self):
        # > close the app
        if not self.gui_handling.close_app('PUT name_app.exe'):
            return False
        return True
