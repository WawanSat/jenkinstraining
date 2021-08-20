from selenium import webdriver

def test_setup():
	global driver
	driver = webdriver.Chrome(executable_path="D:/Source/Free/chromedriver_win32/chromedriver.exe")
	driver.maximize_window();

def test_form_entry():
	driver.get("http://localhost/form.php")
	# mengambil kolom
	driver.find_element_by_name("nip").send_keys("121212")
	driver.find_element_by_name("nama").send_keys("wawan")
	driver.find_element_by_name("nik").send_keys("0012020")
	driver.find_element_by_name("alamat").send_keys("legok")
	driver.find_element_by_name("perusahaan").send_keys("mamat")
	driver.find_element_by_name("tanggal").send_keys("10/01/2020")
	driver.find_element_by_name("divisi").send_keys("hrd")
	driver.find_element_by_name("posisi").send_keys("staff")
	driver.find_element_by_name("gaji").send_keys("1200000")
	driver.find_element_by_name("atasan").send_keys("tri")
	driver.find_element_by_name("submit").click()

def test_clean_up():
	driver.close()
	driver.quit()
	print("Test Selesai...")