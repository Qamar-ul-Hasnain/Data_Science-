{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fd27061-234b-4901-9c3f-1313d33b3ba0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Simple Calculator\n"
     ]
    }
   ],
   "source": [
    "print(\"Simple Calculator\")\n",
    "\n",
    "# Get input from user\n",
    "num1 = float(input(\"Enter first number: \"))\n",
    "num2 = float(input(\"Enter second number: \"))\n",
    "operator = input(\"Enter operator (+, -, *, /): \")\n",
    "\n",
    "\n",
    "if operator == '+':\n",
    "    result = num1 + num2\n",
    "elif operator == '-':\n",
    "    result = num1 - num2\n",
    "elif operator == '*':\n",
    "    result = num1 * num2\n",
    "elif operator == '/':\n",
    "    if num2 != 0:  \n",
    "        result = num1 / num2\n",
    "    else:\n",
    "        result = \"Error! Division by zero is not allowed.\"\n",
    "else:\n",
    "    result = \"Error! Invalid operator.\"\n",
    "\n",
    "# Display the result\n",
    "print(f\"Result: {result}\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abab5c6b-df35-48c8-ba81-e774f3bf0493",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
