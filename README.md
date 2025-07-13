## About the Author

This project was developed and maintained by **Ali Hashmi** — Business student delving into DevOps by replacing 4 years of university knowledge with self-learning.

# OrangeHRM Add Employee Automation

This repository contains a fully automated test suite for the **Add Employee** feature in the OrangeHRM web application. Built using Selenium WebDriver with Python and PyTest, the project follows the **Page Object Model (POM)** architecture for clarity, scalability, and maintenance.

The goal of this project is to demonstrate real-world Software QA Automation practices in a clean and modular format — ideal for QA teams and automation engineers working on HRM systems or form-heavy applications.

---

## Tools & Technologies Used

- Python 3
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- PyTest HTML Reporting
- Git & GitHub
- GitHub Actions (CI/CD)
- Screenshot Capture on Failures

---

## Folder Structure

```
OrangeHRM_AddEmployee_Automation_By_Ali_Hashmi/
│
├── Pages/                    # Page Object classes
│   ├── LoginPage.py
│   └── AddEmployeePage.py
│
├── TestCases/                # Test cases using PyTest
│   └── test_add_employee.py
│
├── Reports/                  # Test execution HTML reports
│
├── Screenshots/             # Auto-captured screenshots on failure
│
├── .github/                 # CI workflow using GitHub Actions
│   └── workflows/
│       └── run-tests.yml
│
├── README.md                # Project documentation
├── requirements.txt         # Dependency list
├── conftest.py              # PyTest setup and fixtures
└── .gitignore               # Files ignored by Git
```

---

## How to Run the Test Locally

### 1. Clone the Repository

```bash
git clone https://github.com/aliihashmiii/OrangeHRM_AddEmployee_Automation_By_Ali_Hashmi.git
cd OrangeHRM_AddEmployee_Automation_By_Ali_Hashmi
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Execute the Test

```bash
pytest TestCases/test_add_employee.py --html=Reports/report.html
```

- 📄 The test report will be available at: `Reports/report.html`
- 📸 Any failure screenshots will be stored in: `Screenshots/`

---

## Continuous Integration with GitHub Actions

This project includes a CI pipeline using GitHub Actions to automatically:

- Install dependencies  
- Run all PyTest test cases  
- Generate HTML test reports  

Workflow file: `.github/workflows/run-tests.yml`

---



---
