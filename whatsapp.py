import pywhatkit
import datetime



#pywhatkit.sendwhatmsg_instantly('+972526843070','This is a bot message', wait_time=5)

now = datetime.datetime.now()
pywhatkit.sendwhatmsg('+972542526124','This is a bot message',now.hour,now.minute+1, tab_close=True, close_time=1)

