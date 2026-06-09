import os
import gc
import psutil


def execute_system_ram_cleanup() -> float:
    """
    Forces garbage collection within LapPulse and purges the working sets
    of accessible processes on Windows to free up system-wide memory.
    
    Returns:
        float: Reclaimed system memory in Megabytes (MB).
    """
    before_mem = psutil.virtual_memory().available

    gc.collect()

    if os.name == 'nt':
        try:
            import ctypes
            ctypes.windll.psapi.EmptyWorkingSet(-1)
        except Exception as win_err:
            print(f"Windows memory optimization subsystem warning: {win_err}")

    after_mem = psutil.virtual_memory().available
    bytes_freed = max(0, after_mem-before_mem)
    return bytes_freed/(1024*1024)
