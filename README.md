# Selenium Test Otomasyonu Projesi 🚀

Bu proje, Page Object Model (POM) tasarım deseni kullanarak Selenium WebDriver ile test otomasyonu için hazırlanmış bir framework'tür.

## 📁 Proje Yapısı

```
SeleniumBase/
├── env/                    # Ortam yapılandırmaları
│   └── constants.py        # Sabitler ve yapılandırma değişkenleri
├── pages/                  # Page Object Model sınıfları
│   ├── base_page.py        # Temel sayfa sınıfı
│   └── login_page.py       # Login sayfası sınıfı
├── tests/                  # Test dosyaları
│   └── test_login.py       # Login test senaryoları
├── utils/                  # Yardımcı fonksiyonlar
│   └── image_helper.py     # Ekran görüntüsü alma fonksiyonları
├── reports/                # Test raporları
│   └── report.html         # HTML test raporu
├── conftest.py            # Pytest fixture'ları
├── pytest.ini            # Pytest yapılandırması
└── requirements.txt       # Python bağımlılıkları
```

## 🏗️ Mimari Tasarım

### Page Object Model (POM)
- **BasePage**: Tüm sayfa sınıflarının miras aldığı temel sınıf
- **Specific Pages**: Her web sayfası için ayrı sınıf (örn: LoginPage)
- **Locator'lar**: Sayfa elementleri class seviyesinde tanımlanır
- **Methods**: Sayfa ile etkileşim fonksiyonları

### Test Yapısı
- **Test Classes**: Her feature için ayrı test sınıfı
- **Fixtures**: Driver ve WebDriverWait için pytest fixture'ları
- **Assertions**: Test sonuçlarını doğrulama

### Utilities
- **Screenshot Helper**: Test başarısız olduğunda otomatik ekran görüntüsü
- **Constants**: URL'ler, path'ler ve diğer sabitler

## 🚀 Yeni Website için Proje Kurulumu

### 1. Proje Hazırlığı

```bash
# Yeni proje klasörü oluştur
mkdir YeniWebsiteTest
cd YeniWebsiteTest

# Virtual environment oluştur
python -m venv selenium-env
selenium-env\Scripts\activate  # Windows
# source selenium-env/bin/activate  # Linux/Mac

# Bu projeyi klonla veya dosyaları kopyala
git clone <bu-proje-url>
# veya dosyaları manuel kopyala
```

### 2. Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

### 3. Yapılandırmaları Güncelle

#### `env/constants.py` dosyasını düzenle:
```python
class Paths():
    SCREENSHOT = "C:\\YeniProje\\Screenshots\\"

class URL():
    BASE_URL = "https://yeni-website.com"
    DASHBOARD_URL = f"{BASE_URL}/dashboard"
    PROFILE_URL = f"{BASE_URL}/profile"

class DateFormat():
    DATE_FORMAT = "%d-%m-%Y"
    TIME_FORMAT = "%H-%M-%S"

class TestData():
    VALID_USERNAME = "test_user"
    VALID_PASSWORD = "test_pass"
    INVALID_USERNAME = "invalid_user"
```

### 4. Yeni Page Object'leri Oluştur

#### Örnek: `pages/homepage.py`
```python
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    # Locator'lar
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-btn")
    USER_MENU = (By.CSS_SELECTOR, ".user-menu")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Çıkış Yap']")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
    def open(self):
        self.driver.get("https://yeni-website.com")
    
    def search_product(self, product_name):
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
    
    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_LINK)
```

### 5. Test Senaryolarını Yaz

#### Örnek: `tests/test_homepage.py`
```python
from pages.homepage import HomePage
from pages.login_page import LoginPage

class TestHomePage():
    def test_search_functionality(self, driver, wait):
        # Login işlemi
        login_page = LoginPage(driver, wait)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        # Ana sayfa işlemleri
        home_page = HomePage(driver, wait)
        home_page.search_product("laptop")
        
        # Assertion
        assert "laptop" in driver.current_url.lower()
    
    def test_logout_functionality(self, driver, wait):
        # Login
        login_page = LoginPage(driver, wait)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        # Logout
        home_page = HomePage(driver, wait)
        home_page.logout()
        
        # Assertion
        assert "login" in driver.current_url
```

### 6. Base Page'i Genişlet (İsteğe Bağlı)

```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage():
    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def is_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False
    
    def select_dropdown(self, locator, value):
        dropdown = self.wait.until(EC.element_to_be_clickable(locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)
    
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
```

## 🔧 Testleri Çalıştırma

### Tüm testleri çalıştır:
```bash
pytest
```

### Belirli bir test dosyasını çalıştır:
```bash
pytest tests/test_login.py
```

### Belirli bir test methodunu çalıştır:
```bash
pytest tests/test_login.py::TestLogin::test_successfull
```

### Verbose mod ile çalıştır:
```bash
pytest -v
```

### HTML raporu ile çalıştır:
```bash
pytest --html=reports/report.html
```

## 📊 Test Raporları

- HTML raporları `reports/report.html` dosyasında oluşturulur
- Başarısız testlerin ekran görüntüleri otomatik olarak alınır
- Screenshots klasörü tarih bazında organize edilir

## 🛠️ Özellikler

- ✅ Page Object Model tasarım deseni
- ✅ Pytest framework kullanımı
- ✅ Otomatik ekran görüntüsü alma
- ✅ HTML test raporları
- ✅ WebDriverWait ile güvenli element bekleme
- ✅ Modüler ve ölçeklenebilir yapı
- ✅ Cross-browser test desteği hazır

## 📝 Best Practices

1. **Locator Strategy**: ID > Name > CSS Selector > XPath sıralamasını takip edin
2. **Wait Strategy**: Implicit wait yerine explicit wait kullanın
3. **Test Data**: Hassas verileri constants.py'da tutun
4. **Page Methods**: Her sayfa işlemi için ayrı method oluşturun
5. **Assertions**: Her testte en az bir assertion bulunmalı
6. **Screenshot**: Başarısız testlerde otomatik screenshot alın

## 🚨 Dikkat Edilmesi Gerekenler

- Chrome driver'ın güncel olduğundan emin olun
- Screenshot path'inin var olduğundan emin olun
- Test verilerini güvenli bir şekilde saklayın
- Browser'ı her testten sonra kapatın (conftest.py'da yapılıyor)

## 🤝 Katkıda Bulunma

1. Fork'layın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Commit'leyin (`git commit -am 'Yeni özellik eklendi'`)
4. Push'layın (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📞 Destek

Herhangi bir sorunuz olursa, issue açabilir veya iletişime geçebilirsiniz.

---

**Not**: Bu framework, herhangi bir web sitesi için kolayca adapte edilebilir. Sadece page object'leri ve test senaryolarını güncelleyerek kullanmaya başlayabilirsiniz.
