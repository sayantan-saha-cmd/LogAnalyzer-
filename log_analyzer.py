import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
from collections import Counter

def analyze_failed_logins(file_path, output_widget):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {file_path}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read CSV file.\n{e}")
        return

    required_columns = {"timestamp", "username", "ip_address", "status"}
    if not required_columns.issubset(df.columns):
        messagebox.showerror("CSV Format Error", f"CSV must contain columns: {', '.join(required_columns)}")
        return

    failed_logins = df[df["status"] == "FAILED"]
    ip_counts = Counter(failed_logins["ip_address"])
    suspicious_ips = {ip: count for ip, count in ip_counts.items() if count > 2}

    suspicious_df = pd.DataFrame(list(suspicious_ips.items()), columns=["IP Address", "Failed Attempts"])
    output_file = "suspicious_ips_report.csv"
    suspicious_df.to_csv(output_file, index=False)

    output_widget.delete("1.0", tk.END)
    output_widget.insert(tk.END, f"Total Failed Logins: {len(failed_logins)}\n\n")
    output_widget.insert(tk.END, "Failed Login Attempts by IP:\n")
    for ip, count in ip_counts.items():
        output_widget.insert(tk.END, f"{ip} -> {count} times\n")

    output_widget.insert(tk.END, "\nSuspicious IPs (More than 2 Failed Attempts):\n")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            output_widget.insert(tk.END, f"{ip} is suspicious ⚠️ ({count} attempts)\n")
    else:
        output_widget.insert(tk.END, "No suspicious IPs found.\n")

    output_widget.insert(tk.END, f"\nSuspicious IP report saved as '{output_file}'\n")

def browse_file(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

root = tk.Tk()
root.title("LogAnalyzr - GUI")

tk.Label(root, text="CSV Log File Path:").pack(pady=5)
path_entry = tk.Entry(root, width=60)
path_entry.pack(padx=10)
tk.Button(root, text="Browse", command=lambda: browse_file(path_entry)).pack(pady=5)

tk.Button(root, text="Analyze Logins", command=lambda: analyze_failed_logins(path_entry.get(), output_box)).pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=80, height=20)
output_box.pack(padx=10, pady=10)

root.mainloop()
