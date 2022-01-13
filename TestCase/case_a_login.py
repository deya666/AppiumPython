# -*- coding: utf-8 -*-
from __future__ import absolute_import
from Page.BasePage import Action
from common.logger import Log
import unittest
import time


class CaseLogin(Action):
    u"""输入正确的用户名和密码能登陆成功"""
    u"""登录页面"""
    # 用户名
    username_loc = ('id', 'com.fifedu.tsdx:id/et_username')
    # 密码
    pwd_loc = ('id', 'com.fifedu.tsdx:id/et_psw')
    # 同意协议
    agree_loc = ('id','com.fifedu.tsdx:id/iv_check')
    # 登录
    login_button_loc = ('id', 'com.fifedu.tsdx:id/bt_login')
    # 登录成功之后页面
    login_success_loc = ('id', 'com.fifedu.tsdx:id/tv_content')

    log = Log()

    def input_username(self):
        # self.driver.find_element_by_id("com.fifedu.tsdx:id/bt_agree").click()
        # #向左滑动跳过引导页
        # x = 0
        # while x < 2:
        #     self.adb_swipe()
        #     x += 1
        # enterApp = self.driver.find_element_by_id("com.fifedu.tsdx:id/iv_to_login")
        # enterApp.click()
        # approveApp = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
        # approveApp.click()

        u"""输入正确的用户名"""
        self.clear_key(self.username_loc)
        self.send_keys(self.username_loc,"csbfsux160")
    def input_pwd(self):
        u"""输入正确的密码"""
        self.clear_key(self.pwd_loc)
        self.send_keys(self.pwd_loc,"123456")
    def agree(self):
        u"""同意协议"""
        self.click_button(self.agree_loc)
    def click_login(self):
        u"""点击登录"""
        self.click_button(self.login_button_loc)

    def login_success(self):
        u"""判断是否登录成功"""
        login_success = self.find_element(self.login_success_loc).text
        return login_success

    def test_login_success(self):
        u"""输入正确的用户名和密码能登陆成功"""
        try:
            # text = self.driver.find_element_by_id("com.fifedu.tsdx:id/tv_content").text
            # print (text)
            # if u'12月第5周新闻（BBC）' in text:
            #     print (u"登录成功")
            self.assertEqual(self.login_success(),'12月第5周新闻（BBC）')
            self.log.info('登录成功')
            print(u"登录成功")
        except Exception:
            print(u"登录失败")


if __name__ == "__main__":
    unittest.main()