{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dcffaf31-614f-4c6d-8f3d-75f3f1f8474a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table created successfully.\n"
     ]
    }
   ],
   "source": [
    "# database mysql connectivity with using python\n",
    "import sqlite3\n",
    "com = sqlite3.connect(\"College.db\")\n",
    "cursor = com.cursor()\n",
    "cursor.execute('''\n",
    "CREATE TABLE IF NOT EXISTS student (\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
    "    name TEXT NOT NULL,\n",
    "    age INTEGER,\n",
    "    grade TEXT\n",
    ")\n",
    "''')\n",
    "v.commit()\n",
    "print(\"Table created successfully.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5d169d51-8fa2-4ff9-8981-c004c6ee19f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student inserted successfully.\n",
      "Student inserted successfully.\n"
     ]
    }
   ],
   "source": [
    "def in_st(name, age, grade):\n",
    "    cursor.execute(\"INSERT INTO student (name, age, grade) VALUES (?, ?, ?)\", (name, age, grade))\n",
    "    v.commit()\n",
    "    print(\"Student inserted successfully.\")\n",
    "\n",
    "\n",
    "in_st('Riya', 20, 'A')\n",
    "in_st('Sneha', 22, 'B')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b448d3f6-f1fc-4fb0-bd82-8ea7c67994d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 'Riya', 20, 'A')\n",
      "(2, 'Sneha', 22, 'B')\n"
     ]
    }
   ],
   "source": [
    "def fetch_students():\n",
    "    cursor.execute(\"SELECT * FROM student\")\n",
    "    rows = cursor.fetchall()\n",
    "    for row in rows:\n",
    "        print(row)\n",
    "\n",
    "\n",
    "fetch_students()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5b109fde-33f4-42f7-a609-bd8cf7a1be2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student updated successfully.\n"
     ]
    }
   ],
   "source": [
    "def update_student(student_id, new_name, new_age, new_grade):\n",
    "    cursor.execute(\"UPDATE student SET name=?, age=?, grade=? WHERE id=?\", (new_name, new_age, new_grade, student_id))\n",
    "    com.commit()\n",
    "    print(\"Student updated successfully.\")\n",
    "update_student(1, 'Riya Sharma', 21, 'A+')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0397e64f-02a4-4191-8193-63d156b2cf1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student deleted successfully.\n"
     ]
    }
   ],
   "source": [
    "def delete_student(student_id):\n",
    "    cursor.execute(\"DELETE FROM student WHERE id=?\", (student_id,))\n",
    "    com.commit()\n",
    "    print(\"Student deleted successfully.\")\n",
    "\n",
    "\n",
    "delete_student(2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "227603b1-bc87-45c6-b164-172223a31f87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Database connection closed.\n"
     ]
    }
   ],
   "source": [
    "com.close()\n",
    "print(\"Database connection closed.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "157fbdca-dc26-4563-bf65-644f8dd47620",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n",
      "[[1 2]\n",
      " [3 4]]\n"
     ]
    }
   ],
   "source": [
    "# numpy\n",
    "import numpy as np\n",
    "# array\n",
    "a = np.array([1,2,3])\n",
    "b = np.array([[1,2],[3,4]])\n",
    "print(a)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "42bcef31-3a56-4340-9a5e-2f032a1624eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n",
      "6\n",
      "2\n",
      "int64\n"
     ]
    }
   ],
   "source": [
    "twoD = np.array([[1,2,3],[4,5,6]])\n",
    "# array function\n",
    "print(twoD.shape)\n",
    "print(twoD.size)\n",
    "print(twoD.ndim)\n",
    "print(twoD.dtype)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6615a1bf-ea7d-4078-8e93-f001080c35be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]\n",
      " [5 6]]\n"
     ]
    }
   ],
   "source": [
    "# reshape\n",
    "twoD = np.array([1,2,3,4,5,6])\n",
    "print(twoD.reshape(3,2))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4bf1e18c-5666-4fac-a6e6-43075d1e402a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n",
      "[99  2  3]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "# copy\n",
    "a = np.array([1, 2, 3])\n",
    "b = a.copy()\n",
    "c = a.view()\n",
    "\n",
    "a[0] = 99\n",
    "\n",
    "print(b)  # [1 2 3] (copy remains same)\n",
    "print(c)  # [99 2 3] (view reflects change)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e16cf5e3-448d-429f-b500-6461d9f9e4ff",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Zeros Matrix: \n",
      " [[0. 0. 0.]\n",
      " [0. 0. 0.]]\n",
      "Ones Matrix: \n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]]\n",
      "Identity Matrix: \n",
      " [[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n",
      "Full Matrix:\n",
      " [[7 7 7]\n",
      " [7 7 7]]\n",
      "Arranged Matrix:\n",
      " [1 3]\n",
      "linspace Matrix:\n",
      " [1. 4. 7.]\n"
     ]
    }
   ],
   "source": [
    "#twoD = np.array([[1,2,3],[4,5,6]])\n",
    "print(\"Zeros Matrix: \\n\",np.zeros((2,3)))\n",
    "print(\"Ones Matrix: \\n\",np.ones((3,3)))\n",
    "print(\"Identity Matrix: \\n\",np.eye(3,3)) \n",
    "print(\"Full Matrix:\\n\",np.full((2,3),7))\n",
    "print(\"Arranged Matrix:\\n\",np.arange(1,5,2))\n",
    "print(\"linspace Matrix:\\n\",np.linspace(1,7,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3e845e7d-18d8-4fa2-82ac-3b825e6e781d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition of matrix:  [26  7  4]\n",
      "Multiplication of corresponding elements:  [69 12  4]\n",
      "Exponent Matrix:  [ 9 16  4]\n",
      "Square of a Matrix:  [4.79583152 1.73205081 1.41421356]\n",
      "Mean of a Matrix:  3.0\n"
     ]
    }
   ],
   "source": [
    "a = np.array([23,3,2])\n",
    "b = np.array([3,4,2])\n",
    "# mathematical operation\n",
    "print(\"Addition of matrix: \",a+b)\n",
    "print(\"Multiplication of corresponding elements: \",a * b)\n",
    "print(\"Exponent Matrix: \",b ** 2)\n",
    "print(\"Square of a Matrix: \",np.sqrt(a))\n",
    "print(\"Mean of a Matrix: \",np.mean(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "52a1d576-549b-4303-b6ed-e8e29be0ebc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n",
      "1\n",
      "9\n",
      "[ 5 15  9]\n",
      "[10 19]\n",
      "[[1 3 6]\n",
      " [4 6 9]]\n",
      "[1 6 3 4 9 6]\n",
      "[[1 4]\n",
      " [6 9]\n",
      " [3 6]]\n"
     ]
    }
   ],
   "source": [
    "twoD = np.array([[1,6,3],[4,9,6]])\n",
    "print(np.sum(twoD))\n",
    "print(np.min(twoD))\n",
    "print(np.max(twoD))\n",
    "print(np.sum(twoD,axis=0)) #column wise sum\n",
    "print(np.sum(twoD,axis=1)) #row wise sum\n",
    "print(np.sort(twoD))\n",
    "print(twoD.flatten()) # converted to array\n",
    "print(twoD.T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e3de7794-c0c2-46b6-b109-a493f4544db4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[14 39 24]\n",
      " [13 63 33]]\n"
     ]
    }
   ],
   "source": [
    "# matrix multiplication \n",
    "b = np.array([[1,6,3],[4,9,6]])\n",
    "a = np.array([[2,3],[9,1]])\n",
    "print(np.dot(a,b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a6785edf-443f-4759-a442-f5c2deaa5f00",
   "metadata": {},
   "outputs": [],
   "source": [
    "#metplotlib\n",
    "#seaborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6546cd29-9cd7-4eed-8ef7-a86e751fc51a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f0fff76a-4de1-48e0-b0df-9c5312456f2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': ['Sneha', 'Riya', 'Khushi'], 'Age': [19, 19, 18]}\n"
     ]
    }
   ],
   "source": [
    "# from dictionary\n",
    "data = {\n",
    "    \"Name\" : [\"Sneha\",\"Riya\",\"Khushi\"], # dictionary with multiple values \n",
    "    \"Age\" : [19,19,18]}\n",
    "\n",
    "\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4b931774-b5e4-41bf-9403-a17fdf254772",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  1  2  3  4  5  6  7  8  9 10]\n"
     ]
    }
   ],
   "source": [
    "# Que1: Create a NumPy array of integers from 0 to 10.\n",
    "print(np.arange(0,11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9efb7a63-f686-4a58-8fec-e9559c455266",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "# Que2: Create an array of 10 zeros and change the 5th value to 1.\n",
    "arr = np.zeros((10))\n",
    "arr[5] = 1\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c02bf8c5-b8ec-4e6c-be58-9744273449bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\n"
     ]
    }
   ],
   "source": [
    "# Que3: Generate an array of 10 ones.\n",
    "print(np.ones((10)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5362fc3d-6752-421a-9e7a-1fc1646e0999",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.         0.05263158 0.10526316 0.15789474 0.21052632 0.26315789\n",
      " 0.31578947 0.36842105 0.42105263 0.47368421 0.52631579 0.57894737\n",
      " 0.63157895 0.68421053 0.73684211 0.78947368 0.84210526 0.89473684\n",
      " 0.94736842 1.        ]\n"
     ]
    }
   ],
   "source": [
    "# Que4: Create a 1D array of 20 equally spaced numbers between 0 and 1.\n",
    "print(np.linspace(0,1,20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "67b59f78-bf7f-4cf7-b9d9-f5f06a413fe9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# Que5: Create a 3x3 identity matrix.\n",
    "print(np.eye(3,3)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "4251a57c-ec70-4c79-8ce0-386722d36b71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix 4x4:\n",
      " [[ 0  1  2  3]\n",
      " [ 4  5  6  7]\n",
      " [ 8  9 10 11]\n",
      " [12 13 14 15]]\n"
     ]
    }
   ],
   "source": [
    "# Que6: Create a 4x4 matrix with values from 0 to 15.\n",
    "arr = np.arange(0, 16).reshape(4, 4)\n",
    "print(\"Matrix 4x4:\\n\", arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "6c20777c-127a-4345-aa9d-c426cadd67e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix 5x5:\n",
      " [[49 91 68 48 89]\n",
      " [50 35 34 24 91]\n",
      " [88 23 79  9 62]\n",
      " [57 91 70 71 14]\n",
      " [ 4 58 14 10  4]]\n"
     ]
    }
   ],
   "source": [
    "# Que7: Generate a 5x5 matrix with random values.\n",
    "arr = np.random.randint(1, 101, size=(5, 5))\n",
    "print(\"Matrix 5x5:\\n\", arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6c712e8a-97e7-4629-b606-1e69d29403ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12 90 21 78]\n"
     ]
    }
   ],
   "source": [
    "# Que8: Reverse the elements of an array.\n",
    "arr = np.array([78,21,90,12])\n",
    "print(np.flip(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "77b3286c-2691-45b2-bb31-d10534e6b502",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[21 34 89 23]\n"
     ]
    }
   ],
   "source": [
    "# Que9: Flatten a 2D array to 1D.\n",
    "twoD = np.array([[21,34],[89,23]]) # 2D\n",
    "print(twoD.flatten()) # 1D"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c6fbf8f2-299a-422e-b324-52ae4e5b4891",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "78\n",
      "90\n",
      "12\n"
     ]
    }
   ],
   "source": [
    "# Que10: Extract even numbers from an array\n",
    "arr = np.array([78,21,90,12])\n",
    "for i in arr:\n",
    "    if i%2==0:\n",
    "        print(i)"
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
