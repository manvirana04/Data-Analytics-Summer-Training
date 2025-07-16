{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cee60d27-1256-4745-9a07-d77b173d7e34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first value: 50\n",
      "Enter second value: 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition:\n",
      "60\n",
      "Subtrction:\n",
      "40\n",
      "product:\n",
      "500\n",
      "divide:\n",
      "5.0\n",
      "modulus:\n",
      "0\n",
      "Float division:\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#Arithmetic Operators\n",
    "a=int(input(\"Enter first value:\"))\n",
    "b=int(input(\"Enter second value:\"))\n",
    "print(\"Addition:\")\n",
    "print(a+b)\n",
    "print(\"Subtrction:\")\n",
    "print(a-b)\n",
    "print(\"product:\")\n",
    "print(a*b)\n",
    "print(\"divide:\")\n",
    "print(a/b)\n",
    "print(\"modulus:\")\n",
    "print(a%b)\n",
    "print(\"Float division:\")\n",
    "print(a//b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "21e2fc8f-4448-4435-b11b-ef0efd236412",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pre increment:\n",
      "15\n",
      "post increment:\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "#Preorder , Postorder Incrementation\n",
    "a=10\n",
    "print(\"pre increment:\")\n",
    "a+=5\n",
    "print(a)\n",
    "print(\"post increment:\")\n",
    "a=+20\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b225c1e0-93b3-4347-bd9d-e178d86dd1d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a is greater:\n",
      "False\n",
      "b is greater:\n",
      "True\n",
      "a and b are equal\n",
      "False\n",
      "a is less than equal to b:\n",
      "True\n",
      "b is less than equal to a:\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#Comparison Operators\n",
    "a=10\n",
    "b=20\n",
    "print(\"a is greater:\")\n",
    "print(a>b)\n",
    "print(\"b is greater:\")\n",
    "print (a<b)\n",
    "print(\"a and b are equal\")\n",
    "print(a==b)\n",
    "print(\"a is less than equal to b:\")\n",
    "print(a<=b)\n",
    "print(\"b is less than equal to a:\")\n",
    "print(a>=b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7e083bbd-3c65-401f-8442-7c2e12e3fa55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AND operator:\n",
      "True\n",
      "OR operator:\n",
      "True\n",
      "NOT operator:\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#logical operators\n",
    "a=10\n",
    "b=20\n",
    "print(\"AND operator:\")\n",
    "print(a<b and b>a)\n",
    "print(\"OR operator:\")\n",
    "print(a<b or a==b)\n",
    "print(\"NOT operator:\")\n",
    "print(not(a<b and b>a))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bb351799-a123-4d3b-9ed7-ef90ff2fe004",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#Membership operator\n",
    "a=\"Manvi\"\n",
    "print(\"M\" in a)\n",
    "print(\"B\" in a)\n",
    "print(\"v\" not in a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "95a7c474-e499-4e61-b2ed-a206e6e6682d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bitwise AND operator\n",
      "True\n",
      "Bitwise OR operator\n",
      "False\n",
      "Bitwise Not operator\n",
      "-11\n"
     ]
    }
   ],
   "source": [
    "#bitwise operator\n",
    "a=10\n",
    "b=20\n",
    "print(\"Bitwise AND operator\")\n",
    "result=a<b & b>a\n",
    "print(result)\n",
    "print(\"Bitwise OR operator\")\n",
    "result = a>b | b>a\n",
    "print(result)\n",
    "print(\"Bitwise Not operator\")\n",
    "result=~a\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c7d41982-d9fd-4e78-be01-3e367fe26464",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "#Indentify operator\n",
    "a=10\n",
    "b=20\n",
    "print(a is b)\n",
    "print(a is not b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b846985-dda0-47da-92db-5da69ab56b39",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30c6e9c4-4fd8-49fb-af88-e961b2119b6f",
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
