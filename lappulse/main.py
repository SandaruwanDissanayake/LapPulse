import sys
from PyQt6.QtWidgets import QApplication
# 🚨 මෙන්න මේ ලයින් එක තමයි නිවැරදි එක! ui/dashboard එකෙන් ගන්න ඕනේ:
from lappulse.ui.dashboard import DashboardWindow

def main():
    # 1. PyQt6 Application එක Initialize කරනවා
    app = QApplication(sys.argv)
    
    # 2. අපි ලියාගත්ත styles.qss එක කියවලා App එකට CSS සෙට් කරනවා
    try:
       with open("lappulse/ui/style.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Style sheet not found, running with default theme.")

    # 3. අපේ Dashboard Window එක Object එකක් විදිහට හදලා පෙන්වනවා
    window = DashboardWindow()
    window.show()
    
    # 4. App එකේ Event Loop එක දිගටම රන් කරනවා (User වහනකම්)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()