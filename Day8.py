{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7d55441e-72bc-4d57-bf9a-1d0e37e967f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Pandas data minuplation: series, data frame\n",
    "#series: use array\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e4a9f6de-00c1-452d-ba51-82975c1d74c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Name  Age  Marks\n",
      "0      Manvi   20     95\n",
      "1      Sneha   21     96\n",
      "2  Sanskriti   22     97\n",
      "3     Sakshi   23     98\n"
     ]
    }
   ],
   "source": [
    "#Dataframe\n",
    "data={ 'Name':['Manvi','Sneha','Sanskriti','Sakshi'], 'Age':[20,21,22,23], 'Marks':[95,96,97,98]}\n",
    "df=pd.DataFrame(data)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "05eceefe-8ee3-4490-af23-2e6a08b53943",
   "metadata": {},
   "outputs": [],
   "source": [
    "# To read a csv file:  df=pd.read_csv('data.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3c4e7f4c-1074-42a5-9c39-9840c78685c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Head:first 5 rows\n",
      "        Name  Age  Marks\n",
      "0      Manvi   20     95\n",
      "1      Sneha   21     96\n",
      "2  Sanskriti   22     97\n",
      "3     Sakshi   23     98\n",
      "\n",
      "Tail:last 5 rows\n",
      "        Name  Age  Marks\n",
      "0      Manvi   20     95\n",
      "1      Sneha   21     96\n",
      "2  Sanskriti   22     97\n",
      "3     Sakshi   23     98\n",
      "\n",
      "shape:(rows,columns)\n",
      "(4, 3)\n",
      "\n",
      "columns:Column names\n",
      "Index(['Name', 'Age', 'Marks'], dtype='object')\n",
      "\n",
      "Stats Summary\n",
      "             Age      Marks\n",
      "count   4.000000   4.000000\n",
      "mean   21.500000  96.500000\n",
      "std     1.290994   1.290994\n",
      "min    20.000000  95.000000\n",
      "25%    20.750000  95.750000\n",
      "50%    21.500000  96.500000\n",
      "75%    22.250000  97.250000\n",
      "max    23.000000  98.000000\n",
      "\n",
      "info:Summary\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4 entries, 0 to 3\n",
      "Data columns (total 3 columns):\n",
      " #   Column  Non-Null Count  Dtype \n",
      "---  ------  --------------  ----- \n",
      " 0   Name    4 non-null      object\n",
      " 1   Age     4 non-null      int64 \n",
      " 2   Marks   4 non-null      int64 \n",
      "dtypes: int64(2), object(1)\n",
      "memory usage: 228.0+ bytes\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "#Functions\n",
    "print(\"Head:first 5 rows\")\n",
    "print(df.head())\n",
    "print(\"\")\n",
    "print(\"Tail:last 5 rows\")\n",
    "print(df.tail())\n",
    "print(\"\")\n",
    "print(\"shape:(rows,columns)\")\n",
    "print(df.shape)\n",
    "print(\"\")\n",
    "print(\"columns:Column names\")\n",
    "print(df.columns)\n",
    "print(\"\")\n",
    "print(\"Stats Summary\")\n",
    "print(df.describe())\n",
    "print(\"\")\n",
    "print(\"info:Summary\")\n",
    "print(df.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "744870da-1be0-4ecd-ba74-8b176f1dbbca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0        Manvi\n",
      "1        Sneha\n",
      "2    Sanskriti\n",
      "3       Sakshi\n",
      "Name: Name, dtype: object\n",
      "\n",
      "        Name  Marks\n",
      "0      Manvi     95\n",
      "1      Sneha     96\n",
      "2  Sanskriti     97\n",
      "3     Sakshi     98\n",
      "\n",
      "Name     Manvi\n",
      "Age         20\n",
      "Marks       95\n",
      "Name: 0, dtype: object\n",
      "\n",
      "Name     Sneha\n",
      "Age         21\n",
      "Marks       96\n",
      "Name: 1, dtype: object\n"
     ]
    }
   ],
   "source": [
    "#loc, iloc\n",
    "print(df['Name'])\n",
    "print()\n",
    "print(df[['Name','Marks']])\n",
    "print()\n",
    "print(df.loc[0])\n",
    "print()\n",
    "print(df.iloc[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d356b9a6-9b28-481b-bc04-fc8bd6d35fdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Marks above 85:\n",
      "        Name  Age  Marks\n",
      "0      Manvi   20     95\n",
      "1      Sneha   21     96\n",
      "2  Sanskriti   22     97\n",
      "3     Sakshi   23     98\n",
      "\n",
      "Marks>85 and age < 22:\n",
      "    Name  Age  Marks\n",
      "0  Manvi   20     95\n",
      "1  Sneha   21     96\n"
     ]
    }
   ],
   "source": [
    "#conditionwise filtering\n",
    "print(\"Marks above 85:\")\n",
    "print(df[df['Marks']>85])\n",
    "print()\n",
    "print(\"Marks>85 and age < 22:\")\n",
    "print(df[(df['Marks']>85) & (df['Age']<22)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c57edda1-939b-4529-8eb2-ccc834cd75f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Name Course  marks\n",
      "0      Manvi    BFA     97\n",
      "1      Sneha    BCA     98\n",
      "2  Sanskriti   Bcom     99\n"
     ]
    }
   ],
   "source": [
    "#Practice\n",
    "ds={'Name':['Manvi','Sneha','Sanskriti'],'Course':['BFA','BCA','Bcom'],'marks':[97,98,99]}\n",
    "df1=pd.DataFrame(ds)\n",
    "print(df1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "251133d3-ca76-4d5c-9c89-b5f10d52d185",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Add, update Column\n",
    "df1['Grade']=['A','B','C']\n",
    "df1['marks']=df1['marks']+5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "69dfa6b3-d832-41d0-8956-8285c9bc6469",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Columnwise Drop\n",
    "df1.drop('Grade', axis=1, inplace=True) #inplace=true means original dataframe changed, if not there then everywhere same named column deleted\n",
    "#Rowwise drop\n",
    "df1.drop(1,axis=0,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7711c370-e716-43b1-8f30-389aa53cf440",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Name Course  marks\n",
      "2  Sanskriti   Bcom    104\n",
      "0      Manvi    BFA    102\n"
     ]
    }
   ],
   "source": [
    "#Sorting\n",
    "print(df1.sort_values(by='marks', ascending=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c9524ba8-fd4e-4efb-868d-053a2fe0c76c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Name Course  marks\n",
      "0      Manvi    BFA     99\n",
      "1      Sneha    BCA     95\n",
      "2  Sanskriti   Bcom     98\n",
      "3     Sakshi    BBA     97\n",
      "4      Aditi     BA     98\n"
     ]
    }
   ],
   "source": [
    "#Practice\n",
    "ds1={'Name':['Manvi','Sneha','Sanskriti','Sakshi','Aditi'],'Course':['BFA','BCA','Bcom','BBA','BA'],'marks':[99,95,98,97,98]}\n",
    "df2=pd.DataFrame(ds1)\n",
    "print(df2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cf637860-bab4-4afd-92ed-283208c3a9cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Name Course  marks\n",
      "0      Manvi    BFA     99\n",
      "2  Sanskriti   Bcom     98\n",
      "4      Aditi     BA     98\n",
      "3     Sakshi    BBA     97\n",
      "1      Sneha    BCA     95\n"
     ]
    }
   ],
   "source": [
    "#Sorting\n",
    "print(df2.sort_values(by='marks', ascending=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "861c1af1-401c-479c-b7b6-21797d2d06db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Name  Marks\n",
      "0     a      1\n",
      "1     b      2\n",
      "2  None      3\n",
      "\n",
      "   Name  Marks\n",
      "0     a      1\n",
      "1     b      2\n",
      "2  None      3\n"
     ]
    }
   ],
   "source": [
    "#fillna, dropna\n",
    "df3=pd.DataFrame({'Name':['a','b',None], 'Marks':[1,2,3]})\n",
    "print(df3)\n",
    "df.fillna('Unknown', inplace=True)\n",
    "df.dropna(inplace=True)\n",
    "print()\n",
    "print(df3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "68942bc0-e3c3-43f2-b322-a7757d43e636",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dept\n",
      "HR    25.0\n",
      "IT    25.0\n",
      "Name: Salary, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "#Groupby\n",
    "df4=pd.DataFrame({'Dept':['IT','HR','HR','IT'], 'Salary':[10,20,30,40]})\n",
    "print(df4.groupby('Dept')['Salary'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a2f2b6ee-2a11-4bac-b5dd-4fe19c104df1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataframe 1:\n",
      "   Id Name\n",
      "0  11    A\n",
      "1  22    B\n",
      "2  33    C\n",
      "3  44    D\n",
      "4  55    E\n",
      "\n",
      "Dataframe 2:\n",
      "   Id  Marks\n",
      "0  11     93\n",
      "1  22     94\n",
      "2  33     95\n",
      "3  44     96\n",
      "4  55     97\n",
      "\n",
      "Mergeed Dataframe:\n",
      "   Id Name  Marks\n",
      "0  11    A     93\n",
      "1  22    B     94\n",
      "2  33    C     95\n",
      "3  44    D     96\n",
      "4  55    E     97\n"
     ]
    }
   ],
   "source": [
    "#Merge Frameset\n",
    "df5=pd.DataFrame({'Id':[11,22,33,44,55],'Name':['A','B','C','D','E']})\n",
    "df6=pd.DataFrame({'Id':[11,22,33,44,55],'Marks':[93,94,95,96,97]})\n",
    "print(\"Dataframe 1:\")\n",
    "print(df5)\n",
    "print()\n",
    "print(\"Dataframe 2:\")\n",
    "print(df6)\n",
    "merged=pd.merge(df5,df6, on='Id')\n",
    "print()\n",
    "print(\"Mergeed Dataframe:\")\n",
    "print(merged)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2acf5b38-faa9-4f08-a651-1a4528a9ddaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#clean up data: update, replace, drop, find unknown values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c5e41495-5408-4ae2-91bf-00d249aa2c87",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Graph\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "a2a044a7-f078-406d-9e8b-4aa24addaa05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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787kyZOpVasWjRo14ptvvmHmzJkMHjzY6tLs6tNPP8UwDG677TZ++uknxo4dy2233cagQYOsLq3QLl26xE8//ZRzfPDgQRITE6lUqRK1atUiKiqKKVOmUL9+ferXr8+UKVPw8/Ojb9++xVNgsdwz5UaAfL8WLVpkdWl2M3jwYKN27dqGt7e3UbVqVaNjx47Gli1brC7Lodzp1uw+ffoYgYGBhpeXlxEUFGT06NHD2L9/v9Vl2d3//d//GY0bNzZ8fHyMBg0aGPPmzbO6JLv69NNPDcA4cOCA1aXYXVJSkjFq1CijVq1aRunSpY26desaL730kpGWlmZ1aXa1cuVKo27duoa3t7dRvXp1Y/jw4caFCxesLqtItm3blu/ffQMGDDAMw7w9e/z48Ub16tUNHx8f47777jP27dtXbPXZDMMwiic2iYiIiNif1syIiIiIS1OYEREREZemMCMiIiIuTWFGREREXJrCjIiIiLg0hRkRERFxaQozIiIi4tIUZkSkRGjXrh1RUVFWlyEiDqCH5olIiXDu3Dm8vLwoV66c1aWIiJ0pzIiIiIhL0zSTiBSrM2fOUL16daZMmZLT9vXXX+Pt7c2WLVvyfU9CQgLh4eFUqVKF8uXLExYWxp49e3Je3759O97e3uzYsSOn7Y033qBKlSqcPHkSyDvN9O6771K/fn1Kly5NQEAAPXv2tHNPRaS4KMyISLGqWrUqCxcuJDo6ml27dnHp0iX69evHsGHDiIiIyPc9ycnJDBgwgB07dvDVV19Rv359unTpQnJyMnA1qPTv35+LFy+yd+9eXnrpJebPn09gYGCe6+3atYuRI0cyceJEDhw4wCeffMJ9993n0H6LiONomklELDF8+HA+++wzWrZsyd69e0lISKB06dIFem9mZiYVK1Zk+fLldOvWDYArV65w9913U79+ffbv30/r1q2ZP39+znvatWtHaGgoMTExrF27lkGDBnHs2DGtoRFxAxqZERFLvP7662RkZLBq1So++OADSpcuzZEjRyhbtmzOV/ZU1OnTpxk6dCi33nor5cuXp3z58ly6dIkjR47kXM/b25tly5axZs0aLl++TExMzHX/7PDwcGrXrk3dunXp378/H3zwAampqY7usog4SCmrCxCRkumXX37hxIkTZGVlcfjwYZo0aUJQUBCJiYk551SqVAmAgQMHcubMGWJiYqhduzY+Pj60bt2aK1eu5Lrml19+CZh3Lp07d44yZcrk+2eXK1eOPXv2sH37drZs2cKrr75KdHQ0CQkJVKhQwSH9FRHH0TSTiBS7K1eu0KpVK0JDQ2nQoAEzZ85k3759BAQE5Ht+uXLlePfdd+nfvz8AR48epVatWrz55ps5i3p//vlnQkNDefvtt1m1ahW///47W7duxcPDHID+4zTTtVJSUqhQoQIrV66kR48eDumziDiORmZEpNi99NJLXLx4kbfffpuyZcuyefNmHn/8cTZu3Jjv+fXq1WPp0qW0aNGCpKQkxo4di6+vb87rmZmZ9O/fn4iICAYNGkRkZCR33HEHb7zxBmPHjs1zvY0bN/LLL79w3333UbFiRT7++GOysrK47bbbHNZnEXEcrZkRkWK1fft2YmJiWLp0Kf7+/nh4eLB06VK++OILZs+ene97Fi5cyPnz52nWrBn9+/dn5MiRVKtWLef1yZMnc+jQIebNmwdA9erVWbBgAS+//HKuaatsFSpUYO3atXTo0IGGDRsyZ84cPvzwQxo1auSQPouIY2maSURERFyaRmZERETEpSnMiIiIiEtTmBERERGXpjAjIiIiLk1hRkRERFyawoyIiIi4NIUZERERcWkKMyIiIuLSFGZERETEpSnMiIiIiEtTmBERERGXpjAjIiIiLu3/AZ4mhwU74IDEAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Line Graph\n",
    "x=[2,4,6,8,10]\n",
    "y=[3,5,8,12,15]\n",
    "plt.plot(x,y, color='blue', linestyle='--', marker='o')\n",
    "plt.title(\"Example:Line graph\")\n",
    "plt.xlabel(\"x-axis\")\n",
    "plt.ylabel(\"y-axis\")\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "77743a88-99b0-481a-a212-ef06e83e320e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAh8AAAGxCAYAAADCo9TSAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAIExJREFUeJzt3XtclGX+//H3CDgiASWloqKSWppk5iHTLM94rta2NLNV10o2xePuKrvfRExla8ulzXLVPLWpaWZqVqarmbZ2QM1DrQ/L8sCuspYpCBoJ3L8/+jHbBJjazGdAXs/H4/5jrrm5r2vG0Xl5zw24HMdxBAAAYKRSoBcAAAAqFuIDAACYIj4AAIAp4gMAAJgiPgAAgCniAwAAmCI+AACAKeIDAACYIj4AAIAp4gO4SAsXLpTL5Sp127x5c6CX6BP169fXkCFDfHa8Q4cOFXuuIiIidNNNNyktLU0FBQU+m+tC7NmzR8OGDVODBg0UGhqq0NBQNWrUSMOHD9f27dtN1/Jj9evXV58+fQK6BsCfggO9AKC8WrBggRo3blxs/IYbbgjAasqPxMREDRw4UJJ06tQprVmzRmPHjlVGRoaefvppkzXMnj1bI0eO1PXXX6/Ro0eradOmcrlc2rdvn5YuXarWrVvrwIEDatCggcl6gIqG+AAuUVxcnFq1ahXoZZQ7devW1a233uq53aNHD33yySdaunSpz+LjzJkzqlq1aon3/fOf/9Sjjz6q3r17a8WKFapcubLnvs6dO2vEiBF65ZVXFBoaeslzADg/PnYB/OTll1+Wy+XSzJkzvcaTk5MVFBSkDRs2eMZSUlLUpk0bVatWTREREWrRooXmzZunH//ex6LT8WvXrtXNN9+s0NBQNWnSRGvXrpX0/UdCTZo0UVhYmG655ZZiHx8MGTJEV1xxhT799FN16dJFYWFhuuaaazRy5EidOXPmJx9Tdna2fvvb3yo2NlaVK1dW7dq1NWbMGOXm5l7q0yRJioyMVEhIiNfYsmXLFB8fr+joaM/jnDhxYrG5ih7T3r17FR8fr/DwcHXp0qXUuaZPn66goCDNnj3bKzx+6N5771WtWrUuaI4NGzborrvuUp06dVSlShU1bNhQw4cP19dff+11zMmTJ8vlcunjjz9Wv379FBERocjISA0aNEhfffVVietYt26dWrRoodDQUDVu3Fjz588v/UkEyhHiA7hEBQUFys/P99p+eN3CgAEDlJCQoPHjx3siYNOmTZo6dar+8Ic/qFu3bp59Dx06pOHDh2v58uVauXKl+vXrp8TERD3++OPF5t29e7eSkpI0YcIErVy5UpGRkerXr5+Sk5P1wgsvaPr06Vq8eLGysrLUp08fnT171uvrz507p169eqlLly5atWqVRo4cqdmzZ6t///7nfbxnzpxRhw4dtGjRIo0aNUpvvfWWJkyYoIULF+rOO+/0CqWiN9qSrn8pLCz0PF8nTpzQ/PnztW7dOj344INe+33++efq1auX5s2bp3Xr1mnMmDFavny5+vbtW+yY3333ne6880517txZq1evVkpKSomPoaCgQO+8845atWql6Ojo8z7eC53jiy++UNu2bTVr1iytX79ekyZN0ocffqj27dvr3LlzxY7zi1/8Qg0bNtSKFSs0efJkrVq1St27dy+27+7duzV+/HiNHTtWq1evVrNmzTRs2DBt2bLlotYNlEkOgIuyYMECR1KJW1BQkNe+3377rXPzzTc7sbGxzr/+9S+nRo0aTocOHZz8/PxSj19QUOCcO3fOmTJlihMVFeUUFhZ67qtXr54TGhrq/Pvf//aM7dq1y5HkREdHO7m5uZ7xVatWOZKcNWvWeMYGDx7sSHKeeeYZrzmnTZvmSHLee+89r7kGDx7suZ2amupUqlTJSU9P9/raFStWOJKcN9980zOWkpLiBAUFOZs3b/aMHTx4sNTnbciQIed9TgoLC51z58457777riPJ2b17d7HHNH/+/FK/vkhmZqYjyRkwYECx+/Lz851z5855th8+7xc6R9E6Dx8+7EhyVq9e7bkvOTnZkeSMHTvW62sWL17sSHJeeuklz1i9evWcKlWqOIcPH/aMnT171qlWrZozfPjwn3ycQFnHmQ/gEr344otKT0/32j788EOvfdxut5YvX64TJ06oRYsWchxHS5cuVVBQkNd+mzZtUteuXRUZGamgoCCFhIRo0qRJOnHihI4fP+61b/PmzVW7dm3P7SZNmkiSOnbs6HUNQtH44cOHi639gQce8LpddAHoO++8U+rjXbt2reLi4tS8eXOvsz3du3cvdpZj0qRJys/PV4cOHYodZ/To0Z7n65133tH06dO1fPly3X///V77ffnllxo4cKBq1qzpeU6Kjrdv375ix73nnntKXfuFaNmypUJCQjxbSdeflDTH8ePHlZCQoJiYGAUHByskJET16tUrdZ0/fu7vu+8+BQcHF3vumzdvrrp163puV6lSRdddd12Jf55AecMFp8AlatKkyQVdcNqwYUPdfvvteuONN/Sb3/ym2On+jz76SPHx8erYsaPmzp2rOnXqqHLlylq1apWmTZtW7GOTatWqed0uum6htPFvv/3Wazw4OFhRUVFeYzVr1pQknThxotTH8d///lcHDhwodm1GkR9f41CaOnXqeD1vHTt2lMvlUlJSkt5++211795dOTk5uv3221WlShVNnTpV1113napWraqMjAz169ev2HNStWpVRURE/OTcV199tUJDQ0t8A1+yZInOnDmjY8eO6c477yx2f0lzFBYWKj4+XkePHtVjjz2mG2+8UWFhYSosLNStt95abJ3S/57rIkV/Hj9+7n/8ZyR9H7MlHRMob4gPwM9eeOEFvfHGG7rllls0c+ZM9e/fX23atPHc//LLLyskJERr165VlSpVPOOrVq3yy3qKrrX44ZtbZmampJLf8IoUvXGXdtHj1VdffclratasmaTvr3Po3r27Nm3apKNHj2rz5s1eZ09OnTpV4te7XK4LmicoKEidO3fW+vXrdezYMa8QLPoW6UOHDl3wHJ988ol2796thQsXavDgwZ7xAwcOlLqGzMxMrzNXJf15AJc7PnYB/Gjv3r0aNWqUfvWrX2nr1q1q1qyZ+vfvr5MnT3r2cblcCg4O9voo5uzZs/r73//ut3UtXrzY6/aSJUskfX8WojR9+vTRF198oaioKLVq1arYVr9+/Utez65duyRJ1atXl/S/N3q32+213+zZsy95jiJJSUkqKChQQkJCiReEXoxLWeePn/vly5crPz//vM89cLnhzAdwiT755BPl5+cXG2/QoIGuueYa5ebm6r777lNsbKyef/55Va5cWcuXL1eLFi00dOhQz5mN3r17a8aMGRo4cKAeeeQRnThxQk899VSxNzRfqVy5sp5++mnl5OSodevW2rZtm6ZOnaqePXuqffv2pX7dmDFj9Oqrr+qOO+7Q2LFj1axZMxUWFurIkSNav369xo8f7zmjM2XKFE2ZMkUbN24sdt3HkSNH9MEHH0iScnNz9f777ys1NVX16tVTv379JEnt2rXTVVddpYSEBCUnJyskJESLFy/W7t27f/bjv+222/Tcc88p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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Bar graph\n",
    "x=['A','B','C']\n",
    "y=[5,10,8]\n",
    "plt.bar(x,y, color='green')\n",
    "plt.title(\"Example:Bar Graph\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "039ae958-2a28-43e5-b3d3-3f699e8db41d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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ZPn+/ftLzX7vvff6XR8yZIgkaePGjed9vuvWrVPr1q11zTXXqKioyHe5+eabS50lM3XqVBUVFalnz56lHmfs2LGl9ltGRkapL13+85//1IkTJ0qdsZKQkKAbb7xRaWlppR77jjvuOO/8ZdmzZ49uvfVWde3aVUuWLPEdeUlPT1dUVJTuvPNOv/VLZjl32zfccIOio6N91+vXr6969eqVue/L8vXXX2vIkCGKj4/3vf4l++7cj4DK40Je548++ki33nqr4uLifNseNmyYzpw5o88//9zv/pdddpluvPHGi54HsMTHIqiSWrZseUFf6LzqqqvUvXt3rV+/Xg888IDvkHiJ7du3q2/fvurVq5cWLVqkxo0bKywsTKtXr9bs2bN14sQJv/Xr1Knjdz0sLOwHl588edJveWhoqOLi4vyWxcfHS5JycnLO+zz+85//6Msvv1TNmjXLvP277747733P1rhx4zL327mn8JbMcu7+kqSGDRv6fWdFkiIjIxUTE3NBM0jSwYMH1a9fPzVu3FirVq3y7a+SbcfHx5c67bNevXoKDQ0ttZ/O3Z/S/8Ly3NeuLPn5+erevbvCw8M1a9Ys/exnP1NkZKSysrJ0++23X9BjlOVCXucDBw6oe/fuat68uZ599lk1adJE4eHh2r59u0aNGlVq22W9FkCwEBeo1l588UWtX79enTt31rx583T33Xfruuuu893+2muvqWbNmlq3bp3Cw8N9y1evXl0h8xQVFSknJ8fvjSc7O1tS2W+SJS6//HJFRESU+hz+7Nstlcxy6NChUrcdPHiw1PYu5O8/lMjLy1P//v1VXFyst956S7GxsaW2/cEHH8g55/e4hw8fVlFRkelzTU9P18GDB/Xee+/5Hem5lL+HIV3Y67x69WoVFBRo1apVSkxM9K2XmZlZ5mOWZx8DFY2PRVBt7dq1Sw899JCGDRumLVu2qG3btrr77rt19OhR3zoej0ehoaF+H5WcOHFCL7/8coXNtXz5cr/rr776qiSV+vLl2QYOHKivvvpKcXFx6tSpU6mL9R+q6tKliyIiIvTKK6/4Lf/mm2+Unp7uOxukvE6dOqXbbrtN+/bt09tvv63GjRuXWqd3797Kz88vFXjLli3z3V5eXq9XkkodDSh5wy65vcSf//zncm/jXD/2Ope1beecFi1adMnbBioaRy5QJf373/8u84yEK6+8UnXr1lVBQYHuuusuJSUl6fnnn1dYWJhWrlypDh066De/+Y3vjWvAgAF65plnNGTIEP3ud79TTk6OnnrqqVJvNlbCwsL09NNPKz8/X9dee63vLIJbbrlF3bp1O+/9xo0bpzfffFM9evTQ+PHj1bZtWxUXF+vAgQN699139cgjj/iOyMycOVMzZ85UWlpamd+7uBC1a9fWE088ocmTJ2vYsGEaPHiwcnJyNGPGDIWHh2vatGkX9bjjx49Xenq6UlJSlJ+fr/fff993W926dXXllVdq2LBhmj9/vpKTk7Vv3z61adNGW7duVUpKivr3768+ffqUe7tt2rSRJD377LNKTk5WzZo11bx5c3Xt2lWXXXaZRo4cqWnTpqlmzZpavny5du7ceVHPr8SFvM433XSTwsLCNHjwYD322GM6efKkFixY4Be/wE9WkL9QCpj6obNFJLlFixY555wbOnSoi4yMdLt37/a7/+uvv+4kuT/+8Y++ZUuWLHHNmzd3Xq/XNW3a1KWmprrFixeXOrsgMTHRDRgwoNRMktyoUaP8lpWcnTF37lzfsuTkZBcVFeU+/vhj16tXLxcREeHq1KnjHnjgAZefn+93/3PPFnHOufz8fPf444+75s2bu7CwMBcbG+vatGnjxo8f77Kzs33rlZzVsHHjxh+c52znO5vixRdfdG3btvVt7xe/+EWpfVryvMpy7tkiJWc9lHU5+/nm5OS4kSNHugYNGrjQ0FCXmJjoJk2a5E6ePOn3+GXte+fK3n+TJk1yDRs2dDVq1PDbP9u2bXNdunRxkZGRrm7duu6+++5zO3bscJLc0qVLffcvz9kiF/o6r1271rVr186Fh4e7Ro0auUcffdS9/fbbpV6/nj17ulatWv3otoFA8Th3zl8CAhAUw4cP1xtvvKH8/PxgjwIAl4TvXAAAAFPEBQAAMMXHIgAAwBRHLgAAgCniAgAAmCIuAACAqYD/Ea3i4mIdPHhQ0dHR/LlaAAAqCeecjh07poYNG6pGjR8+NhHwuDh48KASEhICvVkAAGAgKyurzD/Nf7aAx0XJTx9nZWWV61cSAQBA8OTl5SkhIcH3Pv5DAh4XJR+FxMTEEBcAAFQyF/KVBr7QCQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATAX8V1F9VsZKkUHbOgCgIg1xwZ4AQcSRCwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApi4qLrKzszVmzBg1bdpUXq9XCQkJGjRokNLS0qznAwAAlUxoee+wb98+XX/99apdu7bmzJmjtm3b6vTp0/r73/+uUaNG6dNPP62IOQEAQCVR7rh48MEH5fF4tH37dkVFRfmWt2rVSiNGjCi1fmFhoQoLC33X8/LyLnJUAABQGZTrY5EjR47onXfe0ahRo/zCokTt2rVLLUtNTVVsbKzvkpCQcNHDAgCAn75yxcWXX34p55xatGhxwfeZNGmScnNzfZesrKxyDwkAACqPcn0s4pyTJHk8ngu+j9frldfrLd9UAACg0irXkYtmzZrJ4/Foz549FTUPAACo5MoVF3Xq1NHNN9+s+fPnq6CgoNTt33//vdVcAACgkir337l4/vnndebMGXXu3FlvvvmmvvjiC+3Zs0d/+tOf1KVLl4qYEQAAVCLlPhU1KSlJO3bs0OzZs/XII4/o0KFDqlu3rjp27KgFCxZUxIwAAKAS8biSb2kGSF5enmJjY5W7SIqJDOSWAQABMySgby0IAN/7d26uYmJifnBdflsEAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgKnQoG35rlwpJiZomwcAABWDIxcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAVGjQtrwyVooM2tYBAKiahrhgT8CRCwAAYIu4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApsodF8OHD5fH4/Fd4uLi1K9fP3388ccVMR8AAKhkLurIRb9+/XTo0CEdOnRIaWlpCg0N1cCBA61nAwAAlVDoxdzJ6/UqPj5ekhQfH68JEyaoR48e+u9//6u6dev6rVtYWKjCwkLf9by8vEsYFwAA/NRd8ncu8vPztXz5cl111VWKi4srdXtqaqpiY2N9l4SEhEvdJAAA+Am7qLhYt26datWqpVq1aik6Olpr1qzRihUrVKNG6YebNGmScnNzfZesrKxLHhoAAPx0XVRc3HDDDcrMzFRmZqY++OAD9e3bV7fccov2799fal2v16uYmBi/CwAAqLou6jsXUVFRuuqqq3zXO3bsqNjYWC1atEizZs0yGw4AAFQ+Jn/nwuPxqEaNGjpx4oTFwwEAgErsoo5cFBYWKjs7W5J09OhRzZs3T/n5+Ro0aJDpcAAAoPK5qLh455131KBBA0lSdHS0WrRooddff129evWynA0AAFRCHuecC+QG8/LyFBsbq9xFUkxkILcMAEA1MKRi3tZ979+5uT96cga/LQIAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAFHEBAABMERcAAMAUcQEAAEwRFwAAwBRxAQAATBEXAADAVGjQtnxXrhQTE7TNAwCAisGRCwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGCKuAAAAKaICwAAYIq4AAAApogLAABgirgAAACmiAsAAGAqNGhbXhkrRQZt6wDKY4gL9gQAKhGOXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMHVRcbFt2zaFhISoX79+1vMAAIBK7qLiYsmSJRozZoy2bt2qAwcOWM8EAAAqsdDy3qGgoEArV65URkaGsrOz9dJLL2nq1KnnXb+wsFCFhYW+63l5eRc3KQAAqBTKfeRixYoVat68uZo3b66hQ4dq6dKlcs6dd/3U1FTFxsb6LgkJCZc0MAAA+Gkrd1wsXrxYQ4cOlST169dP+fn5SktLO+/6kyZNUm5uru+SlZV18dMCAICfvHLFxWeffabt27frnnvukSSFhobq7rvv1pIlS857H6/Xq5iYGL8LAACousr1nYvFixerqKhIjRo18i1zzqlmzZo6evSoLrvsMvMBAQBA5XLBRy6Kioq0bNkyPf3008rMzPRddu7cqcTERC1fvrwi5wQAAJXEBR+5WLdunY4eParf/va3io2N9bvtzjvv1OLFizV69GjzAQEAQOVywUcuFi9erD59+pQKC0m64447lJmZqR07dpgOBwAAKp8LPnKxdu3a897WoUOHHzwdFQAAVB/8tggAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU6FB2/JduVJMTNA2DwAAKgZHLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAKeICAACYIi4AAIAp4gIAAJgiLgAAgCniAgAAmCIuAACAqdBAb9A5J0nKy8sL9KYBAMBFKnnfLnkf/yEBj4ucnBxJUkJCQqA3DQAALtGxY8cUGxv7g+sEPC7q1KkjSTpw4MCPDgdbeXl5SkhIUFZWlmJiYoI9TrXBfg8e9n1wsN+DpyL3vXNOx44dU8OGDX903YDHRY0a//uaR2xsLP/ogiQmJoZ9HwTs9+Bh3wcH+z14KmrfX+hBAb7QCQAATBEXAADAVMDjwuv1atq0afJ6vYHedLXHvg8O9nvwsO+Dg/0ePD+Vfe9xF3JOCQAAwAXiYxEAAGCKuAAAAKaICwAAYIq4AAAApogLAABgKuBx8fzzzyspKUnh4eHq2LGjtmzZEugRqp3U1FRde+21io6OVr169fTLX/5Sn332WbDHqnZSU1Pl8Xg0bty4YI9S5X377bcaOnSo4uLiFBkZqWuuuUYffvhhsMeq8oqKivT4448rKSlJERERatq0qWbOnKni4uJgj1blbN68WYMGDVLDhg3l8Xi0evVqv9udc5o+fboaNmyoiIgI9erVS7t37w7YfAGNixUrVmjcuHGaMmWKPvroI3Xv3l233HKLDhw4EMgxqp1NmzZp1KhRev/997VhwwYVFRWpb9++KigoCPZo1UZGRoYWLlyotm3bBnuUKu/o0aO6/vrrVbNmTb399tv65JNP9PTTT6t27drBHq3Ke/LJJ/XCCy9o3rx52rNnj+bMmaO5c+fqueeeC/ZoVU5BQYHatWunefPmlXn7nDlz9Mwzz2jevHnKyMhQfHy8brrpJh07diwwA7oA6ty5sxs5cqTfshYtWriJEycGcoxq7/Dhw06S27RpU7BHqRaOHTvmmjVr5jZs2OB69uzpxo4dG+yRqrQJEya4bt26BXuMamnAgAFuxIgRfstuv/12N3To0CBNVD1Icn/9619914uLi118fLz7wx/+4Ft28uRJFxsb61544YWAzBSwIxenTp3Shx9+qL59+/ot79u3r7Zt2xaoMSApNzdX0v//Qi0q1qhRozRgwAD16dMn2KNUC2vWrFGnTp30q1/9SvXq1VP79u21aNGiYI9VLXTr1k1paWn6/PPPJUk7d+7U1q1b1b9//yBPVr3s3btX2dnZfu+3Xq9XPXv2DNj7bcB+FfW7777TmTNnVL9+fb/l9evXV3Z2dqDGqPacc3r44YfVrVs3tW7dOtjjVHmvvfaaduzYoYyMjGCPUm18/fXXWrBggR5++GFNnjxZ27dv10MPPSSv16thw4YFe7wqbcKECcrNzVWLFi0UEhKiM2fOaPbs2Ro8eHCwR6tWSt5Ty3q/3b9/f0BmCPhPrns8Hr/rzrlSy1BxRo8erY8//lhbt24N9ihVXlZWlsaOHat3331X4eHhwR6n2iguLlanTp2UkpIiSWrfvr12796tBQsWEBcVbMWKFXrllVf06quvqlWrVsrMzNS4cePUsGFDJScnB3u8aieY77cBi4vLL79cISEhpY5SHD58uFRdoWKMGTNGa9as0ebNm9W4ceNgj1Plffjhhzp8+LA6duzoW3bmzBlt3rxZ8+bNU2FhoUJCQoI4YdXUoEEDXX311X7LWrZsqTfffDNIE1Ufjz76qCZOnKh77rlHktSmTRvt379fqampxEUAxcfHS/rfEYwGDRr4lgfy/TZg37kICwtTx44dtWHDBr/lGzZsUNeuXQM1RrXknNPo0aO1atUqpaenKykpKdgjVQu9e/fWrl27lJmZ6bt06tRJ9957rzIzMwmLCnL99deXOtX6888/V2JiYpAmqj6OHz+uGjX831ZCQkI4FTXAkpKSFB8f7/d+e+rUKW3atClg77cB/Vjk4Ycf1q9//Wt16tRJXbp00cKFC3XgwAGNHDkykGNUO6NGjdKrr76qv/3tb4qOjvYdPYqNjVVERESQp6u6oqOjS32vJSoqSnFxcXzfpQKNHz9eXbt2VUpKiu666y5t375dCxcu1MKFC4M9WpU3aNAgzZ49W1dccYVatWqljz76SM8884xGjBgR7NGqnPz8fH355Ze+63v37lVmZqbq1KmjK664QuPGjVNKSoqaNWumZs2aKSUlRZGRkRoyZEhgBgzIOSlnmT9/vktMTHRhYWGuQ4cOnA4ZAJLKvCxdujTYo1U7nIoaGGvXrnWtW7d2Xq/XtWjRwi1cuDDYI1ULeXl5buzYse6KK65w4eHhrmnTpm7KlCmusLAw2KNVORs3bizzv+vJycnOuf+djjpt2jQXHx/vvF6v69Gjh9u1a1fA5vM451xgMgYAAFQH/LYIAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMEVcAAAAU8QFAAAwRVwAAABTxAUAADBFXAAAAFPEBQAAMPV/7sP4aUJGBWsAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Horizontal Bar graph\n",
    "x=['A','B','C']\n",
    "y=[5,10,8]\n",
    "plt.barh(x,y, color='orange')\n",
    "plt.title(\"Example:Horizontal bar\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "9c641074-f663-411e-bc57-39358cc0bd92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Scatter Plot\n",
    "x=['A','B','C']\n",
    "y=[5,10,8]\n",
    "plt.scatter(x,y, color='purple')\n",
    "plt.title(\"Example:Scatter Plot\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "dcf88f09-ba43-406c-ba14-03e328af8047",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Histogram\n",
    "import numpy as np\n",
    "data=np.random.randn(1000)\n",
    "plt.hist(data, bins=30, color='lightblue')\n",
    "plt.title(\"histogram\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "f91ce243-7cc2-4932-b3f2-573bb20cafaa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Example:Pie Chart')"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Pie chart\n",
    "a=['Apple','Mango','Grapes']\n",
    "size=[45,70,32]\n",
    "plt.pie(size,labels=a,autopct='%1.1f%%' , startangle=90)\n",
    "plt.title(\"Example:Pie Chart\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "2c505322-0e45-429f-aa88-c9ddea5d11bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Box Graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "59115e82-4939-48f3-a749-ce2a15751990",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Cluster Chart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "b5c1fb86-d64b-41b3-b4c5-06f722c4ae31",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Error Bar Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "c6876c99-3f70-4c35-a719-f7026d69b859",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Stack Bar Graph"
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
