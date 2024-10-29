import tkinter as tk
import speech_recognition as sr
import webbrowser
import os
import threading

recognizer = sr.Recognizer()

def ses_dinle():
    def arka_planda_ses_dinle():
        with sr.Microphone() as source:
            durum_label.config(text="Lütfen konuşun...")
            window.update()
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language="tr-TR")
                durum_label.config(text=f"Siz: {text}")
                komut_analiz_et(text)
            except sr.UnknownValueError:
                durum_label.config(text="Ses anlaşılamadı.")
            except sr.RequestError:
                durum_label.config(text="API hatası.")

    threading.Thread(target=arka_planda_ses_dinle).start()

def komut_analiz_et(komut):
    if "Google'da ara" in komut:
        arama_terimi = komut.replace("Google'da ara", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={arama_terimi}")
        durum_label.config(text=f"Google'da arama yapılıyor: {arama_terimi}")

    elif "çöp kutusunu boşalt" in komut:
        try:
            # Windows'ta çöp kutusunu boşaltmak için PowerShell komutu
            os.system("powershell.exe -command \"Clear-RecycleBin -Force\"")
            durum_label.config(text="Çöp kutusu boşaltıldı.")
        except Exception as e:
            durum_label.config(text="Bir hata oluştu: " + str(e))

    elif "masaüstünde" in komut and "aç" in komut:
        uygulama_adi = komut.split("masaüstünde")[1].split("aç")[0].strip()
        masaustu_yolu = os.path.join(os.path.expanduser("~"), "Desktop")
        
        dosya_bulundu = False
        for dosya in os.listdir(masaustu_yolu):
            if uygulama_adi.lower() in dosya.lower() and dosya.endswith(".lnk"):
                os.startfile(os.path.join(masaustu_yolu, dosya)) 
                durum_label.config(text=f"{uygulama_adi} açılıyor.")
                dosya_bulundu = True
                break

        if not dosya_bulundu:
            durum_label.config(text=f"{uygulama_adi} masaüstünde bulunamadı.")
    else:
        durum_label.config(text="Komut anlaşılamadı.")

# Tkinter GUI ayarları
window = tk.Tk()
window.title("Sesli Asistan")
window.geometry("400x200")

durum_label = tk.Label(window, text="Sesli komutlar için 'Dinle' butonuna tıklayın.", wraplength=300)
durum_label.pack(pady=20)

dinle_button = tk.Button(window, text="Dinle", command=ses_dinle)
dinle_button.pack(pady=10)

window.mainloop()
