import os
import time
import zipfile
import shutil
import logging
import threading
import socket
import concurrent.futures
import customtkinter as ctk  # المكتبة الجديدة للتصميم الاحترافي
from tkinter import filedialog, messagebox
from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.sign_cryptography import CryptographySigner
from adb_shell.auth.keygen import keygen

# ---------------------------------------------------------
# إعدادات المظهر العام (Theme Settings)
# ---------------------------------------------------------
ctk.set_appearance_mode("Dark")  # الوضع الليلي الاحترافي
ctk.set_default_color_theme("blue")  # اللون الأزرق للعناصر

# ---------------------------------------------------------
# 1. إعداد نظام السجلات (Logger) للواجهة
# ---------------------------------------------------------
class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text_widget.configure(state='normal')
            self.text_widget.insert("end", msg + '\n')
            self.text_widget.configure(state='disabled')
            self.text_widget.yview("end")
        self.text_widget.after(0, append)

# ---------------------------------------------------------
# 2. فئة المثبت (Installer Class)
# ---------------------------------------------------------
class AndroidTVInstaller:
    def __init__(self, ip_address: str, port: int = 5555, key_path: str = 'adbkey'):
        self.ip_address = ip_address
        self.port = port
        self.key_path = key_path
        self.device = AdbDeviceTcp(self.ip_address, self.port)
        self.is_connected = False
        self.logger = logging.getLogger("APK_Installer")

    def _get_signer(self) -> CryptographySigner:
        if not os.path.exists(self.key_path):
            self.logger.info("🔑 جاري توليد مفاتيح مصادقة جديدة...")
            keygen(self.key_path)
        return CryptographySigner(self.key_path)

    def connect(self) -> None:
        self.logger.info(f"📡 محاولة الاتصال بالجهاز: {self.ip_address}...")
        try:
            signer = self._get_signer()
            self.device.connect(rsa_keys=[signer], transport_timeout_s=15)
            self.is_connected = True
            self.logger.info("✅ تم الاتصال بالتلفاز بنجاح!")
        except Exception as e:
            self.logger.error("❌ فشل الاتصال! تأكد من تشغيل التلفاز ووجوده على نفس الشبكة.")
            raise

    def install_apk(self, local_apk_path: str) -> bool:
        if not self.is_connected:
            return False

        filename = os.path.basename(local_apk_path)
        remote_path = f"/data/local/tmp/{filename}"

        try:
            self.logger.info(f"📤 جاري نقل [{filename}] إلى التلفاز...")
            self.device.push(local_apk_path, remote_path)
            self.logger.info("✅ تم النقل بنجاح. جاري التثبيت الآن (الرجاء الانتظار)...")

            # تم إضافة وقت انتظار 120 ثانية لتجنب انقطاع الاتصال مع الملفات الكبيرة
            install_cmd = f"pm install -r \"{remote_path}\""
            result = self.device.shell(install_cmd, read_timeout_s=120) 
            
            self.device.shell(f"rm \"{remote_path}\"")

            if "Success" in result:
                self.logger.info(f"🎉 تم تثبيت التطبيق بنجاح على التلفاز!")
                return True
            else:
                self.logger.error(f"❌ خطأ أثناء التثبيت: {result}")
                return False

        except Exception as e:
            self.logger.error(f"⚠️ حدث خطأ غير متوقع: {str(e)}")
            return False

    def disconnect(self) -> None:
        if self.is_connected:
            self.device.close()
            self.logger.info("🔌 تم إنهاء الاتصال بأمان.")

