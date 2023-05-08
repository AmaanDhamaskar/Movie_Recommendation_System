import smtplib
from email.message import EmailMessage
import sqlite3
from recTopPicks import recTop
import pandas as pd
import schedule
import time


def mail():
    conn = sqlite3.connect("AccountSystem1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT EMAIL FROM AccountDB")
    listmail2 = cursor.fetchall()
    listmail = []
    for i in listmail2:
        listmail.append(i[0])
    print(listmail)
    for i in listmail:
        df = pd.read_csv("refinedMovies.csv", index_col=0)
        movlist = recTop(i)
        print(movlist)
        ratinglist = []
        namelist = []
        posterlist = []
        for j in range(0, 5):
            ratingmail = df.loc[movlist[j]]["vote_average"]
            titlemail = df.loc[movlist[j]]["title"]
            postermail = "https://image.tmdb.org/t/p/original" + \
                df.loc[movlist[j]]["poster_path"]
            ratinglist.append(ratingmail)
            namelist.append(titlemail)
            posterlist.append(postermail)

        print(posterlist)
        subject = "Hey ! You Might Like This"
        sender = "moviesmailing@gmail.com"
        password = "kepeacjuarbhlofv"
        recipients = [i]

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients

        htmlcontent = '''
        <!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:#eee;padding:10px 20px;">
                    <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">Here Are Your Top 5 Recommendations For This Week</h2>
                </div>
                <div style="padding:20px 0px">
                    <div style="height: 700px;width:400px">
                        <img src={posterlist0} height= "500">
                        <div style="text-align:center;">
                            <h3>{namelist0}</h3>
                            <p>Rating : {ratinglist0}</p>
                        </div>
                    </div>
                    <div style="height: 700px;width:400px">
                        <img src={posterlist1} height= "500">
                        <div style="text-align:center;">
                            <h3>{namelist1}</h3>
                            <p>Rating : {ratinglist1}</p>
                            
                        </div>
                    </div>
                    <div style="height: 700px;width:400px">
                        <img src={posterlist2} height= "500">
                        <div style="text-align:center;">
                            <h3>{namelist2}</h3>
                            <p>Rating : {ratinglist2}</p>
                            
                        </div>
                    </div>
                    <div style="height: 700px;width:400px">
                        <img src={posterlist3} height= "500">
                        <div style="text-align:center;">
                            <h3>{namelist3}</h3>
                            <p>Rating : {ratinglist3}</p>
                            
                        </div>
                    </div>
                    <div style="height: 700px;width:400px">
                        <img src={posterlist4} height= "500">
                        <div style="text-align:center;">
                            <h3>{namelist4}</h3>
                            <p>Rating : {ratinglist4}</p>
                            
                        </div>
                    </div>
                </div>
            </body>
        </html>
        '''.format(posterlist0=posterlist[0], namelist0=namelist[0], ratinglist0=ratinglist[0], posterlist1=posterlist[1], namelist1=namelist[1], ratinglist1=ratinglist[1], posterlist2=posterlist[2], namelist2=namelist[2],
                   ratinglist2=ratinglist[2], posterlist3=posterlist[3], namelist3=namelist[3], ratinglist3=ratinglist[3], posterlist4=posterlist[4], namelist4=namelist[4], ratinglist4=ratinglist[4])
        msg.set_content(htmlcontent, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)


# schedule
schedule.every().monday.at("10:00").do(mail)


while True:
    schedule.run_pending()
    time.sleep(1)
# mail()
