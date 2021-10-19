# code by : AriefDev
# usr/bin/python
import os,sys,time

# ------------- color -----------
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;36m"
w = "\033[1;37m"
w1 = "\033[0;37m"


def logo():
	os.system("reset")
	banner = """
\033[0;31m█████████\033[1;33m      ●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[0;31m█▄█████▄█\033[1;36m __--╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗
\033[0;31m█\033[1;32m ▼▼▼▼▼\033[1;36m_---_--║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝
\033[0;31m█\033[1;36m   --_-- --_ ║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗
\033[0;37m█\033[1;32m ▲▲▲▲▲\033[1;36m -_-- -╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝
\033[0;37m█████████\033[1;33m      «°°°°°°°°°°✧°°°°°°°°°°»
\033[0;37m ██ ██
\033[0;31m
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;33m
<\> code by : \033[4;32mAriefDev\033[0m\033[1;33m
<\> team    : \033[4;32mBorneoExploit\033[0m\033[1;33m
<\> github  : \033[4;32mhttps://github.com/BorneoExploit\033[0m\033[1;31m
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
	print (banner)

def loading(e):
	for a in e + "\n":
		sys.stdout.flush()
		sys.stdout.write(a)
		time.sleep(000.01)
def start():
	logo()
	print ("\033[0m")
	print ("[01].install package")
	print ("[02].start")
	print ("[03].more tools")
	print ("[04].Exit/Close")
	print ("")
	try:
		menu = input(r+"["+g+"•"+r+"]"+w+" choose >> ")
		if menu == "1" or menu == "01":
			install()
		elif menu == "2" or menu == "02":
			main()
		elif menu == "3" or menu == "03":
			os.system("xdg-open 'https://github.com/BorneoExploit'")
		elif menu == "4" or menu == "04":
			print (r+"["+g+"•"+r+"]"+w+" Exit/Close ...")
			sys.exit()
	except KeyboardInterrupt:
		print ("[\033[41m%s\033[0m] KeyboardInterrupt .. " % (time.strftime("%X")))
		sys.exit()
def data():
	print ("—————————————————————————————————")
	print ("\33[1;31m ISI DATA DI BAWAH INI :\033[0m")
	print ("—————————————————————————————————")

def install():
	loading(r+"["+g+"√"+r+"]"+w+" install package ...\033[0m")
	os.system("pkg update  && pkg upgrade  && pkg install figlet cowsay toilet")
	start()
def main():
	logo()
	print ("\033[0m")
	f = """
╔═ •~≽ 01.Redskull
║
╠═ •~≽ 02.Dragon
║
╠═ •~≽ 03.Skull
║
╠═ •~≽ 04.Name
║
╠═ •~≽ 05.BlackHat
║
╠═ •~≽ 06.DarkFb
║
╠═ •~≽ 07.Anonymous
║
╠═ •~≽ 08.Termux
║
║
╚═ •~≽ 00.Back

