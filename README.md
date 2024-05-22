# SpiceXtract

SpiceXtract is a command-line utility that facilitates the easy download of SPICE files for virtual machines hosted on
Proxmox. This tool is especially useful for developers and IT professionals who manage VMs and need to quickly access
SPICE connection files.

## Features

- Simple CLI for downloading SPICE files.
- Support for multiple Proxmox nodes and VMs.
- Secure password handling and optional SSL verification.

## Requirements

- Python 3.6 or later.
- `requests` and `urllib3` libraries.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/lHumaNl/SpiceXtract.git
cd SpiceXtract
pip install -r requirements.txt
```

Alternatively, you can install the package using pip:

```bash
pip install spicextract
```

## Usage

To use SpiceXtract, run the following command with the required parameters:

```bash
spicextract -s <server-url> -u <username> -p <password> -n <node> -i <vm_id> -o <output_file_name> [-v]
```

#### Arguments Table

| Argument              | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| `-s`, `--server`      | Proxmox host URL.                                                     |
| `-u`, `--username`    | Proxmox username (must include authentication realm, e.g., user@pam). |
| `-p`, `--password`    | Proxmox password.                                                     |
| `-n`, `--node`        | Proxmox node.                                                         |
| `-i`, `--vm_id`       | VM ID.                                                                |
| `-o`, `--output_file` | Output SPICE file name (.vv extension is appended if not present).    |
| `-v`, `--ssl_verify`  | Optional. Verifies the SSL connection if flagged.                     |
