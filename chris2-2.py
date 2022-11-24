from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import argparse



class GateWarsBot:

    def __init__(self):
        self.driver = webdriver.Firefox() 
        self.target = 2
        self.numr = 0
        self.timesattacked = 0
        self.count = 0
        self.driver.get('https://main.gatewa.rs/')




    def battlefeild(self):

        time.sleep(4)
        self.driver.implicitly_wait(4)
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.nav > li:nth-child(2) > a:nth-child(1)')))

            battlefeild = self.driver.find_element_by_css_selector('.nav > li:nth-child(2) > a:nth-child(1)')
            battlefeild.click()
            print(Stew().gethtmlstew(self.driver.page_source))
        except Exception as e:
            pass




    def armory(self):

        try:

            armory = self.driver.find_element_by_css_selector('.nav > li:nth-child(4) > a:nth-child(1)')
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '.nav > li:nth-child(4) > a:nth-child(1)'))

            )
            armory.location_once_scrolled_into_view
            armory.click()
        except Exception as e:
            pass

    def farmrepair(self):
        try:
            self.armory()
            time.sleep(3.5)
            repair = self.driver.find_element_by_css_selector(
            'table.table-armory:nth-child(4) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > form:nth-child(1) > div:nth-child(3) > span:nth-child(3) > input:nth-child(1)')
            EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             'table.table-armory:nth-child(4) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > form:nth-child(1) > div:nth-child(3) > span:nth-child(3) > input:nth-child(1)')
            )
            repair.click()
            self.driver.back()
            return 'repair needed'
        except Exception as e:
            if e is True:
                return 'no repair needed'





    def nextpage(self):
            try:

                nextpage = self.driver.find_element_by_css_selector(
                    'div.col-12 > nav:nth-child(4) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')
                WebDriverWait(self.driver, 100).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR,
                         "div.col-12 > nav:nth-child(4) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")))
                nextpage.location_once_scrolled_into_view
                nextpage.click()
            except Exception as e:
                pass

    def repeate(self, repeat):
        print('in reapate')
        while self.timesattacked <= repeat:

            try:

                again = self.driver.find_element_by_css_selector('button.hidden-sm-down')
                again.click()
                goattack = self.driver.find_element_by_css_selector(
                    'html body div.container-fluid div.row.primary main.mine div.row div.col-xs-12.col-lg-6 form.mb-2 div.input-group span.input-group-btn button.btn.btn-outline-secondary')
                WebDriverWait(self.driver, 100).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR,
                         'html body div.container-fluid div.row.primary main.mine div.row div.col-xs-12.col-lg-6 form.mb-2 div.input-group span.input-group-btn button.btn.btn-outline-secondary'))
                )
                time.sleep(3)
                goattack.click()
                self.driver.implicitly_wait(500)
                self.timesattacked += 1
                print('times repated %s', self.timesattacked)

            except Exception as e:
                pass
        else:
                self.timesattacked -= repeat
                self.count += 1
                self.target += 3
                print(self.count)
                print(self.target)
                return print('repeate attack done')


    def farmattack(self, num):


        while self.count < int(num):

            try:
                if self.target >= 90:
                    self.target -= self.target
                    self.nextpage()
                    continue
                if self.numr == 3:
                    self.farmrepair()
                    self.numr -= 3
                    continue
                if self.driver.current_url == 'https://main.gatewa.rs/base.php?game=gatewars':
                    self.driver.back()
                    continue

                else:




                    attackbutton = self.driver.find_element_by_css_selector('tr.hidden-xs-down:nth-child({0}) > td:nth-child(2) > form:nth-child(2) > button:nth-child(4)'.format(self.target))
                    self.driver.implicitly_wait(10)
                    attackbutton.click()
                    self.count += 1
                    print('Attacks: {0}'.format(self.count))
                    self.target += 3
                    self.numr += 1
                    self.driver.back()
                    attackbutton.location_once_scrolled_into_view
            except Exception as e:
                if e.__str__()[9:33] == 'Unable to locate element':
                    self.target += 3
                    self.count -= 1

        else:
            print('done')
            close = input('close browser y for yes?')
            if close == 'y':
                self.driver.close()

    def fightmoderepair(self):
        self.armory()
        try:
            time.sleep(45)
            attackweprepair = self.driver.find_element_by_css_selector('table.table-armory:nth-child(4) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > form:nth-child(1) > div:nth-child(3) > span:nth-child(3) > input:nth-child(1)')
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,"table.table-armory:nth-child(4) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > form:nth-child(1) > div:nth-child(3) > span:nth-child(3) > input:nth-child(1)"))
            )
            attackweprepair.click()
            defweprepair = self.driver.find_element_by_css_selector('table.table-armory:nth-child(4) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(3) > form:nth-child(1) > div:nth-child(3) > span:nth-child(3) > input:nth-child(1)')
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'table.table-armory:nth-child(4) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(3) > form:nth-child(1) > div:nth-child(3) > span:nth-child(3) > input:nth-child(1)')
            )
            defweprepair.click()

        except Exception as e:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num')
    args = parser.parse_args()
    bot = GateWarsBot()
    mode = input("Press Enter to continue or w...")
    if mode == 'w':
        bot.target += 1
        print(bot.target)
        input('War page peram set click enter to continue..')
        bot.farmattack(args.num)
    else:
        bot.farmattack(args.num)
main()

"""

tr.hidden-xs-down:nth-child(90) > td:nth-child(2) > form:nth-child(2) > button:nth-child(4)



  self.driver.back()
            self.driver.back()
https://main.gatewa.rs/battlefieldE.php

    """
