import psutil

class HardwareMonitor:
    def __init__(self):
        # Java වල Constructor එක වගේ තමයි මේ __init__ එක
        pass

    def get_system_metrics(self):
        # 1. බැටරි විස්තර ලබා ගැනීම
        battery = psutil.sensors_battery()
        battery_pct = battery.percent if battery else 0
        is_plugged = battery.power_plugged if battery else False
        
        # 2. CPU පාවිච්චිය (%)
        # interval=None දැම්මම background එකේ block නොවී ක්ෂණිකව usage එක දෙනවා
        cpu_usage = psutil.cpu_percent(interval=None)
        
        # Java වල HashMap එකක් හෝ DTO (Data Transfer Object) එකක් return කරනවා වගේ
        # Python වල ලේසියෙන්ම Dictionary (Key-Value) එකක් return කරන්න පුළුවන්
        return {
            "battery_percent": battery_pct,
            "is_plugged": is_plugged,
            "cpu_usage": cpu_usage
        }