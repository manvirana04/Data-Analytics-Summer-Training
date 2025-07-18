{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "1b8b00dd-f413-4d80-94ab-01be6c6999aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Data Structures\n",
    "#List\n",
    "lst=[1,3,5,11,7,9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "3276a7cd-8907-424c-b879-e8d7f4209c67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 11, 7, 9, 11]\n"
     ]
    }
   ],
   "source": [
    "#append\n",
    "lst.append(11)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "0ef508a8-9399-48ef-b8b1-a03eaffb47b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 5, 11, 7, 9, 11]\n"
     ]
    }
   ],
   "source": [
    "#insert\n",
    "lst.insert(1,2)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "590daa12-a538-408f-ba04-d07473868a36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 5, 11, 7, 9, 11, 13, 15]\n"
     ]
    }
   ],
   "source": [
    "#extend\n",
    "lst.extend([13,15])\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "7bc9f046-7d70-43a1-a6ba-26fb7a821b0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 5, 11, 7, 9, 11, 13]\n"
     ]
    }
   ],
   "source": [
    "#pop\n",
    "lst.pop()\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c5daef95-a9e5-4fbb-86aa-1e3b76603cc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 11, 7, 9, 11, 13]\n"
     ]
    }
   ],
   "source": [
    "#remove\n",
    "lst.remove(2)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "0058ae9e-7566-4d1c-b8b9-d7d47bffd8e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#index\n",
    "lst.index(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "9a731658-fad7-4fc4-80db-442142082142",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#count\n",
    "lst.count(11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "c589b024-16eb-4fda-a85c-c3849601224d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 7, 9, 11, 11, 13]\n"
     ]
    }
   ],
   "source": [
    "#sort in ascending\n",
    "lst.sort()\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "71a1cc10-7c6b-4ddf-b5ee-bdde98cc7567",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[13, 11, 11, 9, 7, 5, 3, 1]\n"
     ]
    }
   ],
   "source": [
    "#sort in descending \n",
    "lst.sort(reverse='true')\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "4698408b-5e49-4a84-a327-4f7e8eb9fa12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 7, 9, 11, 11, 13]\n"
     ]
    }
   ],
   "source": [
    "#reverse\n",
    "lst.reverse()\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "825f886e-fbfc-4dc9-9a67-f201cbd3a434",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lst2: [1, 3, 5, 7, 9, 11, 11, 13]\n"
     ]
    }
   ],
   "source": [
    "#copy()\n",
    "lst2=lst.copy()\n",
    "print(f\"lst2: {lst2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "91b1f331-f66a-4762-9446-5c8a2a562fdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lst2:[]\n"
     ]
    }
   ],
   "source": [
    "#clear\n",
    "lst2.clear()\n",
    "print(f\"lst2:{lst2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0801dc52-e99b-406c-8069-c234ffc3b7d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7]\n",
      "[7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "#Slicing\n",
    "lst10=[1,2,3,4,5,6,7,8,9,10]\n",
    "print(lst10[0:7])\n",
    "print(lst10[6:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fce41798-f647-4541-82c7-e0808f3e9010",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 6]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#list comprehension\n",
    "[i*2 for i in [1,2,3]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b7df356a-cfab-4208-8f93-643aceafdefe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[15, 17, 25, 27, 35, 37]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#list comprehension 2\n",
    "[10*i+j for i in [1,2,3] for j in [5,7]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a6d7cc46-a1b1-4f1a-9e96-66f0f9957221",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No. of a in the string: 3\n",
      "index of a: 0\n"
     ]
    }
   ],
   "source": [
    "#Tuples\n",
    "d=tuple('apple mango grapes')\n",
    "print(f\"No. of a in the string: {d.count('a')}\")\n",
    "print(f\"index of a: {d.index('a')}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "688f6b9d-a178-4e89-8d33-1852db341422",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple mango grapes\n",
      "apple mango grapes\n",
      "apple mango grapes\n"
     ]
    }
   ],
   "source": [
    "(a,b,c)= ('apple','mango','grapes') # are optional\n",
    "a,b,c= 'apple','mango','grapes' # The same as the above\n",
    "print(a,b,c)\n",
    "a,b,c = ['apple','mango','grapes'] # can assign lists\n",
    "print(a,b,c)\n",
    "[a,b,c]=('apple','mango','grapes') # even this is OK\n",
    "print(a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "acb97f8f-e757-468c-b043-aa4b83c022c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Sets\n",
    "s1=set([1,2,3,4,5]) #another way: s={1,2,3,4,5}\n",
    "s2=set([6,7,8,9,10])\n",
    "s3={1,2,3,4,5}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "474f44d8-e36e-4c0b-a8ca-324d9493ab8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#union\n",
    "s1.union(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "8a9f8eef-69ac-4440-addd-390a607dc3f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{6, 7, 8, 9, 10, 11}\n"
     ]
    }
   ],
   "source": [
    "#Add\n",
    "s2.add(11)\n",
    "print(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "707ae869-c81c-4ab8-ab82-4d59f6d51ee8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{6, 7, 8, 9, 10, 11, 20}\n"
     ]
    }
   ],
   "source": [
    "#Update\n",
    "s2.update([20])\n",
    "print(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "eaeb9ceb-55f4-468c-a66d-59d47ce46ed0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Pop\n",
    "s2.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "e4ff9921-e7dc-41a5-857a-2f2d6f8fb491",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{7, 8, 10, 11, 20}\n"
     ]
    }
   ],
   "source": [
    "#Remove\n",
    "s2.remove(9)\n",
    "print(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "b9862e6d-77c1-4093-88ae-8cc65089954d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set()"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Intersection\n",
    "s1.intersection(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "ae77d364-4fa0-47c3-9123-c3a5c21f7334",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n",
      "After using clear(): set()\n"
     ]
    }
   ],
   "source": [
    "#Clear\n",
    "print(s3)\n",
    "s3.clear()\n",
    "print(f\"After using clear(): {s3}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "1d9d27e2-e42d-4485-9839-f027dab05a29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5}"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Difference()\n",
    "s1.difference(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "34dc1a91-a49c-4130-882f-6f537f83e956",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 7, 8, 10, 11, 20}"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.symmetric_difference(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "490a6200-9607-408f-bdd7-bc9c5b95d2ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.issubset(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "5c7c537c-7b49-4e71-a135-9046941f89f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.isdisjoint(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "a3111de8-faf9-4b48-9dd9-d157a3a125c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.issuperset(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "4312afd9-c2a7-47ad-8ff9-384ad0a3f6a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dictionaries\n",
    "d={1:'One',2:'Two',3:'Three',4:'Four',5:'Five'}\n",
    "d1={6:'Six',7:'Seven',8:'Eight'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "15c19699-0d39-4d38-bd8b-0736f595556f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#length\n",
    "len(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "e0ffd532-ea1b-4065-9d80-135228eccfd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "One\n"
     ]
    }
   ],
   "source": [
    "#printing value of key\n",
    "print(d[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "9cad8173-3681-4642-b722-b3f94a14db76",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['One', 'Two', 'Three', 'Four', 'Five']"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#printing all values in the dictionary\n",
    "[v for v in d.values()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "f8065863-8d81-4a59-a55b-06726159717e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5}"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#printing all the keys in the dictionary\n",
    "{k for k in d.keys()}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "d807b3c3-424f-4ec0-b077-d3e44918f91d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys([6, 7, 8])"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "7c4ab260-d2c1-4712-953e-7598f84ee3f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Six'"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.get(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "2b20c90c-4cba-4665-922e-a30e209b2684",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['Six', 'Seven', 'Eight'])"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "67763339-0fa6-4b4f-8ac0-ed27368c649f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([(6, 'Six'), (7, 'Seven'), (8, 'Eight')])"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.items()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "d217c50f-19b7-465e-bb3d-ffaf70629c7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight'}\n"
     ]
    }
   ],
   "source": [
    "d.update(d1)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "77ab99d7-b3af-46bb-8ff6-0564fbbb369c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{6: 'Six', 7: 'Seven', 8: 'Eight'}\n"
     ]
    }
   ],
   "source": [
    "d2=d1.copy()\n",
    "print(d2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "1af53830-a81a-441c-b0e0-a4ee1377995b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Eight'"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.pop(8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "c05c3831-7368-468b-b0d6-a22819c17834",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7, 'Seven')"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.popitem()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "bbca0d03-aeaa-4986-97dd-23ba86df733a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "d1.clear()\n",
    "print(d1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "367b786b-4133-4cbd-9268-88eb8877777d",
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
