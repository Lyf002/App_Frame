from pageobjects.base import BasePage
from appium.webdriver.common.mobileby import By
import time
class HomePage(BasePage):
    """注册页面元素"""
    button_topLeft_loc = (By.ID, "com.pdswp.su.smartcalendar:id/actionbar_left")
    regist_link_loc = (By.ID, "com.pdswp.su.smartcalendar:id/email")
    register_link_loc = (By.ID, "com.pdswp.su.smartcalendar:id/register")
    input_nickname_loc = (By.ID, "com.pdswp.su.smartcalendar:id/username")
    input_mail_loc = (By.ID, "com.pdswp.su.smartcalendar:id/email")
    input_password_loc = (By.ID, "com.pdswp.su.smartcalendar:id/password")
    button_register_loc = (By.ID, "com.pdswp.su.smartcalendar:id/reguser")
    logout_link_loc = (By.ID, "com.pdswp.su.smartcalendar:id/exit")

    """登录页面元素"""
    preLogin_link_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    button_login_loc=(By.ID,"com.pdswp.su.smartcalendar:id/login")

    """修改用户名页面元素"""
    modify_link_loc = (By.ID, "com.pdswp.su.smartcalendar:id/imageView4")
    input_rename_loc = (By.ID, "com.pdswp.su.smartcalendar:id/username")
    button_sureMobify_loc = (By.ID, "com.pdswp.su.smartcalendar:id/quick_add")

    """添加备忘录页面元素"""
    addBWL_link_loc=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")
    input_content_loc=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")
    button_sureAdd_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    button_addImg_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")
    button_green_loc=(By.ID,"com.pdswp.su.smartcalendar:id/add_color_green")
    input_searchText_loc=(By.NAME,"   搜索备忘")

    """搜索备忘录页面元素"""
    button_search_loc=(By.CLASS_NAME,"android.widget.ImageView")
    button_quxiao_loc=(By.NAME,"取消")

    """排序页面元素"""
    button_setting_loc=(By.NAME,"应用设置")
    button_colorSort_loc=(By.ID,"com.pdswp.su.smartcalendar:id/set_color")
    # button_oldTimeSort_loc = (By.ID, "com.pdswp.su.smartcalendar:id/set_timesort")
    # button_newTimeSort_loc = (By.ID, "com.pdswp.su.smartcalendar:id/set_timesortnew")
    button_sort_loc=(By.NAME,"排序")
    button_OK_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")

    """归档页面元素"""
    BWL_first_loc = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")
    button_lookGD_loc=(By.NAME,"归档")
    button_huifu_loc=(By.NAME,"恢复")
    button_back_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")

    """删除备忘录页面元素"""
    button_del_loc=(By.NAME,"删除备忘")
    button_huiShouZhan_loc=(By.NAME,"回收站")
    clear_huiShouZhan_loc = (By.ID, "com.pdswp.su.smartcalendar:id/button")
    button_sureClear_loc=(By.NAME,"确定")

    registerFail_text_loc=(By.NAME,"注册中……")
    BWL01_text = (By.NAME, "BWL01")
    BWL02_text=(By.NAME,"BWL02")
    BWL02_GD_text=(By.NAME,"BWL02")

    def login(self,mail,password):
        self.click(*self.button_topLeft_loc)
        self.click(*self.preLogin_link_loc)
        self.clear(*self.input_mail_loc)
        self.sendkeys(mail, *self.input_mail_loc)
        self.clear(*self.input_password_loc)
        self.sendkeys(password, *self.input_password_loc)
        self.click(*self.button_login_loc)

    def relogin(self,mail,password):
        self.clear(*self.input_mail_loc)
        self.sendkeys(mail, *self.input_mail_loc)
        self.clear(*self.input_password_loc)
        self.sendkeys(password, *self.input_password_loc)
        self.click(*self.button_login_loc)

    def regist(self):
        self.click(*self.button_topLeft_loc)
        self.click(*self.regist_link_loc)
        self.click(*self.register_link_loc)

    def reg_sendkeys(self,nickname,mail,password):
        self.clear(*self.input_nickname_loc)
        self.sendkeys(nickname,*self.input_nickname_loc)
        self.clear(*self.input_mail_loc)
        self.sendkeys(mail, *self.input_mail_loc)
        self.clear(*self.input_password_loc)
        self.sendkeys(password, *self.input_password_loc)
        self.clear(*self.button_register_loc)

    def logout(self):
        self.click(*self.button_topLeft_loc)
        self.click(*self.preLogin_link_loc)
        self.click(*self.logout_link_loc)
        time.sleep(10)

    def modify(self,rename):
        self.click(*self.button_topLeft_loc)
        self.click(*self.preLogin_link_loc)
        self.click(*self.modify_link_loc)
        self.clear(*self.input_rename_loc)
        self.sendkeys(rename,*self.input_rename_loc)
        self.click(*self.button_sureMobify_loc)

    def exit(self):
        self.click(*self.logout_link_loc)

    def add_bwl(self,content1,content2):
        self.click(*self.button_topLeft_loc)        #点击备忘录页左上角图片按钮
        self.click(*self.addBWL_link_loc)
        self.sendkeys(content1,*self.input_content_loc)
        self.click(*self.button_sureAdd_loc)
        self.click(*self.button_addImg_loc)
        self.sendkeys(content2, *self.input_content_loc)
        self.click(*self.button_green_loc)
        self.click(*self.button_sureAdd_loc)

    def search(self,search_text):
        self.click(*self.button_search_loc)
        self.sendkeys(search_text,*self.input_searchText_loc)
        self.driver.keyevent(66)

    def noSet(self):
        self.click(*self.button_quxiao_loc)

    def order(self):
        # self.click(*self.button_topLeft_loc)
        # self.click(*self.button_setting_loc)
        # self.click(*self.button_colorSort_loc)
        # self.click(*self.button_topLeft_loc)
        self.longPress(*self.BWL_first_loc)
        self.click(*self.button_sort_loc)
        time.sleep(2)
        self.swipeDown(686,263,686,549,500)
        time.sleep(3)
        self.swipeDown(686, 349, 686, 130, 500)
        time.sleep(3)
        self.click(*self.button_OK_loc)

    def guidang(self):
        self.longPress(*self.BWL_first_loc)
        self.click(*self.button_lookGD_loc)
        self.click(*self.button_topLeft_loc)
        self.click(*self.button_lookGD_loc)
        time.sleep(2)

    def huanYuan(self):
        self.swipeLeft(556, 163, 450, 163,500)
        time.sleep(3)
        self.click(*self.button_huifu_loc)
        self.click(*self.button_back_loc)  # 点击归档页左上角返回按钮

    def delete(self):
        self.longPress(*self.BWL_first_loc)
        self.click(*self.button_del_loc)
        self.click(*self.button_topLeft_loc)
        self.click(*self.button_huiShouZhan_loc)
        self.click(*self.clear_huiShouZhan_loc)
        self.click(*self.button_sureClear_loc)






