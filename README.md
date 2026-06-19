# 🛡️ Standalone DLP (Data Loss Prevention) System

A Python-based Standalone Data Loss Prevention (DLP) solution that monitors files in real time, detects sensitive information, classifies data, and enforces security policies to prevent data leakage.

---

## 📌 Overview

This project simulates the core functionality of an enterprise DLP solution by continuously monitoring files, identifying sensitive information, classifying content, and applying security actions such as Allow, Warn, Block, or Quarantine.

The system is designed as a cybersecurity learning project to understand how modern DLP products protect organizational data.

---

## 🚀 Features

### Real-Time Monitoring

* Monitors files using Watchdog
* Detects newly created files instantly

### Sensitive Data Detection

* PAN Card Numbers
* Aadhaar Numbers
* Email Addresses
* Custom Sensitive Keywords

### AI-Style Classification

* Context-based classification using keyword matching
* Identifies confidential business content

### Policy Enforcement

* Allow
* Warn
* Block
* Quarantine

### Incident Management

* Logs incidents
* Stores events in SQLite database
* Displays incidents in a Flask Dashboard

### File Support

* TXT files
* DOCX files

---

## 🏗️ Architecture

```text
File Created
      │
      ▼
Content Scanner
      │
      ▼
Sensitive Data Detection
(PAN / Aadhaar / Email / Keywords)
      │
      ▼
Data Classification
      │
      ▼
Policy Engine
      │
      ▼
Allow / Warn / Block / Quarantine
      │
      ▼
SQLite Database
      │
      ▼
Flask Dashboard
```

---

## 📂 Project Structure

```text
DLPTool/
│
├── main.py                # Main DLP Agent
├── scanner.py             # Pattern Detection Engine
├── classifier.py          # Data Classification
├── ai_classifier.py       # AI-style Classification
├── policy.py              # Policy Enforcement
├── file_reader.py         # File Reading Logic
├── logger.py              # Logging Module
├── database.py            # SQLite Functions
├── dashboard.py           # Flask Dashboard
├── policies.json          # Security Policies
├── monitored/             # Monitored Folder
├── quarantine/            # Quarantined Files
└── dlp.db                 # SQLite Database
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AksharaAlagarsamy/DLP-Standalone.git
cd DLP-Standalone
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install flask watchdog python-docx
```

---

## ▶️ Run the DLP Agent

```bash
python3 main.py
```

Expected output:

```text
================================
DLP Agent Running...
Monitoring: monitored
================================
```

---

## 🌐 Run the Dashboard

```bash
python3 dashboard.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🧪 Example Detection

Example file:

```text
Employee PAN: ABCDE1234F
```

Output:

```text
FINDINGS: ['PAN']
CLASSIFICATION: CONFIDENTIAL
ACTION: BLOCK
```

---

## 🛡️ Security Policies

| Classification | Action     |
| -------------- | ---------- |
| PUBLIC         | ALLOW      |
| INTERNAL       | WARN       |
| CONFIDENTIAL   | BLOCK      |
| RESTRICTED     | QUARANTINE |

---

## 📊 Technologies Used

* Python
* Flask
* SQLite
* Watchdog
* Regex
* Ubuntu / WSL

---

## 🔮 Future Enhancements

* Machine Learning Classification
* PDF Scanning
* Email DLP Integration
* USB Monitoring
* User Authentication
* Advanced Analytics Dashboard

---

## 👨‍💻 Author

**AksharaAlagasramy**

Cybersecurity enthusiast focused on:

* Data Loss Prevention (DLP)
* Endpoint Security
* SOC Operations
* Threat Detection
* Data Classification

---

## 📜 Disclaimer

This project is developed for educational and learning purposes to understand the working principles of enterprise Data Loss Prevention (DLP) solutions.
