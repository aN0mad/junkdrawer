# NXC `spider_plus` parser

This utility converts the structured JSON file containing file metadata (grouped by share)
into **multiple CSV files**, one per top-level share (for example `NETLOGON`, `SYSVOL`).

It supports **human-readable terminal output**, optional ANSI coloring, and a **quiet mode**
suitable for automation or CI pipelines.

The script uses **only the Python standard library**.

---

## Features

- 📁 One CSV file per top-level share
- 🧾 Fixed CSV schema for easy ingestion and analysis
- 🎨 Optional colored, readable stdout output
- 🔇 Quiet mode for scripting and cron jobs
- 🚫 Optional color suppression (`--no-color`)
- 🧰 No third-party dependencies

---

## Input JSON Structure

The script expects JSON shaped like this:

```json
{
  "SHARE_NAME": {
    "path/to/file.ext": {
      "atime_epoch": "YYYY-MM-DD HH:MM:SS",
      "ctime_epoch": "YYYY-MM-DD HH:MM:SS",
      "mtime_epoch": "YYYY-MM-DD HH:MM:SS",
      "size": "1.23 MB"
    }
  }
}
```

### Mapping Logic

- **Top-level keys** → CSV filenames (`<SHARE>.csv`)
- **Second-level keys** → `file` column
- **Metadata values** → copied verbatim into CSV columns

---

## CSV Output Schema

Each generated CSV uses the following headers:

| Column        | Description                  |
|--------------|------------------------------|
| `file`       | File path (JSON object key)  |
| `atime_epoch`| Access time                  |
| `ctime_epoch`| Creation time                |
| `mtime_epoch`| Modification time            |
| `size`       | File size (as provided)      |

---

## Usage

### Basic usage

```bash
python3 json_to_csv.py input.json
```

Creates:

```
csv_out/NETLOGON.csv
csv_out/SYSVOL.csv
```

### Custom output directory

```bash
python3 json_to_csv.py input.json ./out
```

### Quiet mode

Suppresses share and file listings, but **still prints CSV output paths**:

```bash
python3 json_to_csv.py input.json --quiet
```

### Disable ANSI colors

```bash
python3 json_to_csv.py input.json --no-color
```

### Quiet + no color (CI / cron friendly)

```bash
python3 json_to_csv.py input.json --quiet --no-color
```

---

## Terminal Output (default)

When not using `--quiet`, the script prints a readable summary:

```
SYSVOL
────────────────────────────────────────
  empire.local/Policies/.../msedge.adml
    size: 1.44 MB
  empire.local/Policies/.../chrome.adml
    size: 1.21 MB

  → CSV written: csv_out/SYSVOL.csv
```

The `→ CSV written:` line is **always printed**, even in quiet mode.

---

## Requirements

- Python **3.8+**
- ANSI-capable terminal for colored output (optional)

---

## Notes

- Invalid or malformed JSON fails fast with a clear error message.
- Timestamp and size fields are not transformed.
- Errors are written to **stderr**; normal output goes to **stdout**.

---