#!/usr/bin/env python3

import os
import platform
import stat
import pwd


def get_file_owner(uid):
    try:
        return pwd.getpwuid(uid).pw_name
    except KeyError:
        return str(uid)


def check_current_user():
    print("\n[+] Current User")
    print(f"    Username: {os.getlogin()}")
    print(f"    UID:      {os.getuid()}")
    print(f"    GID:      {os.getgid()}")


def check_system_info():
    print("\n[+] System Information")
    print(f"    Operating System: {platform.system()}")
    print(f"    OS Release:       {platform.release()}")
    print(f"    Architecture:     {platform.machine()}")
    print(f"    Hostname:         {platform.node()}")
    print(f"    Python Version:   {platform.python_version()}")


def check_suid_files():
    print("\n[+] SUID Binary Audit")

    directories = [
        "/usr/bin", "/usr/sbin", "/bin",
        "/sbin", "/usr/local/bin", "/usr/local/sbin"
    ]

    suid_files = set()

    for directory in directories:
        if not os.path.exists(directory):
            continue

        for root, dirs, files in os.walk(directory):
            for filename in files:
                path = os.path.join(root, filename)

                try:
                    file_stat = os.stat(path)

                    if file_stat.st_mode & stat.S_ISUID:
                        suid_files.add(os.path.realpath(path))

                except (PermissionError, FileNotFoundError, OSError):
                    continue

    print(f"    SUID files found: {len(suid_files)}")

    for path in sorted(suid_files):
        print(f"    [!] {path}")

    return len(suid_files)


def check_world_writable():
    print("\n[+] World-Writable File Audit")

    directories = ["/etc", "/usr/local", "/opt", "/var", "/tmp"]

    files_found = set()
    dirs_found = set()

    for directory in directories:

        if not os.path.exists(directory):
            continue

        for root, dirs, files in os.walk(directory):

            for name in dirs:
                path = os.path.join(root, name)

                try:
                    if os.stat(path).st_mode & stat.S_IWOTH:
                        dirs_found.add(path)
                except (PermissionError, FileNotFoundError, OSError):
                    continue

            for name in files:
                path = os.path.join(root, name)

                try:
                    if os.stat(path).st_mode & stat.S_IWOTH:
                        files_found.add(path)
                except (PermissionError, FileNotFoundError, OSError):
                    continue

    print(f"    World-writable files:       {len(files_found)}")
    print(f"    World-writable directories: {len(dirs_found)}")

    return len(files_found), len(dirs_found)


def check_processes():
    print("\n[+] Running Process Audit")

    processes = []

    try:
        entries = os.listdir("/proc")
    except PermissionError:
        print("    [!] Permission denied")
        return 0

    for pid in entries:

        if not pid.isdigit():
            continue

        try:
            with open(
                f"/proc/{pid}/status",
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                uid = None
                name = "Unknown"

                for line in f:

                    if line.startswith("Name:"):
                        name = line.split(":", 1)[1].strip()

                    elif line.startswith("Uid:"):
                        uid = int(line.split()[1])

                if uid is not None:
                    processes.append(
                        {
                            "pid": pid,
                            "name": name,
                            "user": get_file_owner(uid)
                        }
                    )

        except (PermissionError, FileNotFoundError, OSError):
            continue

    root_processes = sum(
        1 for process in processes
        if process["user"] == "root"
    )

    print(f"    Processes detected: {len(processes)}")
    print(f"    Root-owned processes: {root_processes}")

    return len(processes)


def check_network():
    print("\n[+] Network Listening Port Audit")

    socket_files = {
        "/proc/net/tcp": "TCP",
        "/proc/net/tcp6": "TCP6",
        "/proc/net/udp": "UDP",
        "/proc/net/udp6": "UDP6"
    }

    found = []

    for filepath, protocol in socket_files.items():

        try:
            with open(filepath, "r") as f:
                lines = f.readlines()[1:]
        except (PermissionError, FileNotFoundError, OSError):
            continue

        for line in lines:

            fields = line.split()

            if len(fields) < 4:
                continue

            state = fields[3]

            if protocol.startswith("TCP") and state != "0A":
                continue

            if protocol.startswith("UDP") and state != "07":
                continue

            try:
                local_address = fields[1]
                ip_hex, port_hex = local_address.rsplit(":", 1)
                port = int(port_hex, 16)
            except ValueError:
                continue

            if protocol in ("TCP", "UDP"):

                try:
                    ip = ".".join(
                        str(int(ip_hex[i:i + 2], 16))
                        for i in range(6, -1, -2)
                    )
                except ValueError:
                    ip = "Unknown"

            else:
                ip = "IPv6"

            found.append((protocol, ip, port))

    if not found:
        print("    No listening network ports found.")
    else:
        for protocol, ip, port in found:
            print(f"    [!] {protocol:<5} {ip}:{port}")

    print(f"    Listening sockets: {len(found)}")

    return len(found)


def calculate_security_score(suid_count, writable_files,
                             writable_dirs, process_count, ports):

    score = 100

    if suid_count > 20:
        score -= 15
    elif suid_count > 10:
        score -= 10

    if writable_files > 5:
        score -= 15
    elif writable_files > 0:
        score -= 5

    if writable_dirs > 5:
        score -= 10
    elif writable_dirs > 0:
        score -= 5

    if ports > 10:
        score -= 15
    elif ports > 0:
        score -= 5

    score = max(score, 0)

    if score >= 80:
        rating = "GOOD"
    elif score >= 60:
        rating = "MODERATE"
    elif score >= 40:
        rating = "HIGH RISK"
    else:
        rating = "CRITICAL"

    print("\n===================================")
    print("        SECURITY ASSESSMENT")
    print("===================================")
    print(f"    Security Score: {score}/100")
    print(f"    Risk Rating:    {rating}")
    print("===================================")


def main():

    print("===================================")
    print("       LINUX SECURITY AUDITOR")
    print("===================================")

    check_current_user()
    check_system_info()

    suid_count = check_suid_files()

    writable_files, writable_dirs = check_world_writable()

    process_count = check_processes()

    ports = check_network()

    calculate_security_score(
        suid_count,
        writable_files,
        writable_dirs,
        process_count,
        ports
    )


if __name__ == "__main__":
    main()
