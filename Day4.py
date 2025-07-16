{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ea3f412a-9d51-4228-9e8b-39d330b60c27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "#Factorial using function\n",
    "def fact(num):\n",
    "    factorial=1\n",
    "    i=1\n",
    "    while i<=num:\n",
    "        factorial*=i\n",
    "        i+=1\n",
    "    print(factorial)\n",
    "fact(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "567e82bc-77b3-4519-bc70-a65b6ff40fb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter principle amount 2000\n",
      "Enter rate of interest 3\n",
      "Enter time 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Simple interest is : 600.0\n"
     ]
    }
   ],
   "source": [
    "#SI function\n",
    "def interest():\n",
    "    p=int(input(\"Enter principle amount\"))\n",
    "    r=int(input(\"Enter rate of interest\"))\n",
    "    t=int(input(\"Enter time\"))\n",
    "    SI=(p*r*t)/100\n",
    "    print(f\"Simple interest is : {SI}\")\n",
    "interest()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9a5aaa4c-5f35-4d20-a240-b338ddc15ee9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Simple interest is : 200.0\n"
     ]
    }
   ],
   "source": [
    "#SI function\n",
    "def interest(p,r,t):\n",
    "    SI=(p*r*t)/100\n",
    "    print(f\"Simple interest is : {SI}\")\n",
    "interest(1000,5,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "9d7f1775-6a80-42c8-bf06-f25c5332a2fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#table of two\n",
    "def table(a):\n",
    "    for i in range(1,11):\n",
    "        print(f\"{a}x{i}={a*i}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "50d3b07e-1f33-42f4-8acd-1d55b82787cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2x1=2\n",
      "2x2=4\n",
      "2x3=6\n",
      "2x4=8\n",
      "2x5=10\n",
      "2x6=12\n",
      "2x7=14\n",
      "2x8=16\n",
      "2x9=18\n",
      "2x10=20\n"
     ]
    }
   ],
   "source": [
    "table(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2901e9ad-ce7a-41d8-b03e-9398a25d17cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#sum of natural numbers between 1 and 50\n",
    "def naturalsum(a,b):\n",
    "    sum=0\n",
    "    for i in range(a,b):\n",
    "        sum+=i\n",
    "    print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "96db381e-ef69-44b4-8762-3a275cd3a7d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1275\n"
     ]
    }
   ],
   "source": [
    "naturalsum(1,51)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "d3cb6b42-f39b-4463-9ece-3d2914dd4dad",
   "metadata": {},
   "outputs": [],
   "source": [
    "#sum of odd numbers between 1 and 50\n",
    "def oddsum(a,b):\n",
    "    sum=0\n",
    "    for i in range(a,b):\n",
    "        check=i%2\n",
    "        if check==0:\n",
    "            continue\n",
    "        else:\n",
    "            sum+=i\n",
    "    print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "eff01c46-45aa-46e3-b803-4e5a71ade800",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "625\n"
     ]
    }
   ],
   "source": [
    "oddsum(1,51)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "48c929ab-efb1-48f5-b4d0-be704c967909",
   "metadata": {},
   "outputs": [],
   "source": [
    "#default variable\n",
    "def defadd(a,b=10):\n",
    "    print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "791151a4-177b-4b2b-9ed0-471311942a60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "defadd(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "af427edc-70a9-487d-9b58-5bb108d95ae0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n"
     ]
    }
   ],
   "source": [
    "defadd(2,20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "8110a6f1-56fb-47f8-b479-243622d336a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#default variable\n",
    "def defadd2(a=20,b=10):\n",
    "    print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "c9475c3a-4500-4290-b1b0-899b96b1c3bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "defadd2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "a00ca645-29ca-4cff-b11f-48da7d34128b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "defadd2(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "d5009002-6467-41f4-8b8f-bd96298f9f14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "defadd2(10,20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "642c7c32-d2a8-412f-ab41-7e8aa183c7cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def adding(a,b):\n",
    "    c=a+b\n",
    "    print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "a33c3ea8-bdef-4ad2-aab1-e02e31c5b0b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "x=adding(5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "4bd41381-e37c-4cd1-859c-d3192defa742",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "x=adding(5,6)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "2296ac4c-db75-48c7-bdf6-65e023cf8430",
   "metadata": {},
   "outputs": [],
   "source": [
    "def addition(x,y):\n",
    "    z=x+y\n",
    "    return x+y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "07161715-f5d4-40ab-bd98-a55581dc6e85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "addition(2,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "79b6129e-2128-4f79-9c5b-b1c8d6a2a94c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "xy=addition(1,2)\n",
    "print(xy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "fb4b7ca0-060e-4de0-b7c8-0cf45ce24693",
   "metadata": {},
   "outputs": [],
   "source": [
    "#lambda function\n",
    "add=lambda x,y:x+y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "c971d51f-76ca-4f09-a8b2-d887e62ba20c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "a0cae9ca-a96c-4e95-ae2f-c3789ce7b539",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#keyword argument\n",
    "def show(a,b):\n",
    "    return a+b\n",
    "show(a=45, b=12)\n",
    "show(9, b=12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "1d666a62-d09e-4270-b6b9-94bb3c45b9b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'NoneType' and 'int'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[110], line 7\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mcal1\u001b[39m():\n\u001b[1;32m      6\u001b[0m     z\u001b[38;5;241m=\u001b[39mcal(\u001b[38;5;241m4\u001b[39m,\u001b[38;5;241m5\u001b[39m)\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m     \n\u001b[0;32m----> 7\u001b[0m cal1()\n",
      "Cell \u001b[0;32mIn[110], line 6\u001b[0m, in \u001b[0;36mcal1\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mcal1\u001b[39m():\n\u001b[0;32m----> 6\u001b[0m     z\u001b[38;5;241m=\u001b[39mcal(\u001b[38;5;241m4\u001b[39m,\u001b[38;5;241m5\u001b[39m)\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m\n",
      "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'NoneType' and 'int'"
     ]
    }
   ],
   "source": [
    "#nested function\n",
    "def cal(a,b):\n",
    "    c=a+b\n",
    "    print(c)\n",
    "def cal1():\n",
    "    z=cal(4,5)+1     \n",
    "cal1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "09ddebf8-6132-489c-bd2a-510378aef2f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number 6\n",
      "Enter a number 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Can't divide by zero\n",
      "The End\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    a=int(input(\"Enter a number\"))\n",
    "    b=int(input(\"Enter a number\"))\n",
    "    c=a/b\n",
    "except ZeroDivisionError:\n",
    "    print(\"Can't divide by zero\")\n",
    "else:\n",
    "    print(f\"Result: {c}\")\n",
    "finally:\n",
    "    print(\"The End\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "a0bb2824-d604-4fd1-813c-940d5c758469",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "#Factorial using function\n",
    "def factorial(n):\n",
    "    if n==1:\n",
    "        return 1\n",
    "    return n*factorial(n-1)\n",
    "    \n",
    "print(factorial(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "90880fa4-e728-47eb-8f71-152f11593573",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ivnaM\n"
     ]
    }
   ],
   "source": [
    "#Reverse string using splicing\n",
    "def reverse(string):\n",
    "    print(string[::-1])\n",
    "reverse(\"Manvi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "cf091009-afa8-460f-9afa-ad22c96faf5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ivnaM"
     ]
    }
   ],
   "source": [
    "def reverse(string):\n",
    "    i = len(string) - 1\n",
    "    while i >= 0:\n",
    "        print(string[i], end=\"\")\n",
    "        i -= 1\n",
    "reverse(\"Manvi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "c1a84ec5-008f-4571-82c2-cf86009bbd0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "57\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "def add(a,b):\n",
    "    print(a+b)\n",
    "    def add1(c,d):\n",
    "        x = c + d\n",
    "        print(x)\n",
    "    add1(2,3)\n",
    "add(12,45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3f0bc035-94ee-4d04-af8f-4db46d9062f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello user\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter password open\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Login\n"
     ]
    }
   ],
   "source": [
    "def login():\n",
    "    password='open'\n",
    "    attempts=3\n",
    "    print(\"Hello user\")\n",
    "    while attempts>0:\n",
    "        x=input(\"Enter password\")\n",
    "        if x=='open':\n",
    "            print(\"Login\")\n",
    "            break\n",
    "        else:\n",
    "            attempts-=1\n",
    "            print(f\"Wrong password:{attempts} attempts left\")\n",
    "login()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7af10d67-f24a-432c-8425-6ab0c41051af",
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
