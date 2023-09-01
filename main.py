import smtplib#eposta sağlayıcısına ulaşmak için kullanılıyor örnek:gmail,hotmail biz gmail kullanıcaz
import ssl#bu ssl bizim bilgilerimizi yani eposta ve şifremizi encode ediyor

discord="dao026"
email = "<mail adresi>"#burda mailmizi yazıyoruz
password = "<uygulama şifresi>"#readme kısmını okuyunuz

alici=email#kime gönderdiğimiz

mesaj="Merhaba"#mesajımız

context=ssl.create_default_context()#burda ssl ile smtp güvenli bir bağlantı oluşturuyoruz yani burda bizim şifrelerimizi encode ediyor

port=465#gmail smtp bağlanma portu
host="smtp.gmail.com"#gmail smtp bağlanma hostu


eposta=smtplib.SMTP_SSL(host=host,port=port,context=context)#burda bağlantıyı oluşturduk

eposta.login(email,password)#login oluyoruz
eposta.sendmail(email,alici,mesaj)#son olarak mail gönderiyoruz

