from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QFrame, QProgressBar
from PyQt6.QtCore import QTimer, Qt
from lappulse.core.hardware import HardwareMonitor

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.monitor = HardwareMonitor()
        self.init_ui()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_dashboard)
        self.timer.start(1000) # හැම තත්පරයකටම Update කරමු (Faster & Smoother)

    def init_ui(self):
        self.setWindowTitle("LapPulse v1.0 Pro")
        self.setFixedSize(400, 550) 

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(18)

        # 1. App Title
        title_label = QLabel("⚡ LapPulse Pro")
        title_label.setObjectName("MainTitle")
        main_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignLeft)

        # 2. Battery Card
        self.battery_card = QFrame()
        self.battery_card.setObjectName("Card")
        bat_layout = QVBoxLayout(self.battery_card)
        # bat_layout.setMargins(QProgressBar().contentsMargins())
        bat_layout.setContentsMargins(15, 15, 15, 15)
        
        bat_title = QLabel("Battery Status")
        bat_title.setObjectName("CardTitle")
        self.bat_value = QLabel("--%")
        self.bat_value.setObjectName("CardValue")
        
        # 🔋 Battery Progress Bar එක
        self.bat_bar = QProgressBar()
        self.bat_bar.setValue(0)
        
        bat_layout.addWidget(bat_title)
        bat_layout.addWidget(self.bat_value)
        bat_layout.addWidget(self.bat_bar)
        main_layout.addWidget(self.battery_card)

        # 3. Charger Status Card
        self.charger_card = QFrame()
        self.charger_card.setObjectName("Card")
        char_layout = QVBoxLayout(self.charger_card)
        
        char_title = QLabel("Power Source")
        char_title.setObjectName("CardTitle")
        self.char_value = QLabel("Checking...")
        self.char_value.setObjectName("StatusActive")
        
        char_layout.addWidget(char_title)
        char_layout.addWidget(self.char_value)
        main_layout.addWidget(self.charger_card)

        # 4. CPU Usage Card
        self.cpu_card = QFrame()
        self.cpu_card.setObjectName("Card")
        cpu_layout = QVBoxLayout(self.cpu_card)
        
        cpu_title = QLabel("CPU Load")
        cpu_title.setObjectName("CardTitle")
        self.cpu_value = QLabel("--%")
        self.cpu_value.setObjectName("CardValue")
        
        # 📈 CPU Progress Bar එක
        self.cpu_bar = QProgressBar()
        self.cpu_bar.setValue(0)
        
        cpu_layout.addWidget(cpu_title)
        cpu_layout.addWidget(self.cpu_value)
        cpu_layout.addWidget(self.cpu_bar)
        main_layout.addWidget(self.cpu_card)

    def update_dashboard(self):
        metrics = self.monitor.get_system_metrics()
        
        # Text සහ Progress Bars අප්ඩේට් කිරීම
        self.bat_value.setText(f"{metrics['battery_percent']}%")
        self.bat_bar.setValue(metrics['battery_percent'])
        
        self.cpu_value.setText(f"{metrics['cpu_usage']}%")
        self.cpu_bar.setValue(int(metrics['cpu_usage']))
        
        if metrics['is_plugged']:
            self.char_value.setText("⚡ PLUGGED IN (Direct AC Power)")
            self.char_value.setStyleSheet("color: #34D399;") # Premium Green
        else:
            self.char_value.setText("🔋 BATTERY MODE (Discharging)")
            self.char_value.setStyleSheet("color: #FB923C;") # Premium Orange