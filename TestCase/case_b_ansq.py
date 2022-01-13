# -*- coding: utf-8 -*-
from __future__ import absolute_import
from Page.BasePage import Action
from TestCase.models import screenShot
from common.logger import Log
import unittest
import time
import os


class CaseAnsq(Action):
    u"""做题并且能正确出报告"""
    # 课程
    curriculum_loc = ('xpath', '//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ImageView')
    # 查看全部
    all_loc = ('xpath', '//android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView')
    # 校本题库
    schoolbased_loc = ('xpath', '//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView')
    # 搜索
    search_loc = ('id', 'com.fifedu.tsdx:id/ib_head_share')
    # 搜索输入框
    search_input_loc = ('id','com.fifedu.tsdx:id/et_search')
    # communicative单元
    communicative_loc = ('xpath', '//android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView')
    # 模式
    pattern_loc = ('id', 'com.fifedu.tsdx:id/tv_moshi')
    # 权限允许
    approve_loc = ('id', 'com.android.permissioncontroller:id/permission_allow_button')
    # 录音提交
    record_loc = ('id', 'com.fifedu.tsdx:id/av_anim')
    # 挑战结果
    challenge_loc = ('id', 'com.fifedu.tsdx:id/tv_info')

    log = Log()

    def curriculum(self):
        u"""课程栏"""
        self.click_button(self.curriculum_loc)

    def all(self):
        u"""查看全部"""
        self.click_button(self.all_loc)

    def schoolbased(self):
        u"""校本题库"""
        self.click_button(self.schoolbased_loc)

    def search(self):
        u"""点击搜索"""
        self.click_button(self.search_loc)

    def search_input(self):
        u"""搜索输入框"""
        self.click_button(self.search_input_loc)
        self.clear_key(self.search_input_loc)
    def communicative(self):
        self.click_button(self.communicative_loc)

    def approve(self):
        u"""权限允许"""
        self.click_button(self.approve_loc)
    def record(self):
        u"""录音提交"""
        self.click_button(self.record_loc)

    def test_ansq_report(self):
        u"""做题并且能正确出报告"""

        self.curriculum()
        self.all()
        self.schoolbased()
        self.search()
        self.search_input()
        self.send_keys(self.search_input_loc,'communicative')
        # 键盘搜索
        os.system("adb shell input tap 1000 2255")
        self.communicative()
        # self.driver.find_element_by_xpath("//*[@text='Communicative Function: Jobs and Job Interviews']").click()
        self.driver.find_element_by_id("com.fifedu.tsdx:id/tv_moshi").click()
        time.sleep(5)
        screenShot.take_screenShot(self, "Practice")
        os.system("adb shell input tap 958 2170")
        time.sleep(2)
        os.system("adb shell input tap 535 1860")

        # 录音提交
        self.record()
        time.sleep(3)
        screenShot.take_screenShot(self, "Report score")
        text = self.driver.find_element_by_id("com.fifedu.tsdx:id/tv_info").text
        self.assertEqual(text, u'挑战失败！请再接再厉')
        print(u'挑战失败，分数小于60分')


if __name__ == "__main__":
    unittest.main()