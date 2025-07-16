{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f9f1bd61-f406-4fb7-8815-2ee67a0aa59d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4x1=4\n",
      "4x2=8\n",
      "4x3=12\n",
      "4x4=16\n",
      "4x5=20\n",
      "4x6=24\n",
      "4x7=28\n",
      "4x8=32\n",
      "4x9=36\n",
      "4x10=40\n"
     ]
    }
   ],
   "source": [
    "#while loop\n",
    "num=int(input(\"Enter a number\"))\n",
    "i=1\n",
    "while i<=10:\n",
    "    print(f\"{num}x{i}={num*i}\")\n",
    "    i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0b653ae-470b-4434-acce-676056a2b692",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exit from while loop\n",
    "while True:\n",
    "    x=input(\"Enter a letter\")\n",
    "    if x=='q':\n",
    "        print(\"Exited loop\") \n",
    "        break\n",
    "    else:\n",
    "        print(\"You typed:\", x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2accf2aa-ee87-4d89-b29d-bc22ef721e64",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Three attempts\n",
    "password='open'\n",
    "attempts=3\n",
    "while attempts>0:\n",
    "    x=input(\"Enter password\")\n",
    "    if x=='open':\n",
    "        print(\"Login\")\n",
    "        break\n",
    "    else:\n",
    "        attempts-=1\n",
    "        print(f\"Wrong password:{attempts} attempts left\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "832879bf-f629-45ba-9b65-099e915c0854",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Numbers divisible by 7\n",
    "num=1\n",
    "print(\"Numbers divisible by 7 between 1 and 100 are:\")\n",
    "while num<=100:\n",
    "    if num%7==0:\n",
    "        print(num)\n",
    "    num+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae661443-3233-4e86-bc0d-53238adeb366",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for loop using range\n",
    "for i in range(1,6):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6482eb0-0dc5-4fee-83ee-c207232cde61",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for loop using range\n",
    "num=int(input(\"Enter a number\"))\n",
    "for i in range(1,11):\n",
    "    print(f\"{num}x{i}={num*i}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe5b6543-bc63-4d40-8745-b4528cadba5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Three attempts using for loop\n",
    "password='open'\n",
    "attempt=3\n",
    "for attempts in range(3):\n",
    "    x=input(\"Enter password\")\n",
    "    if x=='open':\n",
    "        print(\"Login\")\n",
    "        break\n",
    "    else:\n",
    "        print(f\"Wrong password:{2-attempts} attempts left\")\n",
    "        attempts-=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "104173b1-f9e9-4e92-920c-757c4abf50c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#continue statement\n",
    "for i in range(1,6):\n",
    "    if i==3:\n",
    "        continue\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9226efc7-9b34-4bfa-9c70-07ed6a1da0bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#continue and break statement\n",
    "for i in range(1,11):\n",
    "    if i==5:\n",
    "        continue\n",
    "    elif i==8:\n",
    "        break\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc7b38f8-5b54-4a98-9d6f-4b78910f8b8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Five attempts using continue and break\n",
    "password='open'\n",
    "attempt=5\n",
    "for attempts in range(6):\n",
    "    x=input(\"Enter password\")\n",
    "    if x=='open':\n",
    "        print(\"Login\")\n",
    "        break\n",
    "    elif x=='Forgot password':\n",
    "            attempts-=1\n",
    "            continue\n",
    "    else:\n",
    "        print(f\"Wrong password:{4-attempts} attempts left\")\n",
    "        attempts-=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d517ab8a-9491-44ed-a274-d7ea4d93d652",
   "metadata": {},
   "outputs": [],
   "source": [
    "#continue and break statement\n",
    "lang=\"Python programming\"\n",
    "i=lang[0]\n",
    "for i in range (len(lang)):\n",
    "    if lang[i]=='o':\n",
    "        continue\n",
    "    elif lang[i]=='n':\n",
    "        break\n",
    "    else:\n",
    "        print(lang[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5efaf907-ced9-4eed-86cc-329a24b2a605",
   "metadata": {},
   "outputs": [],
   "source": [
    "#User defined function\n",
    "def apple():\n",
    "    print(\"Hello\")\n",
    "apple() #calling teh function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bda57290-a2a6-41cb-b563-e2b1bfcba5af",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function to add two numbers\n",
    "def mango(a,b):\n",
    "    c=a+b\n",
    "    print(f\"The sum of {a},{b} is {c}\")\n",
    "\n",
    "mango(5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5fa3355b-5307-4c73-8d82-bc40d67c6a45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "M\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "string index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[4], line 7\u001b[0m\n\u001b[1;32m      5\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mreversed\u001b[39m[index]\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      6\u001b[0m         index\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m\n\u001b[0;32m----> 7\u001b[0m rev(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mManvi\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "Cell \u001b[0;32mIn[4], line 5\u001b[0m, in \u001b[0;36mrev\u001b[0;34m(name)\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m index \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;28mlen\u001b[39m(name)):\n\u001b[1;32m      4\u001b[0m     \u001b[38;5;28mreversed\u001b[39m \u001b[38;5;241m=\u001b[39m name[index]\n\u001b[0;32m----> 5\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mreversed\u001b[39m[index]\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      6\u001b[0m     index\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m\n",
      "\u001b[0;31mIndexError\u001b[0m: string index out of range"
     ]
    }
   ],
   "source": [
    "def rev(name):\n",
    "    index=len(name)\n",
    "    for index in range(len(name)):\n",
    "        reversed = name[index]\n",
    "        print(f\"{reversed[index]}\")\n",
    "        index+=1\n",
    "rev(\"Manvi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecaaa367-7997-4d9b-b810-7ccf51998e25",
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
