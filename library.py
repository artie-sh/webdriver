import time
import pyscreenshot as screen


screenshots = '/home/artie-sh/Documents/screenshots/'
reports = '/home/artie-sh/Documents/reports/'
username = 'artie.sh.87@gmail.com'
password = '931xpqa1'


def get_date():
    return str(time.strftime('%Y.%m.%d'))


def get_time():
    return str(time.strftime('%H:%M:%S'))


def take_screen():
    screen_name = get_date() + '_' + get_time() + '.png'
    screen.grab_to_file(reports + screen_name)
    return screen_name


def add_screen(report, screen_name):
    report.write('<img src="' + screen_name + '" height="50% width="50%"">\n<p>\n' + screen_name + '\n<br>\n<br>\n')


def get_report():
    report = open(reports + get_date() + '.htm', 'w')
    report.write('<html>\n <body> \n')
    return report


def close_report(report):
    report.write('</body> \n </html>')
    report.close()
