import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Script untuk menggunakan library Unittest dan libarry HtmlTestRunner untuk mengeksekusi Script test yang sudah dibuat
# Unit test berfungsi untuk memberikan hasil apakah Testcase berhasil atau tidak (Pass/Fail) 
# HtmlTestRunner berfungsi untuk membuat laporan hasil testing dalam bentuk sebuah file HTML
import unittest
import HtmlTestRunner

class PopulixLoginTest(unittest.TestCase) :
    @classmethod
    def setUpClass(cls) :
        cls.browser=webdriver.Chrome()
        cls.browser.maximize_window()

    # test apakah url page yang dibuka sesuai atau tidak 
    def test_homePageTitle(self) :
        self.browser.get("https://www.populix.co/login/")
        self.assertEqual("Populix", self.browser.title,"webpage tidak Sesuai")
    
    # Testcase 
    # Klik button Masuk
    # script ini bertujuan untuk menguji apakah fungsi  login berhasil apabila kolom username dan password di isi kosong 
    def test_loginEmailPasswordKosong(self):
        self.browser.get("https://www.populix.co/login/")
        self.browser.find_element(By.NAME, value="username").send_keys("")
        self.browser.find_element(By.NAME, value="password").send_keys("")
        self.browser.find_element(By.ID, value="submit_login").click()
        self.assertEqual("Populix", self.browser.title,"webpage tidak Sesuai")

    # TestCase
    # script ini kita gunakan untuk Mengisi kolom username dan Password secara otomatis setelah halaman login terbuka
    def test_login(self):
        # username dan Password yang akan kita masukkan di halaman login Populix
        username = "qa@gmail.com"
        password = "engineer"
        self.browser.get("https://www.populix.co/login/")
        self.browser.find_element(By.NAME, value="username").send_keys(username)
        self.browser.find_element(By.NAME, value="password").send_keys(password)
        # Klik Masuk
        # script ini bertujuan untuk menguji apakah fungsi button login setelah username dan password di input dan melihat apakah login berhasil atau tidak dengan asumsi email dan password yang dimasukkan sudah terdaftar/valid
        self.browser.find_element(By.ID, value="submit_login").click()
        self.assertEqual("Populix", self.browser.title,"webpage tidak Sesuai")
    
    # TestCase
    # Klik Lupa Kata Sandi
    # script ini bertujuan untuk menguji apakah fungsi "Lupa Kata Sandi" berjalan atau tidak, apakah user diarahkan ke halaman lupa kata sandi setelah di klik
    def test_forgetPassword(forget) :
        forget.browser.get("https://www.populix.co/login/")
        forget.browser.find_element(By.ID, value="btn_to-forgot-password").click()
        forget.assertEqual("Populix", forget.browser.title,"webpage tidak Sesuai")

    # TestCase
    # klik Daftar
    # script ini bertujuan untuk menguji apakah fungsi "Daftar" berjalan atau tidak, apakah user diarahkan ke halaman registrasi setelah di klik
    def test_daftar(daftar) :
        daftar.browser.get("https://www.populix.co/login/")
        daftar.browser.find_element(By.ID, value="btn_to-register").click()
        daftar.assertEqual("Populix", daftar.browser.title,"webpage tidak Sesuai")
    
    # Test Case 
    # klik Facebook
    # script ini bertujuan untuk menguji apakah fungsi "Login dengan Facebook" berjalan atau tidak, apakah user diarahkan ke halaman login facebook setelah d klik
    def test_loginFacebook(fb) :
        fb.browser.get("https://www.populix.co/login/")
        fb.browser.find_element(By.XPATH, '//*[@id="login_facebook"]').click()
        fb.browser.find_element(By.ID, value="btn_resend").click()
        fb.assertEqual("Facebook", fb.browser.title,"webpage tidak Sesuai")
    
    # test Case 
    # klik Google
    # Script ini bertujuan untuk menguji apakah fungsi "Login dengan Google" berjalan atau tidak, apakah user diarahkan ke halaman login Google setelah d klik
    def test_loginGoogle(ggl) :
        ggl.browser.get("https://www.populix.co/login/")
        ggl.browser.find_element(By.XPATH, '//*[@id="login_google"]').click()
        ggl.browser.find_element(By.ID, value="btn_resend").click()
        ggl.assertEqual("Login - Akun Goolge", ggl.browser.title,"webpage tidak Sesuai")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        print("Test Case Selesai")

if __name__=='__main__':
    # unittest.main() 
    # Script ini berfungsi untuk generate report hasil testing kedalam sebuah file html, disimpan pada Folder report pada directory
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Report'))