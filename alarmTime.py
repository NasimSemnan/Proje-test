import time
import platform
from datetime import datetime, timedelta

# اگر سیستم عامل ویندوز باشد، winsound را وارد کن
if platform.system() == "Windows":
    import winsound
else:
    print("faghat dar windows seday booogh mide")


def pashooo():
    now = datetime.now()
    try:
        wakeup_time = input("s@t bidar shodan vared kon(07:03)")
        wakeup_date_time = datetime.strptime(wakeup_time, "%H:%M").time()
    except ValueError:
        print("b in sorat varet kon HH:MM")
        return None

    wakeup = datetime.combine(now.date(), wakeup_date_time)

    if wakeup < now:
        wakeup += timedelta(days=1)

    tim_bidar_bash = wakeup - now
    print(f"zaman baghi mande bidar shodan : {tim_bidar_bash}")
    time.sleep(tim_bidar_bash.total_seconds())
    print("bidar shoooo azizaaam")

    return True


def start_beep(count):
    if platform.system() == "Windows":
        for _ in range(count):
            winsound.Beep(2500, 1000)
            print("wake up!")
    else:
        for _ in range(count):
            print("🔔 wake up!")  # برای سیستم‌های غیر ویندوز


# گرفتن تعداد بوق‌ها
try:
    count = int(input("tedad booogh vared kon "))
except ValueError:
    print("addd vared nashode! ")
    count = 3  # مقدار پیش‌فرض

# اجرای برنامه
if pashooo():
    start_beep(count)
