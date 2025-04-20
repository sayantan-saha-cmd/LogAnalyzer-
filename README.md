# 🛡️ LogAnalyzr 

## 📘 Overview

**LogAnalyzr** is a Python-based GUI application that analyzes login activity logs (in CSV, TXT, or LOG format) to identify failed login attempts and flag potentially suspicious IP addresses.

This tool is crafted for blue teamers, system administrators, and SOC analysts to detect brute-force attacks or unauthorized access attempts using simple automation and a user-friendly interface.

---

## 🚀 Key Features

- 📊 **Failed Login Analysis**: Detect and filter out all failed login attempts from log files.
- 🔍 **Suspicious IP Detection**: Flags IPs with more than 2 failed login attempts automatically.
- 📄 **Auto-Generate Reports**: Outputs a separate CSV file named `suspicious_ips_<timestamp>.csv` with all flagged IPs.
- 🖼️ **GUI Interface**: Easy-to-use interface built with `tkinter`.
- 💡 **CSV + TXT + LOG Support**: Works with `.csv`, `.log`, and `.txt` files seamlessly.
- 💾 **Offline Use**: Works entirely offline once installed.

---

## 🛠️ Installation

> Follow these steps to set up and run the LogAnalyzr GUI on your system.

### 1. Clone this repository
```bash
git clone https://github.com/sayantan-saha-cmd/LogAnalyzer-.git
cd LogAnalyzer-
pip3 install pandas
python3 log_analyzer.py
   ```
