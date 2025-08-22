{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c8f1f17-944d-4940-8876-845fd8529548",
   "metadata": {},
   "outputs": [],
   "source": [
    "#String methods\n",
    "s1='apple'\n",
    "s2='mango'\n",
    "s3='Grapes'\n",
    "s4='    Hello    World     '\n",
    "s5='12345'\n",
    "s6='4 mango'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a691442-80c9-41f6-8e09-9264be552444",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Capitalize first letter\n",
    "print(s1.capitalize())\n",
    "print(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e0a8ac0-0d08-449c-897d-b20465a44a27",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Everything to upper case\n",
    "print(s1.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c799f8ea-9294-4734-9be9-8c782834131a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#lower case everything\n",
    "print(s3.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f940e6a-d6fd-4136-9c9f-17d8af941bd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#title\n",
    "print(s1.title())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "204543be-20b6-40fe-9047-1279ce975015",
   "metadata": {},
   "outputs": [],
   "source": [
    "#swapcase\n",
    "print(s3.swapcase())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0688ac92-aff3-48e4-a69d-9fa0994933de",
   "metadata": {},
   "outputs": [],
   "source": [
    "#strip, lstrip, rstrip\n",
    "print(f\"Remove space from left side:  {s4.lstrip()}\")\n",
    "print(f\"Remove space from left side:  {s4.rstrip()}\")\n",
    "print(f\"Remove space from left AND right side: {s4.strip()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7081f484-f517-47c3-93a2-c7fef903b0ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "#split\n",
    "print(s4.split())\n",
    "print(s4.split(\",\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2585a79-fea1-42d1-b0ec-2e39fac60775",
   "metadata": {},
   "outputs": [],
   "source": [
    "#find\n",
    "print(s4.find(\"World\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30151f2b-f04e-431a-9603-0945eca41bd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#index\n",
    "print(s1.index('p'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea607082-a15d-40b8-ae4b-0537af090320",
   "metadata": {},
   "outputs": [],
   "source": [
    "#count\n",
    "print(s1.count('p'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28bc1311-a6b7-49df-83a1-871bcbd5e4ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "#isalpha\n",
    "print(s1.isalpha())\n",
    "print(s5.isalpha())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc85e621-be03-4798-b62e-b7607481522e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#isnum\n",
    "print(s5.isdigit())\n",
    "print(s4.isdigit())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8060c695-1f16-405e-997d-90752cee7af1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#isalnum\n",
    "print(s6.isalnum())\n",
    "print(s5.isalnum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54cbaf76-a8e9-44b0-bf63-0b8bf06abcb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#format\n",
    "name='manvi'\n",
    "profession='artist'\n",
    "print(\"My name is {}, and I am an {}.\".format(name,profession))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dde01d0d-564e-4ddc-9838-2d693c2f9484",
   "metadata": {},
   "outputs": [],
   "source": [
    "#calculator\n",
    "balance=100000\n",
    "pin=1234\n",
    "def withdrawal():\n",
    "    global balance\n",
    "    amount=int(input(\"Enter amount to withdraw\"))\n",
    "    if amount>(balance-1000):\n",
    "        print(\"Insufficient balance\")\n",
    "    else:\n",
    "        balance=balance-amount\n",
    "        print(f\"Amount withdrawn: {amount}\")\n",
    "        print(f\"New balance of account:{balance}\")\n",
    "def deposit():\n",
    "    global balance\n",
    "    depositamount=int(input(\"Enter amount to deposit\"))\n",
    "    balance=balance+depositamount\n",
    "    print(f\"New balance of account:{balance}\")\n",
    "def atm():\n",
    "    pin2=int(input(\"Enter pin\"))\n",
    "    if pin2==pin:\n",
    "        print(\"1.Withdrawal:         2.Deposit:\")\n",
    "        choice=int(input(\"Enter choice\"))\n",
    "        if choice==1:\n",
    "            withdrawal()\n",
    "        elif choice==2:\n",
    "            deposit()\n",
    "        else:\n",
    "            print(\"invalid choice.try again\")\n",
    "    else:\n",
    "        print(\"Incorrect pin\")\n",
    "atm()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6158b605-657d-4cbc-a79e-8c7769eb8b4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#test\n",
    "print(len(\"hello world\"))\n",
    "print(\"python\".upper())\n",
    "print(\"banana\".find(\"a\"))\n",
    "print(\" \".isspace())\n",
    "print(type({}))\n",
    "dict = {1: \"one\", 2: \"two\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7eda01d0-d350-4741-a97e-54f619e70dd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#File handling\n",
    "file=open(\"check.txt\",\"r\")\n",
    "content=file.read()\n",
    "print(content)\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8d881ee-83cb-4a58-98a4-5bf6984d60c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#check if file exists\n",
    "import os\n",
    "if os.path.exists(\"apple.txt\"):\n",
    "    os.remove(\"apple.txt\")\n",
    "else:\n",
    "    print(\"File doesn't exist\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e38aed45-543a-41aa-be0b-0ef3c0f819d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#create new file\n",
    "file=open(\"mangoes.txt\",\"x\")\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c8d0ecc-92ca-4c85-92ce-418deb06e83b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#write in file\n",
    "file=open(\"mangoes.txt\",\"w\")\n",
    "file.write(\"hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e4409ef-efa5-46c3-94cd-d86cd86f5fff",
   "metadata": {},
   "outputs": [],
   "source": [
    "#read from file\n",
    "file=open(\"mangoes.txt\",\"r\")\n",
    "content=file.read()\n",
    "print(content)\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57548181-e036-4072-ad3f-7232b8ce353d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#OOPS\n",
    "class car:\n",
    "    def __init__(self,brand,model):\n",
    "        self.brand=brand\n",
    "        self.model=model\n",
    "    def show(self):\n",
    "        print(f\"It is {self.model} from {self.brand} brand\")\n",
    "c=car(\"Toyota\",\"Innova\")\n",
    "c.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86ed18e2-971d-46e2-a41e-0a3abd3da856",
   "metadata": {},
   "outputs": [],
   "source": [
    "#ATM simulator using OOPS\n",
    "balance=100000\n",
    "class atm:\n",
    "    print(\"1.Withdrawal:         2.Deposit:\")\n",
    "    def func(self):\n",
    "        global balance\n",
    "        choice=int(input(\"Enter choice\"))\n",
    "        if choice==1:\n",
    "            amount=int(input(\"Enter amount to withdraw\"))\n",
    "            if amount>(balance-1000):\n",
    "                print(\"Insufficient balance\")\n",
    "            else:\n",
    "                balance=balance-amount\n",
    "                print(f\"Amount withdrawn: {amount}\")\n",
    "                print(f\"New balance of account:{balance}\")\n",
    "        elif choice==2:   \n",
    "            depo=int(input(\"Enter amount to deposit\"))\n",
    "            balance=balance+depo\n",
    "            print(f\"New balance of account:{balance}\")\n",
    "        else:\n",
    "            print(\"Invalid choice\")\n",
    "a=atm()\n",
    "a.func()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f77da80-04a0-4ade-976b-d42c9381bf1d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ce0c9754-324c-4d6d-9c94-2a3e4cbeace0",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'apple.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m file\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mapple.txt\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mr\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      2\u001b[0m content\u001b[38;5;241m=\u001b[39mfile\u001b[38;5;241m.\u001b[39mread()\n",
      "File \u001b[0;32m/opt/anaconda3/lib/python3.13/site-packages/IPython/core/interactiveshell.py:324\u001b[0m, in \u001b[0;36m_modified_open\u001b[0;34m(file, *args, **kwargs)\u001b[0m\n\u001b[1;32m    317\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[1;32m    318\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[1;32m    319\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    320\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    321\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    322\u001b[0m     )\n\u001b[0;32m--> 324\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'apple.txt'"
     ]
    }
   ],
   "source": [
    "file=open(\"apple.txt\",\"r\")\n",
    "content=file.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "631de6ab-258f-4b22-bd0f-5962780be553",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file=open(\"mangoes.txt\",\"r\")\n",
    "content=file.read()\n",
    "f=open(\"check.text\",\"w\")\n",
    "f.write(content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1b6ac6d-f63b-4c59-aa5e-2c301e30b431",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
