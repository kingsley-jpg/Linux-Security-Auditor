# Linux Security Auditor

A Python-based Linux security auditing tool that performs automated checks for security-sensitive system configurations, file permissions, running processes, network exposure, and overall system risk.

This project was built as a practical cybersecurity project to strengthen Linux security, Python scripting, system auditing, and security assessment skills.

## Features

### 👤 User Audit

* Displays the current username
* Displays UID and GID
* Identifies the account running the auditor

### 🖥️ System Information

Collects basic system information including:

* Operating system
* Kernel release
* CPU architecture
* Hostname
* Python version

### 🔐 SUID Binary Audit

Searches common system binary directories for SUID-enabled files.

Reports:

* File path
* File owner
* Linux permissions
* Numeric permission value

SUID binaries are security-sensitive because they can execute with the privileges of their file owner.

### 📁 World-Writable File Audit

Searches selected system directories for files and directories writable by all users.

The auditor checks:

```text
/etc
/usr/local
/opt
/var
/tmp
```

This helps identify permissions that may require further security investigation.

> Note: World-writable does not automatically mean vulnerable. Some locations, especially temporary directories, are intentionally configured this way.

### ⚙️ Process Audit

Inspects running Linux processes through `/proc`.

Reports:

* Process ID
* Process name
* Process owner
* Number of running processes
* Number of root-owned processes

### 🌐 Network Audit

Checks Linux `/proc/net` socket tables for listening:

* TCP
* TCP6
* UDP
* UDP6

This provides visibility into network services currently exposed by the system.

### 📊 Security Assessment

Generates a simple security score from 0–100 based on selected audit findings.

Example:

```text
===================================
        SECURITY ASSESSMENT
===================================
    Security Score: 60/100
    Risk Rating:    MODERATE
===================================
```

The scoring system is a project-specific heuristic and is not intended to replace professional security frameworks or vulnerability scanners.

---

## Project Structure

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

## Requirements

* Linux operating system
* Python 3.9+
* Git

The project currently uses Python's standard library, so no external Python packages are required.

---

## Installation

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

## Example Output

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
    OS Release:       6.19.14+kali-amd64
    Architecture:     x86_64
    Hostname:         dell
    Python Version:   3.13.12

[+] SUID Binary Audit
    SUID files found: 28

[+] World-Writable File Audit
    World-writable files:       9
    World-writable directories: 7

[+] Running Process Audit
    Processes detected: 201
    Root-owned processes: 131

[+] Network Listening Port Audit
    No listening network ports found.
    Listening sockets: 0

===================================
        SECURITY ASSESSMENT
===================================
    Security Score: 60/100
    Risk Rating:    MODERATE
===================================
```

---

## Security Score Methodology

The auditor begins with a score of **100** and applies deductions based on selected findings.

| Finding                    | Condition    | Deduction |
| -------------------------- | ------------ | --------: |
| SUID files                 | More than 20 |       -15 |
| SUID files                 | 11–20        |       -10 |
| World-writable files       | More than 5  |       -15 |
| World-writable files       | 1–5          |        -5 |
| World-writable directories | More than 5  |       -10 |
| World-writable directories | 1–5          |        -5 |
| Listening ports            | More than 10 |       -15 |
| Listening ports            | 1–10         |        -5 |

### Risk Ratings

|  Score | Rating    |
| -----: | --------- |
| 80–100 | GOOD      |
|  60–79 | MODERATE  |
|  40–59 | HIGH RISK |
|   0–39 | CRITICAL  |

This scoring model is intentionally simple and is designed for educational purposes.

---

## Security Considerations

The auditor reports security-relevant configurations but does not automatically classify every finding as a vulnerability.

For example:

* Some SUID binaries are legitimate system components.
* `/tmp` commonly contains world-writable directories.
* Root-owned processes are normal on Linux.
* A listening service is not necessarily vulnerable.

Findings should therefore be investigated in context.

---

## Technologies

* **Python 3**
* **Linux**
* **Linux `/proc` filesystem**
* **Git**
* **GitHub**

Python standard-library modules used include:

```text
os
platform
stat
pwd
```

---

## Learning Objectives

This project was developed to practice:

* Linux system administration
* Linux file permissions
* SUID permissions
* Process enumeration
* Network socket inspection
* Python system programming
* Security auditing
* Risk assessment
* Git and GitHub workflow

---

## Future Improvements

Planned improvements include:

* [ ] Detect suspicious SUID binaries
* [ ] Identify suspicious world-writable system files
* [ ] Map network ports to processes
* [ ] Add configuration checks
* [ ] Add password-policy auditing
* [ ] Check SSH security configuration
* [ ] Detect insecure services
* [ ] Generate JSON reports
* [ ] Generate HTML security reports
* [ ] Add automated tests
* [ ] Add command-line arguments
* [ ] Improve security scoring
* [ ] Add logging
* [ ] Add remediation recommendations

---

## Disclaimer

This project is intended for **educational, defensive, and authorized security auditing purposes**.

Only run security auditing tools on systems you own or have explicit permission to assess.

---

## Author

**Kingsley Senyedji**

Computer Science Student | Cybersecurity Enthusiast

GitHub: [@kingsley-jpg](https://github.com/kingsley-jpg)

---

## License

This project is available for educational and personal cybersecurity development.
