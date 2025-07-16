{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e1b7c13d-637e-4d12-9380-0973dbc0109c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "#Explicit Type conversion\n",
    "x=10\n",
    "y=float(x)\n",
    "print(type(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5f47ae0d-550e-4a7d-9e7c-08402a98b467",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "#Implicit Type Conversion\n",
    "x=10\n",
    "y=10.5\n",
    "print(type(x+y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fa617342-9af9-4845-aaaa-9eb086c358eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Product name Mango\n",
      "Quantity 12\n",
      "Price 100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The bill for  Mango : 1200.0\n"
     ]
    }
   ],
   "source": [
    "#Bill Calculator\n",
    "Product=input(\"Product name\")\n",
    "Qty=int(input(\"Quantity\"))\n",
    "Price=float(input(\"Price\"))\n",
    "Bill=Qty*Price\n",
    "print(\"The bill for \" , Product , \":\" ,Bill)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a958e697-9980-438d-874b-9c9a96b173e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "false\n"
     ]
    }
   ],
   "source": [
    "# control statements\n",
    "x=0\n",
    "if x:\n",
    "    print('true')\n",
    "else:\n",
    "    print('false')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1e23d915-df59-4e40-812f-078f11903014",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Age 25\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eligible to vote\n"
     ]
    }
   ],
   "source": [
    "#Q2\n",
    "age=int(input(\"Age\"))\n",
    "if age<18:\n",
    "        print(\"Not eligible\")\n",
    "else:\n",
    "        print(\"Eligible to vote\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "7754666b-906e-48e1-b771-772bd5e98c55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Number 23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Odd number\n"
     ]
    }
   ],
   "source": [
    "#Q3\n",
    "num=int(input(\"Number\"))\n",
    "check=num%2\n",
    "if check==0:\n",
    "    print(\"Even number\")\n",
    "else:\n",
    "    print(\"Odd number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ef36b995-816f-496a-bfc0-35a3c462f199",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Entert marks 67\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pass\n"
     ]
    }
   ],
   "source": [
    "#Q5\n",
    "marks=int(input(\"Entert marks\"))\n",
    "if marks>=40:\n",
    "    print(\"Pass\")\n",
    "else:\n",
    "    print(\"Fail\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4419caa9-c0b4-411b-b996-46fd7ce631ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter name ManviRana\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length is greater than 5\n"
     ]
    }
   ],
   "source": [
    "#Q4\n",
    "name=input(\"Enter name\")\n",
    "if len(name)>5 :\n",
    "    print(\"Length is greater than 5\")\n",
    "else:\n",
    "    print(\"Length less than 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f8315cbc-1454-4c6c-b43d-fc06f0855f4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number -5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Negative number\n"
     ]
    }
   ],
   "source": [
    "#Q1\n",
    "x=int(input(\"Enter number\"))\n",
    "if x>0:\n",
    "    print(\"Positive number\")\n",
    "else:\n",
    "    print(\"Negative number\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "33a1adfb-da29-4008-b615-79cf0b3134cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter month December\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Winter\n"
     ]
    }
   ],
   "source": [
    "#nested elif\n",
    "month=(input(\"Enter month\"))\n",
    "if month=='January' or month=='November' or month=='December':\n",
    "       print(\"Winter\")\n",
    "elif month=='February' or month=='March':\n",
    "       print(\"Spring\")\n",
    "elif month=='April' or month=='May' or month=='June' or month=='July':\n",
    "    print(\"Summer\")\n",
    "elif month=='August' or month=='September':\n",
    "    print(\"Monsoon\")\n",
    "elif month=='October':\n",
    "    print(\"Autumn\")\n",
    "else:\n",
    "    print(\"Invalid month\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "b8b8cf24-abf6-4dde-b78e-8e05486be311",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter type of vehicle Bike\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Expires 20 years after registeration\n"
     ]
    }
   ],
   "source": [
    "#Vehicle Expiry Checking\n",
    "v=input(\"Enter type of vehicle\")\n",
    "if v=='Car':\n",
    "    print(\"Expires 10 years after registeration\")\n",
    "elif v=='Bike':\n",
    "    print(\"Expires 20 years after registeration\")\n",
    "elif v=='Scooty':\n",
    "    print(\"Expires 20 years after registeration\")\n",
    "elif v=='Truck':\n",
    "    print(\"Expires 30 years after registeration\")\n",
    "else:\n",
    "    print(\"Vehicle type not in list\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "82d27ec6-c225-4684-9c2d-6b237c208eb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number +2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive number\n"
     ]
    }
   ],
   "source": [
    "#assignment\n",
    "#positive negative or zero \n",
    "x=int(input(\"Enter number\"))\n",
    "if x>0:\n",
    "    print(\"Positive number\")\n",
    "elif x==0:\n",
    "    print(\"Zero\")\n",
    "else:\n",
    "    print(\"Negative number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bee1cf71-79f6-4d02-bf91-f50ad672db53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Age 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Child\n"
     ]
    }
   ],
   "source": [
    "#assignment\n",
    "age=int(input(\"Age\"))\n",
    "if age<13:\n",
    "    print(\"Child\")\n",
    "elif age<18:\n",
    "    print(\"Teen\")\n",
    "else:\n",
    "    print(\"Adult\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f38893e6-fb58-4f99-9d4c-87d3381f2e59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Number 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It is Even number\n"
     ]
    }
   ],
   "source": [
    "#assignment\n",
    "num=int(input(\"Number\"))\n",
    "check=num%2\n",
    "if check==0 and num>10:\n",
    "    print(\"It is Even number and greater than 10\")\n",
    "elif check==0:\n",
    "    print(\"It is Even number\")\n",
    "else:\n",
    "    print(\"Odd number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "dda74e4c-849c-4819-af26-ee3c801065b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Entert marks 65\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C\n"
     ]
    }
   ],
   "source": [
    "#assignment\n",
    "marks=int(input(\"Entert marks\"))\n",
    "if marks>90:\n",
    "    print(\"A\")\n",
    "elif marks>75:\n",
    "    print(\"B\")\n",
    "elif marks>60:\n",
    "    print(\"C\")\n",
    "else:\n",
    "    print(\"Fail\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c5280168-fd61-487f-8541-3618c0fb3f9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Entert number 21\n",
      "Entert number 22\n",
      "Entert number 24\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24 (c) is the greatest integer\n"
     ]
    }
   ],
   "source": [
    "#assignment\n",
    "a=int(input(\"Entert number\"))\n",
    "b=int(input(\"Entert number\"))\n",
    "c=int(input(\"Entert number\"))\n",
    "if a>b and a>c:\n",
    "    print(a, \"(a) is the greatest integer\")\n",
    "if b>a and b>c:\n",
    "    print(b, \"(b) is the greatest integer\")\n",
    "if c>a and c>b:\n",
    "    print(c, \"(c) is the greatest integer\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e98bc646-546b-4570-92d2-852fc3d04d87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "#while loop\n",
    "a=2\n",
    "i=1\n",
    "while i<=10:\n",
    "    print(a*i)\n",
    "    i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2a6a76f-19cd-4eb2-95f8-8ab0eabb74c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#TUPLES"
   ]
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
