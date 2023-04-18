import pywhatkit
import pandas as pd

dataset = pd.read_csv("GDSC AASTMT-Cairo ML Track.csv")
whatsapp_numbers = dataset.iloc[:,3].values

msg= """Congratulations🎊🎊, 
You are accepted into Machine Learning Track🤖.

Best of Luck ✨
"""
for i in whatsapp_numbers:
    pywhatkit.sendwhatmsg_instantly("+20"+str(int(i)),msg,10,tab_close=True)