"""
	print (f)
	menu = input("[choose]•~≽ ")
	if menu == "1" or menu == "01":
		redskull()
	elif menu == "2" or menu == "02":
		dragon()
	elif menu == "3" or menu == "03":
		skull()
	elif menu == "4" or menu == "4":
		name()
	elif menu == "5" or menu == "05":
		blackhat()
	elif menu == "6" or menu == "06":
		darkfb()
	elif menu == "7" or menu == "7":
		anonymous()
	elif menu == "8" or menu == "08":
		termux()
def redskull():
	data()
	autor = input("[•] Nama Di Autor •~≽ ")
	terminal = input("[•] Nama Di Terminal •~≽ ")
	print ("———————————————————————————————————")
	if autor == "":
		print ("[x] Data/Formulir Tidak Boleh Kosong ")
	if terminal == "":
		print ("[x] Data/Formulir Tidak Boleh Kosong ")
	code = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
clear
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit
echo '\033[1;31m         @@@@@                                        @@@@@'
echo '        @@@@@@@                                      @@@@@@@'
echo '        @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@'
echo '         @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@'
echo '             @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@'
echo '               @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@'
echo '                 @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@'
echo '                    @@@@@@@    @@@@@@    @@@@@@'
echo '                    @@@@@@      @@@@      @@@@@'
echo '                    @@@@@@      @@@@      @@@@@'
echo '                     @@@@@@    @@@@@@    @@@@@'
echo '                      @@@@@@@@@@@  @@@@@@@@@@'
echo '                       @@@@@@@@@@  @@@@@@@@@'
echo '                    @@   @@@@@@@@@@@@@@@@@   @@'
echo '                   @@@@  @@@@ @ @ @ @ @@@@  @@@@'
echo '                  @@@@@   @@@ @ @ @ @ @@@   @@@@@'
echo '                @@@@@      @@@@@@@@@@@@@      @@@@@'
echo '              @@@@          @@@@@@@@@@@          @@@@'
echo '           @@@@@              @@@@@@@              @@@@@'
echo '          @@@@@@@                                 @@@@@@@'
echo '           @@@@@                                   @@@@@ \033[0m'
echo ''
echo '                       =[ Coded by : \033[4;33m%s\033[0m ]='
echo '                     ====[ \033[41mWelcome To Termux\033[0m ]===='
echo '\n'
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (autor,terminal)

	file = open("bash.bashrc","w")
	file.write(code)
	file.close()
	os.system("mv bash.bashrc /$HOME/../usr/etc && bash")
def dragon():
	data()
	autor = input("[•] Nama Autor •~≽ ")
	if autor == "":
		print ("[x] Data Tidak Boleh Kosong ..")
	terminal = input("[•] Nama di terminal •~≽ ")
	if terminal == "":
                print ("[x] Data Tidak Boleh Kosong ..")
	file = open("bash.bashrc","w")
	code = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit
clear
echo '\033[1;31m		            ______________'
echo '                ,===:.,            `-._'
echo '                `:.`---.__         `-._'
echo '                  `:.     `--.         `.'
echo '                  `:.     `--.         `.'
echo '            (,,(,    \.         `.   ____,-`.,'
echo '         (,      `/   \.   ,--.___`.\033[1;37m'
echo '     ,  ,  ,--.   `,   \. ;`'
echo '      `{%sD%s,{     \  :    \ ;'
echo '        V,,     /  /    //'
echo '        j;;    /  ,  ,-//.    ,---.      ,'
echo '        \;    /  ,  /  _  \  /  _  \   , /'
echo '              \   `   / \  `   / \  `.  /'
echo '               `.___,/   `.__,/   `.__,/\033[0m'
echo ''
echo '                    =[ Coded by : \033[4;33m%s\033[0m ]='
echo '                  ====[ \033[41mWelcome To Termux\033[0m ]===='
echo '\n'
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (b,w1,autor,terminal)
	file.write(code)
	file.close()
	os.system("mv bash.bashrc /$HOME/../usr/etc && bash")
def skull():
	data()
	autor = input("[•] Nama Di Bagian Autor •~≽ ")
	if autor == "":
                print ("[x] Data Tidak Boleh Kosong ..")
	terminal = input("[•] Nama Di Terminal •~≽ ")
	if terminal == "":
                print ("[x] Data Tidak Boleh Kosong ..")
	file = open("bash.bashrc","w")
	dev = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit
clear
echo -e "\033[0;37m"
echo -e '                       .:::!~!!!!!:.'
echo -e '                    .xUHWH!! !!?M88WHX:.'
echo -e '                  .X*#M@&!!  !X!M&&&&&&WWx:.'
echo -e '                 :!!!!!!?H! :!&!&&&&&&&&&&8X:'
echo -e '                !!~  ~:~!! :~!&!#&&&&&&&&&&8X:'
echo -e '               :!~::!H!<   ~.U&X!?R&&&&&&&&MM!'
echo -e '               ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!'
echo -e '                 !:~~~ .:!MST#&&&&WX??#MRRMMM!'
echo -e '                 ~?WuxiW*`   `√#&&&&8!!!!??!!!'
echo -e '               :X- M&&&&       `rT#&T~!8&WUXU~'
echo -e '              :%`  ~#&&&m:    \033[1;31m✪\033[0;37m   ~!~ ?&&&&&&'
echo -e '            :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&'
echo -e ' .......   -~~:<` !    ~?T#&&@@W@*?&&   \033[1;31m✪\033[0;37m  /`'
echo -e '\033[1;32mG\033[0;37m |W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :'
echo -e '\033[1;32mH\033[0;37m |#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`'
echo -e '\033[1;32mO\033[0;37m |:::~:!!`:X~ .: ?H.!u °&&&B&&&!W:U!T&&M~'
echo -e '\033[1;32mS\033[0;37m .~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `'
echo -e '\033[1;32mT\033[0;37m Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!'
echo -e ' .......         /   ~&&&&&B&&en:``'
echo -e '                     ~`##*&&&&M~'
echo -e '\n'
"""
	try:
		code = """
echo -e '\033[1;37m                  =[ Coded by : \033[4;33m%s\033[0m]='
echo -e '\033[1;37m                ====[ \033[41mWelcome To Termux\033[0m]===='
echo '\n'
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (autor,terminal)
		file.write(dev)
		file.write(code)
		file.close()
		os.system("mv bash.bashrc /$HOME/../usr/etc && bash")
	except ValueError:
		print ("Error.....")


def name():
	data()
	banner = input("[•] text figlet  •~≽ ")
	if banner == "":
		print ("[x] Data Tidak Boleh Kosong ...")
	terminal = input("[•] Nama Di Terminal •~≽ ")
	if terminal == "":
		print ("[x] Data Tidak Boleh Kosong ...")
	print ("——————————————————————————————————")
	file = open("bash.bashrc","w")
	code = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit
clear
figlet %s | lolcat
echo -e "\033[1;33m————————————————————"
echo -e "[\033[41mWelcome To Termux\033[0m\033[1;33m]"
echo -e "\033[1;33m————————————————————"
echo -e ""
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (banner,terminal)
	file.write(code)
	file.close()
	os.system("mv bash.bashrc /$HOME/../usr/etc && bash")

def blackhat():
	data()
	autor = input("[•] Nama Autor •~≽ ")
	if autor == "":
		print ("[x] Data Tidak Boleh Kosong ...")
	terminal = input("[•] Nama Di Terminal •~≽ ")
	if terminal == "":
		print ("[x] Data Tidak Boleh Kosong ...")


	file = open("bash.bashrc","w")
	code = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
clear
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit
echo -e   "\033[1;32m ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀    ██░ ██  ▄▄▄     ▄▄▄█████▓"
echo -e   " ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒    ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒"
echo -e   " ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░"
echo -e   " ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░"
echo -e   " ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░"
echo -e   " ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░"
echo -e   " ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░   ░"
echo -e   "  ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░     ░  ░░ ░  ░   ▒    ░\033[0m"
echo -e   "\n"
echo -e   "                  =[ Coded by \033[4;33m%s\033[0m ]="
echo -e   "               ====[ \033[41mWelcome To Termux\033[0m ]====\n"
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (autor,terminal)
	file.write(code)
	file.close()
	os.system("mv bash.bashrc /$HOME/../usr/etc && bash")
def darkfb():
	data()
	autor = input("[•] Nama Autor •~≽ ")
	terminal = input("[•] Terminal •~≽ ")
	if autor == "":
		print ("[x] Data Tidak Boleh Kosong ...")
		time.sleep(1)
		darkfb()
	if terminal == "":
		print ("[x] Data Tidak Boleh Kosong ...")
		time.sleep(1)
		darkfb()
	code = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
clear
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit
echo -e "\033[1;31m █████████\033[1;33m      ●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●"
echo -e "\033[1;31m █▄█████▄█\033[1;31m __--╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗"
echo -e "\033[1;31m █\033[0;36m ▼▼▼▼▼\033[1;31m_---_--║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝"
echo -e "\033[1;31m █   \033[1;31m--_-- --_ ║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗"
echo -e "\033[1;37m █\033[0;36m ▲▲▲▲▲ \033[1;31m-_-- -╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝"
echo -e "\033[1;37m █████████\033[1;33m      «°°°°°°°°°°✧°°°°°°°°°°»"
echo -e "\033[1;37m   ██ ██"
echo -e "\033[1;373m ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m"
echo -e ""
echo -e "     =[ Coded by \033[4;33m%s\033[0m ]="
echo -e "  ====[ \033[41mWelcome To Termux\033[0m ]===="
echo "\n"
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (autor,terminal)
	file = open("bash.bashrc","w")
	file.write(code)
	file.close()
	os.system("mv bash.bashrc /$HOME/../usr/etc && bash")
def anonymous():
	data()
	autor = input("[•] Nama Autor •~≽ ")
	terminal = input("[•] Nama Di Terminal •~≽ ")
	code = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit
clear
echo '\033[1;31m                        `/ymMMMMMMMMmy/`'
echo '                    `/ymMMMMMMMMMMMMMMmy/`' 
echo '                   /hMMMMMMMMMMMMMMMMMMMMMMh/'
echo '                 /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/'
echo '               `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`'
echo '              .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.'
echo '             `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`'
echo '             ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys'
echo '            `my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`'
echo '            -h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-^\033[1;37m'
echo '            -N.o.sMmMMMNh/:-`-MosM-`-:/hNMMMmMs.+.N-'
echo '            `ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh'
echo '             s+-s-odmNNN`     /-:/     .NNNmd+:s-+s'
echo '             `mo/-:+ymMm                mMms+:-/om`'
echo '              .h/+/y`hhs                yyh`y/+/h.'
echo '               `hd/::-+.                .+-::/dy`'
echo '                 /hs+/::.--          --.::/+sh:'
echo '                   :hds+/-`          `-/+sdh:'
echo '                     `/ymM+          oMmy:'
echo '                         \033[41m W E L C O M E \033[0m'
echo '\n'
echo '\033[0m                     =[ Coded by \033[4;32m%s\033[0m ]='
echo '\033[0m                 ====[ \033[41mAnonymous Indonesia\033[0m ]===='
echo ''
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (autor,terminal)
	file = open("bash.bashrc","w")
	file.write(code)
	file.close()
	os.system("mv bash.bashrc /$HOME/../usr/etc && bash")
def termux():
	data()
	autor = input("[•] Nama Autor •~≽ ")
	terminal = input("[•] Nama Terminal •~≽ ")
	if autor == "":
		print ("[x] Data Tidak Boleh Kosong ")
		time.sleep(1)
		termux()
	if terminal == "":
		print ("[x] Data Tidak Boleh Kosong ")
		time.sleep(1)
		termux()
	code = """if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
clear
#  autor  : AriefDev
#  team   : BorneoExploit
#  github : https://github.com/BorneoExploit

echo -e "\033[1;31m      ████████ ███████ ██████  ███    ███ ██    ██ ██   ██ "
echo -e "         ██    ██      ██   ██ ████  ████ ██    ██  ██ ██  "
echo -e "         ██    █████   ██████  ██ ████ ██ ██    ██   ███  "
echo -e "         ██    ██      ██   ██ ██  ██  ██ ██    ██  ██ ██ "
echo -e "         ██    ███████ ██   ██ ██      ██  ██████  ██   ██ \033[0m"
echo -e "\n"
echo -e "		     =[ Coded by: \033[4;33m%s\033[0m ]="
echo -e "                 ===[ \033[41mWelcome To Termux\033[0m ]==\n"
PS1='\033[1;34m\]╭───\[\033[1;31m\]≼\[\033[1;33m\]%s\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\]≽
\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '
""" % (autor,terminal)
	file = open("bash.bashrc","w")
	file.write(code)
	file.close()
	os.system("mv bash.bashrc /$HOME/../usr/etc && bash")
start()
