# 🔍 Legacy Module Analysis Report

## 📁 Module: `legacy_customer.py`

The current Customer Management module was written using **procedural programming** and lacks software engineering best practices. Below are the major problems identified:

---

### 🧠 Key Issues in the Legacy Module

#### 1. **No Object-Oriented Design**
- All logic is written using plain functions and global variables.
- There is no use of classes to represent real-world entities like `Customer`.

#### 2. **No Modularity / Tight Coupling**
- All operations directly access and modify the same `customers` list.
- There's no separation of data management and business logic.

#### 3. **Code Duplication**
- The code structure may lead to repeated loops and logic in larger systems.
- Adding new features would require changes in multiple places.

#### 4. **No Unit Testing Support**
- Functions are tightly coupled with the data store.
- There is no clear input/output structure to easily test individual components.

#### 5. **Poor Readability**
- The structure is linear with no comments, classes, or separation of concerns.
- Functionality is directly tied to a shared global list (`customers`).

#### 6. **Violations of SOLID Principles**
| Principle | Violation |
|----------|-----------|
| SRP (Single Responsibility) | Each function does multiple things |
| OCP (Open/Closed) | Code must be modified to add features |
| DRY (Don't Repeat Yourself) | Risk of repeating similar logic |
| LSP (Liskov Substitution) | Not applicable due to lack of inheritance |
| DIP (Dependency Inversion) | No abstraction or interface usage |

---

## 🧩 Conclusion

This legacy module is fragile and difficult to maintain or extend. To address these issues, we will refactor the code using:

- **OOP (Object-Oriented Programming)**
- **SOLID Design Principles**
- **Modular Structure**
- **Test-Driven Development**