# ---------------------------------------------------------
# 3. واجهة المستخدم الرسومية (Modern GUI)
# ---------------------------------------------------------
class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("APK TV Installer - Pro")
        self.root.geometry("700x650")
        
        self.selected_file_path = None
        self.setup_ui()
        self.setup_logging()

    def setup_ui(self):
        # عنوان التطبيق
        title_label = ctk.CTkLabel(self.root, text="📦 مثبت تطبيقات Android TV", font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"))
        title_label.pack(pady=(25, 20))

        # 1. إطار الشبكة (الـ IP والفحص)
        network_frame = ctk.CTkFrame(self.root, corner_radius=10)
        network_frame.pack(fill="x", padx=25, pady=10)

        ip_label = ctk.CTkLabel(network_frame, text="عنوان التلفاز (IP):", font=ctk.CTkFont(size=14))
        ip_label.pack(side="left", padx=15, pady=15)

        self.ip_combo = ctk.CTkComboBox(network_frame, values=["192.168.100.45"], font=ctk.CTkFont(size=14), width=180)
        self.ip_combo.pack(side="left", padx=5)

        self.scan_btn = ctk.CTkButton(network_frame, text="🔍 اكتشاف الأجهزة", command=self.start_network_scan, fg_color="#333333", hover_color="#444444")
        self.scan_btn.pack(side="right", padx=15)

        # 2. إطار اختيار الملف (APK / XAPK)
        file_frame = ctk.CTkFrame(self.root, corner_radius=10)
        file_frame.pack(fill="x", padx=25, pady=10)

        self.file_btn = ctk.CTkButton(file_frame, text="📂 تصفح واختيار التطبيق", command=self.select_file, height=40, font=ctk.CTkFont(size=15), fg_color="#2b2b2b", hover_color="#3b3b3b")
        self.file_btn.pack(pady=(20, 5))

        self.file_label = ctk.CTkLabel(file_frame, text="لم يتم اختيار أي ملف", text_color="gray", font=ctk.CTkFont(size=12))
        self.file_label.pack(pady=(0, 15))

        # 3. زر التثبيت الرئيسي (بارز وكبير)
        self.install_btn = ctk.CTkButton(self.root, text="⚡ بدء التثبيت الآن", command=self.start_installation, state="disabled", height=50, font=ctk.CTkFont(size=16, weight="bold"))
        self.install_btn.pack(fill="x", padx=25, pady=15)

        # 4. شاشة العمليات (Console)
        self.console_text = ctk.CTkTextbox(self.root, font=ctk.CTkFont(family="Consolas", size=13), fg_color="#0d1117", text_color="#00ff00", wrap="word", corner_radius=10)
        self.console_text.pack(fill="both", expand=True, padx=25, pady=(0, 25))
        self.console_text.configure(state="disabled")

    def setup_logging(self):
        self.logger = logging.getLogger("APK_Installer")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            text_handler = TextHandler(self.console_text)
            formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt="%H:%M:%S")
            text_handler.setFormatter(formatter)
            self.logger.addHandler(text_handler)

    # --- دوال الشبكة والاكتشاف ---
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def scan_port(self, ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((ip, 5555))
        sock.close()
        return result == 0

    def network_scan_task(self):
        self.logger.info("🔍 جاري فحص الشبكة، الرجاء الانتظار...")
        local_ip = self.get_local_ip()
        base_ip = local_ip.rsplit('.', 1)[0] + '.'
        ips_to_scan = [base_ip + str(i) for i in range(1, 255)]
        
        discovered_devices = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            future_to_ip = {executor.submit(self.scan_port, ip): ip for ip in ips_to_scan}
            for future in concurrent.futures.as_completed(future_to_ip):
                ip = future_to_ip[future]
                if future.result():
                    discovered_devices.append(ip)

        if discovered_devices:
            self.logger.info(f"🎯 تم العثور على أجهزة: {', '.join(discovered_devices)}")
            self.root.after(0, lambda: self.ip_combo.configure(values=discovered_devices))
            self.root.after(0, lambda: self.ip_combo.set(discovered_devices[0]))
        else:
            self.logger.warning("⚠️ لم يتم العثور على أجهزة.")
        
        self.root.after(0, self.enable_buttons)

    def start_network_scan(self):
        self.clear_console()
        self.disable_buttons()
        threading.Thread(target=self.network_scan_task, daemon=True).start()

    # --- دوال اختيار وتثبيت الملفات ---
    def select_file(self):
        filepath = filedialog.askopenfilename(
            title="اختر ملف التطبيق",
            filetypes=(("Android Apps", "*.apk *.xapk"), ("All files", "*.*"))
        )
        if filepath:
            self.selected_file_path = filepath
            filename = os.path.basename(filepath)
            self.file_label.configure(text=f"تم اختيار: {filename}", text_color="#00E676")
            self.enable_buttons()

    def handle_xapk(self, xapk_path):
        temp_dir = os.path.join(os.getcwd(), "temp_xapk_extract")
        self.logger.info("🗜️ جاري تجهيز ملف الـ XAPK...")
        try:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            os.makedirs(temp_dir)

            with zipfile.ZipFile(xapk_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            apk_files = [os.path.join(r, f) for r, d, files in os.walk(temp_dir) for f in files if f.endswith(".apk")]
            if not apk_files:
                self.logger.error("❌ ملف الـ XAPK تالف أو لا يحتوي على تطبيق.")
                return None

            main_apk = max(apk_files, key=os.path.getsize)
            self.logger.info(f"✅ تم استخراج الملف الأساسي: {os.path.basename(main_apk)}")
            return main_apk

        except Exception as e:
            self.logger.error(f"❌ فشل فك الضغط: {str(e)}")
            return None

    def run_install_task(self, target_ip, file_path):
        installer = AndroidTVInstaller(ip_address=target_ip)
        try:
            actual_apk_path = file_path
            temp_used = False
            
            if file_path.lower().endswith('.xapk'):
                actual_apk_path = self.handle_xapk(file_path)
                temp_used = True
                if not actual_apk_path:
                    return

            installer.connect()
            installer.install_apk(actual_apk_path)

        except Exception as e:
            self.logger.error("❌ توقفت العملية.")
        finally:
            installer.disconnect()
            if temp_used and os.path.exists("temp_xapk_extract"):
                shutil.rmtree("temp_xapk_extract", ignore_errors=True)
            self.root.after(0, self.enable_buttons)

    def start_installation(self):
        target_ip = self.ip_combo.get().strip()
        if not target_ip:
            messagebox.showerror("خطأ", "الرجاء تحديد التلفاز أولاً.")
            return
        if not self.selected_file_path:
            return

        self.clear_console()
        self.disable_buttons()
        threading.Thread(target=self.run_install_task, args=(target_ip, self.selected_file_path), daemon=True).start()

    # --- دوال مساعدة للواجهة ---
    def clear_console(self):
        self.console_text.configure(state='normal')
        self.console_text.delete(1.0, "end")
        self.console_text.configure(state='disabled')

    def disable_buttons(self):
        self.install_btn.configure(state="disabled")
        self.file_btn.configure(state="disabled")
        self.scan_btn.configure(state="disabled")

    def enable_buttons(self):
        self.scan_btn.configure(state="normal")
        self.file_btn.configure(state="normal")
        if self.selected_file_path:
            self.install_btn.configure(state="normal")

if __name__ == "__main__":
    root = ctk.CTk()
    app = InstallerApp(root)
    root.mainloop()
