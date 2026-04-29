# 🏢 Classes Used in the Project

---

## 1️⃣ Employee Class (Parent Class)

This is the **Base Class** of the project.

### 📌 Attributes

* Employee ID
* Name
* Age
* Salary

### 📌 Methods

* `__init__()` → Constructor
* `get_data()` → Getter Method
* `set_data()` → Setter Method
* `display()` → Display Employee Details

---

## 2️⃣ Manager Class (Child Class)

This class inherits properties from Employee class.

### 📌 Extra Attribute

* Department

### 📌 Methods

* Constructor using `super()`
* Overridden `display()` Method

### 📌 Purpose

Used to store Manager-specific information with employee details.

---

## 3️⃣ Developer Class (Child Class)

This class also inherits properties from Employee class.

### 📌 Extra Attribute

* Programming Language

### 📌 Methods

* Constructor using `super()`
* Overridden `display()` Method

### 📌 Purpose

Used to store Developer details along with programming language.

---

# 🔥 OOP Concepts Used

---

## 🔹 1. Inheritance

Inheritance allows child classes to use parent class properties.

### Example:

```python
class Manager(Employee):
```

This reduces code repetition and improves reusability.

---

## 🔹 2. Constructor (`__init__`)

Used to initialize object values automatically.

### Example:

```python
def __init__(self, employee_id, name, age, salary):
```

---

## 🔹 3. Method Overriding

Child classes redefine the `display()` method according to their own needs.

This concept is known as **Method Overriding**.

---

## 🔹 4. `super()` Function

Used to call parent class constructor and methods.

### Example:

```python
super().__init__(employee_id, name, age, salary)
```

It helps in accessing parent class features easily.

---

## 🔹 5. Encapsulation

Private variables are created using double underscore (`__`).

### Example:

```python
self.__salary
```

This protects data from direct access.

---

## 🔹 6. Getter and Setter

### Getter → Used to access private data

### Setter → Used to modify private data

### Example:

```python
def get_data(self):
```

```python
def set_data(self):
```

---

## 🔹 7. `issubclass()` Function

Used to check whether one class is subclass of another.

### Example:

```python
issubclass(Manager, Employee)
```

### Output:

```python
True
```

---

# 🔄 Program Flow

At the beginning, the program checks:

```python
Manager is subclass of Employee = True
```

Then the following menu appears:

```text
1. Employee Data
2. Manager Data
3. Developer Data
4. Exit
```

### User Choices:

### 👉 Choice 1 → Employee Details

### 👉 Choice 2 → Manager Details

### 👉 Choice 3 → Developer Details

### 👉 Choice 4 → Exit Program

If wrong input is entered → Invalid message shown.

---

# 💻 Sample Output

```text
Manager is subclass of Employee = True

1. EMPLOYEE DATA
2. MANAGER DATA
3. DEVELOPER DATA
4. EXIT

ENTER YOUR CHOICE : 3

ID : 103
NAME : RAHUL
AGE : 22
SALARY : 16LAC
PROGRAMME : PYTHON
```

---

# ✅ Advantages of the Project

✔ Simple and easy to understand
✔ Best for beginners
✔ Strong OOP concept practice
✔ Real-world example of employee management
✔ Reusable code using inheritance
✔ Helpful for Viva and Practical Exams
✔ Attractive menu-driven structure

---

# ❌ Limitations

### Some current limitations are:

* No database connection
* No file handling
* Static values used
* No permanent data storage
* No login system

These can be improved in future versions.

---

# 🚀 Future Improvements

This project can be upgraded by adding:

### 🔸 MySQL Database Connection

### 🔸 File Handling System

### 🔸 Login Authentication

### 🔸 Search Employee Feature

### 🔸 Update/Delete Records

### 🔸 GUI using Tkinter

### 🔸 Web Version using Django/Flask

---

# 🎓 Conclusion

The **Employee Management System** is a simple yet highly effective Python OOP project that helps students understand important concepts like inheritance, constructors, method overriding, encapsulation, getter-setter methods, and subclass relationships.

This project is extremely useful for:

✔ College Practical Submission
✔ Viva Examination
✔ Python OOP Lab Work
✔ Mini Project Presentation
✔ Strengthening Programming Basics

It builds confidence in Python programming and improves logical thinking.

---

# 👨‍💻 Developed By

## Student Project – Python OOP Practical

### Created for Academic Learning, Viva, and Project Submission Purpose

---

# ⭐ Thank You ⭐
