# 📦 مثبت تطبيقات Android TV الاحترافي (APK/XAPK Installer Pro)

![إصدار بايثون](https://img.shields.io/badge/Python-3.8%2B-blue)
![المنصة](https://img.shields.io/badge/Platform-Windows_|_Android_TV-green)
![الواجهة](https://img.shields.io/badge/UI-CustomTkinter-blueviolet)
![الترخيص](https://img.shields.io/badge/License-MIT-orange)

---

<div align="center">
  <h3>أداة عصرية لتثبيت التطبيقات (Sideloading) على شاشات الأندرويد لاسلكياً</h3>
</div>

---

## 📌 نبذة عن المشروع
برنامج سطح مكتب مستقل بواجهة رسومية عصرية (Dark Mode) مصمم لتسهيل عملية تثبيت التطبيقات الخارجية على أجهزة **Android TV** (مثل Xiaomi Stick, Chromecast, Mi Box، والشاشات الذكية). 
الأداة تغنيك عن استخدام الفلاش ميموري (USB) أو تطبيقات نقل الملفات المعقدة؛ حيث تقوم بنقل وتثبيت التطبيقات من كمبيوترك إلى التلفاز مباشرة عبر شبكة الـ Wi-Fi بضغطة زر.

## ✨ المميزات الرئيسية
* **🚀 تثبيت لاسلكي مباشر:** نقل وتثبيت التطبيقات عبر شبكة الواي فاي (ADB) بدون أي أسلاك.
* **🗜️ الدعم الذكي لملفات XAPK:** الأداة تدعم ملفات `.xapk` بشكل أصلي؛ حيث تقوم بفك الضغط تلقائياً في الخلفية، استخراج التطبيق الأساسي، تثبيته، ثم تنظيف الملفات المؤقتة.
* **🔍 فحص الشبكة التلقائي:** لا حاجة لكتابة عنوان الـ IP يدوياً! الأداة تقوم بفحص شبكتك المحلية والعثور على أجهزة التلفاز المتصلة تلقائياً.
* **🎨 واجهة احترافية (Pro UI):** تصميم عصري ومريح للعين باستخدام مكتبة `CustomTkinter` مع شاشة أوامر (Console) لمتابعة حالة التثبيت خطوة بخطوة.
* **🛡️ حماية من انقطاع الاتصال:** مبرمجة خصيصاً للتعامل مع التطبيقات كبيرة الحجم (مهلة انتظار تصل إلى 120 ثانية) لضمان عدم فشل التثبيت للألعاب والتطبيقات الضخمة.

## 🛠️ المتطلبات الأساسية (مهم جداً)
لكي تعمل الأداة، يجب تفعيل خيار **"تصحيح أخطاء USB"** في جهاز التلفاز:
1. اذهب إلى `الإعدادات` > `تفضيلات الجهاز` > `لمحة` (About).
2. انزل إلى `رقم الإصدار` (Build) واضغط عليه **7 مرات متتالية** حتى يظهر إشعار "أنت الآن مطور برامج".
3. ارجع للخلف، وادخل إلى `خيارات المطور` (Developer options).
4. قم بتفعيل **تصحيح أخطاء USB (USB Debugging)**.
5. *تأكد أن الكمبيوتر والتلفاز متصلان بنفس شبكة الواي فاي.*

## 🚀 طريقة التثبيت والتشغيل للمطورين

1. **قم بتحميل المشروع:**

   ```bash
       git clone [https://github.com/Turki-Alshaikh/APK-TV-Installer.git](https://github.com/Turki-Alshaikh/APK-TV-Installer.git)
   cd APK-TV-Installer


   pip install adb-shell cryptography customtkinter


   python apk_installer.py
   

   💡 ملاحظة هامة عند التشغيل لأول مرة: بمجرد الضغط على زر التثبيت، انظر إلى شاشة التلفاز. ستظهر رسالة تطلب منك "السماح بتصحيح أخطاء USB". ضع علامة الصح على "السماح دائماً" واضغط موافق.

📦 تحويل الأداة إلى برنامج تنفيذي (.exe)
إذا أردت استخدام الأداة كبرنامج ويندوز جاهز بدون الحاجة لكتابة أوامر بايثون في كل مرة
   ```bash
pip install pyinstaller
pyinstaller --noconsole --onefile apk_installer.py
```
## 🚀 Sponsored & Maintained By | برعاية متجر مفاتيحي

This project is developed and maintained as an open-source initiative. If this tool streamlined your workflow or saved you time, consider supporting the developer by upgrading your digital workspace through our store:

**[Mfatihy Store (متجر مفاتيحي)](https://mfatihy.com)** is your premium destination for genuine software solutions. We provide authentic **[Windows and Office keys](https://mfatihy.com/Office/c2015509396)**, top-tier antivirus subscriptions, and professional design tools (Adobe & Autodesk) at unbeatable prices with instant automated delivery.

---

تم تطوير هذا المشروع البرمجي وإتاحته مجاناً لدعم مجتمع المطورين والمستخدمين. إذا ساعدتك هذه الأداة في إنجاز مهامك، يمكنك دعم استمرارية التطوير من خلال زيارة متجرنا الرقمي:

**[متجر مفاتيحي (Mfatihy)](https://mfatihy.com)** هو الوجهة الأولى والموثوقة في السعودية والخليج للحصول على **[تراخيص البرامج الأصلية](https://mfatihy.com)**. نوفر لك **[مفاتيح تفعيل ويندوز وأوفيس](https://mfatihy.com/windows-keys/c1242520213)** مدى الحياة، بالإضافة إلى اشتراكات برامج التصميم الهندسية والاحترافية بأفضل الأسعار، مع ضمان التسليم الفوري والتفعيل الآمن. 

[![Visit Mfatihy](https://img.shields.io/badge/Visit_Store-Mfatihy.com-2ea44f?style=for-the-badge&logo=shopify)](https://mfatihy.com)


