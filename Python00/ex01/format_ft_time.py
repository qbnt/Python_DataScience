import datetime
import time


date = datetime.date.today()
formatedDate = date.strftime("%b %d %Y")

hour = time.gmtime()

print(f"Seconds since January 1, 1970: {time.time():.2f} \
      or {time.time():.2e} in scientific notation")
print(f"{formatedDate}")
