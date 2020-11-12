import shutil
import webbrowser


def open(url):
    browser = 'opera-beta'
    if shutil.which(browser):
        webbrowser.register(browser, None, webbrowser.Opera(browser))
        
    webbrowser.get(using=browser).open(url)
