
<div align="center">

# 📦 APK/XAPK Installer Pro

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows_|_Android_TV-green)
![UI](https://img.shields.io/badge/UI-CustomTkinter-blueviolet)
![License](https://img.shields.io/badge/License-MIT-orange)

[**[🇸🇦 اقرأ التفاصيل باللغة العربية]**](#-النسخة-العربية)

### A modern GUI tool for wirelessly sideloading apps to Android smart screens.

</div>

---

## 📌 About The Project
A standalone desktop application with a modern Graphical User Interface (Dark Mode) designed to streamline the process of sideloading external apps onto **Android TV** devices (such as Xiaomi Stick, Chromecast, Mi Box, and Smart TVs). 
This tool eliminates the need for USB flash drives or complex file-transfer apps. It securely transfers and installs applications directly from your PC to your TV over Wi-Fi with a single click.

## ✨ Key Features
* **🚀 True Wireless Installation:** Transfer and install apps over your local Wi-Fi network via ADB—no cables required.
* **🗜️ Smart XAPK Support:** Native support for `.xapk` files. The tool automatically extracts the package, installs the core application, and seamlessly cleans up temporary files in the background.
* **🔍 Auto-Network Scanning:** No need to type IP addresses manually! The tool scans your local network and automatically discovers connected Android TV devices.
* **🎨 Professional UI:** Built with `CustomTkinter` for a sleek, eye-friendly design, featuring a live console to monitor the installation progress step-by-step.
* **🛡️ Timeout Protection:** Specifically engineered to handle massive applications and games with an extended 120-second timeout, ensuring large installations don't fail midway.

## 🛠️ Prerequisites (Crucial)
For this tool to work, you **must enable "USB Debugging"** on your TV:
1. Go to `Settings` > `Device Preferences` > `About`.
2. Scroll down to `Build` and click it **7 times** until you see the "You are now a developer" prompt.
3. Go back, and open `Developer options`.
4. Enable **USB Debugging**.
5. *Ensure both your PC and TV are connected to the same Wi-Fi network.*

## 🚀 Installation & Usage (For Developers)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Turki-Alshaikh/APK-TV-Installer.git](https://github.com/Turki-Alshaikh/APK-TV-Installer.git)
   cd APK-TV-Installer



2. **Install required dependencies:**

```bash
pip install adb-shell cryptography customtkinter

```


3. **Run the tool:**
```bash
python apk_installer.py

```


> **💡 First-run Note:** As soon as you click 'Install' for the first time, look at your TV screen. A prompt will appear asking to "Allow USB debugging". Check "Always allow from this computer" and click OK.



### 📦 Compile to Standalone (.exe)

If you want to use the tool as a ready-to-run Windows executable without typing Python commands every time:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile apk_installer.py

```

---

---

## 📦 مثبت تطبيقات Android TV الاحترافي (النسخة العربية)

أداة سطح مكتب مستقلة بواجهة رسومية عصرية (Dark Mode) مصممة لتسهيل عملية تثبيت التطبيقات الخارجية على أجهزة **Android TV** (مثل Xiaomi Stick, Chromecast, Mi Box، والشاشات الذكية).
الأداة تغنيك عن استخدام الفلاش ميموري (USB) أو تطبيقات نقل الملفات المعقدة؛ حيث تقوم بنقل وتثبيت التطبيقات من كمبيوترك إلى التلفاز مباشرة عبر شبكة الـ Wi-Fi بضغطة زر.

### ✨ المميزات الرئيسية

* **🚀 تثبيت لاسلكي مباشر:** نقل وتثبيت التطبيقات عبر شبكة الواي فاي (ADB) بدون أي أسلاك.
* **🗜️ الدعم الذكي لملفات XAPK:** الأداة تدعم ملفات `.xapk` بشكل أصلي؛ حيث تقوم بفك الضغط تلقائياً في الخلفية، استخراج التطبيق الأساسي، تثبيته، ثم تنظيف الملفات المؤقتة.
* **🔍 فحص الشبكة التلقائي:** لا حاجة لكتابة عنوان الـ IP يدوياً! الأداة تقوم بفحص شبكتك المحلية والعثور على أجهزة التلفاز المتصلة تلقائياً.
* **🎨 واجهة احترافية (Pro UI):** تصميم عصري ومريح للعين باستخدام مكتبة `CustomTkinter` مع شاشة أوامر (Console) لمتابعة حالة التثبيت خطوة بخطوة.
* **🛡️ حماية من انقطاع الاتصال:** مبرمجة خصيصاً للتعامل مع التطبيقات كبيرة الحجم (مهلة انتظار تصل إلى 120 ثانية) لضمان عدم فشل التثبيت للألعاب والتطبيقات الضخمة.

### 🛠️ المتطلبات الأساسية (مهم جداً)

لكي تعمل الأداة، يجب تفعيل خيار **"تصحيح أخطاء USB"** في جهاز التلفاز:

1. اذهب إلى `الإعدادات` > `تفضيلات الجهاز` > `لمحة` (About).
2. انزل إلى `رقم الإصدار` (Build) واضغط عليه **7 مرات متتالية** حتى يظهر إشعار "أنت الآن مطور برامج".
3. ارجع للخلف، وادخل إلى `خيارات المطور` (Developer options).
4. قم بتفعيل **تصحيح أخطاء USB (USB Debugging)**.
5. *تأكد أن الكمبيوتر والتلفاز متصلان بنفس شبكة الواي فاي.*

### 🚀 طريقة التثبيت والتشغيل للمطورين

1. **قم بتحميل المشروع:**
```bash
git clone [https://github.com/Turki-Alshaikh/APK-TV-Installer.git](https://github.com/Turki-Alshaikh/APK-TV-Installer.git)
cd APK-TV-Installer

```


2. **تثبيت المكتبات المطلوبة:**
```bash
pip install adb-shell cryptography customtkinter

```


3. **تشغيل الأداة:**
```bash
python apk_installer.py

```


> **💡 ملاحظة هامة عند التشغيل لأول مرة:** بمجرد الضغط على زر التثبيت، انظر إلى شاشة التلفاز. ستظهر رسالة تطلب منك "السماح بتصحيح أخطاء USB". ضع علامة الصح على "السماح دائماً" واضغط موافق.



### 📦 تحويل الأداة إلى برنامج تنفيذي (.exe)

إذا أردت استخدام الأداة كبرنامج ويندوز جاهز بدون الحاجة لكتابة أوامر بايثون في كل مرة:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile apk_installer.py

```

---

---

## 📺 Supported By | بدعم من متجر مفاتيحي

Tools like this are essential when your smart TV setup requires sideloading external apps to overcome built-in store limitations. While you take full control of your Android TV's software ecosystem, you can secure and upgrade your PC environment with **[Mfatihy Store](https://mfatihy.com)**. We provide developers and everyday users with genuine **[Windows and Office keys](https://mfatihy.com/Office/c2015509396)**, premium design software, and digital utilities at unbeatable prices, backed by reliable delivery and dedicated technical support.

وكما تحرص على ترقية وتخصيص بيئة التلفاز الذكي الخاص بك، يمكنك الارتقاء ببيئة عمل حاسوبك الشخصي عبر **[متجر مفاتيحي (Mfatihy)](https://mfatihy.com)**. نحن نوفر لك **[مفاتيح تفعيل ويندوز وأوفيس](https://mfatihy.com/windows-keys/c1242520213)** الأصلية، وبرامج التصميم الاحترافية بأسعار منافسة جداً. وجهتك التقنية الموثوقة للحصول على تراخيص رقمية آمنة، مع التزامنا التام بسياسات دعم وتسليم موثوقة تضمن حقوقك.

