# Linux Security Auditor 🔐

A Python-based Linux security auditing tool that automatically checks a Linux system for common security and configuration risks, including SUID binaries, world-writable files, running processes, and exposed network services.

The project was built as a practical cybersecurity learning project to strengthen my understanding of **Linux security, system enumeration, Python automation, and security auditing**.

---

## 🎯 Project Overview

Linux systems contain many configuration settings, permissions, processes, and services that can affect their security.

Manually checking these areas can be time-consuming. The **Linux Security Auditor** automates several basic security checks and produces a simple security assessment based on the findings.

The tool is designed for **defensive security auditing and educational purposes**.

---

## ✨ Features

### 👤 User Audit

* Displays the current username
* Displays UID and GID
* Identifies the account running the audit

### 🖥️ System Information

Collects:

* Operating system
* Kernel release
* CPU architecture
* Hostname
* Python version

### 🔑 SUID Binary Audit

Searches common system directories for files with the **SUID permission bit** enabled.

SUID files are important to audit because they can execute with the privileges of their file owner.

### 📁 World-Writable File Audit

Searches selected system directories for:

* World-writable files
* World-writable directories

These permissions can introduce security risks when incorrectly configured.

### ⚙️ Process Audit

Examines running processes through `/proc` and reports:

* Number of detected processes
* Number of root-owned processes
* Process names and ownership information

### 🌐 Network Audit

Examines Linux `/proc/net` information to identify listening:

* TCP sockets
* TCP6 sockets
* UDP sockets
* UDP6 sockets

### 📊 Security Assessment

Generates a simple **0–100 security score** and risk rating based on selected findings.

Possible ratings:

|  Score | Rating    |
| -----: | --------- |
| 80–100 | GOOD      |
|  60–79 | MODERATE  |
|  40–59 | HIGH RISK |
|   0–39 | CRITICAL  |

> **Note:** The scoring system is a project-specific heuristic created for this educational tool. It is not an industry-standard security rating.

---

## 🛠️ Technologies

* **Python 3**
* Linux
* `/proc` filesystem
* Unix file permissions
* Git & GitHub
* Python standard library

No external Python packages are currently required.

---

## 📂 Project Structure

```text
linux-security-auditor/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│
├── src/
│   └── auditor.py
│
└── tests/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/kingsley-jpg/Linux-Security-Auditor.git
```

Enter the project directory:

```bash
cd Linux-Security-Auditor
```

Run the auditor:

```bash
python3 src/auditor.py
```

---

## 💻 Example Output

```text
===================================
       LINUX SECURITY AUDITOR
===================================

[+] Current User
    Username: kingsley
    UID:      1000
    GID:      1000

[+] System Information
    Operating System: Linux
    OS Release:       6.x.x
    Architecture:     x86_64
    Hostname:         kali

[+] SUID Binary Audit
    SUID files found: 28

[+] World-Writable File Audit
    World-writable files:       9
    World-writable directories: 7

[+] Running Process Audit
    Processes detected: 200+
    Root-owned processes: 100+

[+] Network Listening Port Audit
    Listening sockets: 0

===================================
        SECURITY ASSESSMENT
===================================
    Security Score: 60/100
    Risk Rating:    MODERATE
===================================
```

The exact output will vary depending on the Linux system being audited.

---

## 🔍 Security Checks

The current version focuses on four major areas:

```text
             Linux System
                  │
        ┌─────────┴─────────┐
        │                   │
   System Audit        Security Audit
        │                   │
   ┌────┼────┐        ┌─────┼─────┐
   │    │    │        │     │     │
 User System Process  SUID  Files Network
```

The collected findings are then passed to the security scoring component.

---

## 🧠 What I Learned

Building this project helped me practice:

* Linux filesystem enumeration
* Linux file permissions
* SUID permissions
* Process enumeration
* `/proc` filesystem analysis
* Network socket enumeration
* Python system programming
* Exception handling
* Security-focused automation
* Git and GitHub workflow
* Writing security tooling for defensive purposes

---

## 🔮 Future Improvements

Planned improvements include:

* [ ] JSON report generation
* [ ] HTML security reports
* [ ] CSV export
* [ ] Configurable security thresholds
* [ ] Better network-service identification
* [ ] Suspicious process detection
* [ ] File integrity monitoring
* [ ] Log analysis
* [ ] CVE/security advisory integration
* [ ] Automated remediation recommendations
* [ ] Unit tests
* [ ] CI/CD integration

---

## ⚠️ Security Considerations

The tool is intended for **authorized security auditing and educational use only**.

Some findings, such as SUID files or world-writable directories, are not automatically vulnerabilities. They require contextual analysis before determining whether they represent an actual security issue.

Always run security assessments only on systems you own or have explicit permission to assess.

---

## 📚 Project Goals

The main goals of this project are to:

1. Improve practical Linux security knowledge.
2. Develop Python-based security automation skills.
3. Understand common Linux security misconfigurations.
4. Build a foundation for more advanced security tooling.
5. Create a practical cybersecurity portfolio project.

---

## 👨‍💻 Author

**Kingsley Senyedji**

Computer Science Student | Cybersecurity Enthusiast | Python Developer

Interested in:

* Cybersecurity
* Ethical Hacking
* Linux Security
* Python
* Security Automation
* AI & Machine Learning

---

## 📄 License

This project is intended for educational and defensive security purposes.
