export LANG=C.UTF-8

echo -e "\nMengecek Data...\n"

if command -v python3 >/dev/null 2>&1 ; then
    echo -e "python3 found "
    echo -e "version: $(python3 -V)"
else
    echo -e "python not found "
    if [ "$(command -v pkg)" != "" ]; then
        arr+=(python ) #termux python3 is in python
    else
        arr+=(python3 )
    fi
fi

sleep 1

if command -v wget >/dev/null 2>&1 ; then
    echo -e "\nwget found\n"
else
    echo -e "\nwget not found\n"
    arr+=(wget )
fi

DEPENDENCIES=${arr[@]}
sleep 1

if [ ! -z "$DEPENDENCIES" ]; then
    echo -e "\nInstalling required dependencies\n"
    sleep 1

    if [ "$(command -v pkg)" != "" ]; then # termux
        pkg install "$DEPENDENCIES" -y

    elif [ "$(command -v apt-get)" != "" ]; then # debian
        sudo apt-get install "$DEPENDENCIES" -y

    elif [ "$(command -v pacman)" != "" ]; then # arch
        sudo pacman -S "$DEPENDENCIES" -y

# Free to PR to add others
    else
        echo -e "\nDistro not supported \nInstall this packages yourself: $DEPENDENCIES\n"
    fi

else
    echo -e "\nDependencies have been installed. \nContinuing to install python packages(PyPI)\n"
    sleep 1
fi

echo -e "\nUpgrading python pip\n"
pip3 install --upgrade pip setuptools
echo -e "\nMenginstall telethon...\n"
pip3 install telethon
sleep 2

if [ ! -e string_session.py ]; then
    echo -e "\nDownloading string_session.py\n"
    wget https://raw.githubusercontent.com/aldoaprilyan3/One-Piece/One-Piece/string_session.py

    echo -e "\nMenjalankan Script...\n"
    sleep 1
    python3 string_session.py
else
    echo -e "\nstring_session.py detected... \nrunning file\n"
    sleep 1
    python3 string_session.py
fi

echo -e "Apakah Anda ingin membersihkan file Anda?"
echo -e "[1] cleanup: hapus ini string_session.py dan ini "
echo -e "[2] exit : dan ini untuk keluar saja namun tidak menghapus string"
echo -ne "\nTentukan Pilihanmu[1-2]: "
read choice
if [ "$choice" = "1" ]; then
    echo -e "Cleanup: menghapus file"
    rm -f string_session.py Getstring.sh
elif [ "$choice" = "2" ]; then
    exit
fi
