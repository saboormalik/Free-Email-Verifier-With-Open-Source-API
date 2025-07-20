# 📧 Email Validator CLI Tool

This is a simple Python-based command-line tool for validating a list of email addresses using an API. It reads emails from a file, validates them using an external API, and saves the results in both CSV and JSON formats.

## 🚀 Features

- Bulk validation of email addresses from a `.txt` file
- Automatic retries on request failures
- Progress bar using `tqdm` for better visibility
- Outputs results to both CSV and JSON
- Graceful error handling and retry mechanism

## 📂 Project Structure

```

email-validator/
├── data.txt                # Input file containing email addresses (one per line)
├── validated\_emails.csv    # Output file (CSV)
├── validated\_emails.json   # Output file (JSON)
├── email\_validator.py      # Main script
└── README.md               # This file

````

## 📥 Installation

1. Clone the repository:

2. Install dependencies:

   ```bash
   pip install requests tqdm
   ```

## 🛠️ Usage

1. Add your emails (one per line) in `data.txt`.

2. Run the script:

   ```bash
   python email_validator.py
   ```

3. Results will be saved to:

   * `validated_emails.csv`
   * `validated_emails.json`

## 🔧 Configuration

You can modify the following variables in the script to suit your needs:

```python
INPUT_FILE = 'data.txt'                # Change to your input filename
CSV_OUTPUT_FILE = 'validated_emails.csv'
JSON_OUTPUT_FILE = 'validated_emails.json'
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
API_URL = 'https://rapid-email-verifier.fly.dev/api/validate'
```

## ✅ Output Format

Each result contains:

* `email`: the email address
* `valid`: whether it's valid or not (`true` / `false`)
* `error`: any error encountered (if any)

## 📌 Example Output (JSON)

```json
[
    {
        "email": "test@example.com",
        "valid": true
    },
    {
        "email": "invalid@fake",
        "valid": false,
        "error": "Invalid domain"
    }
]
