import time
import library.paths as paths
import library.general as lib
import pyscreenshot as screen

class Report:


    def __init__(self):
        self.report = open(paths.reports + lib.get_date() + '.htm', 'w')
        self.report.write('<html>\n <body> \n')


    def add_screen(self):
        screen_name = time.strftime('%Y.%m.%d') + '_' + time.strftime('%H.%M.%S') + '.png'
        screen.grab_to_file(paths.reports + screen_name)
        self.report.write('<img src="' + screen_name + '" height="50% width="50%"">\n<p>\n' + screen_name + '\n<br>\n<br>\n')


    def close(self):
        self.report.write('</body>\n</html>')
        self.report.close()