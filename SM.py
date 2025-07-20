import requests
import time
import json
import csv
import sys
from tqdm import tqdm

# Config
API_URL = 'https://rapid-email-verifier.fly.dev/api/validate'
INPUT_FILE = 'data.txt'
CSV_OUTPUT_FILE = 'validated_emails.csv'
JSON_OUTPUT_FILE = 'validated_emails.json'
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds between retries

def read_emails(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def validate_email(email):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(API_URL, params={'email': email}, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRIES:
                print(f"[Retry {attempt}] Error validating {email}: {e}. Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"[Error] Failed to validate {email} after {MAX_RETRIES} retries.")
                return {'email': email, 'valid': False, 'error': str(e)}

def save_results_csv(results, filename):
    if not results:
        print("No results to write.")
        return
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

def save_results_json(results, filename):
    with open(filename, 'w') as jsonfile:
        json.dump(results, jsonfile, indent=4)

def main():
    emails = read_emails(INPUT_FILE)
    if not emails:
        print(f"No emails found in {INPUT_FILE}")
        sys.exit(1)

    print(f"Validating {len(emails)} emails...\n")

    results = []
    for email in tqdm(emails, desc="Validating", unit="email"):
        result = validate_email(email)
        results.append(result)
    
    save_results_csv(results, CSV_OUTPUT_FILE)
    save_results_json(results, JSON_OUTPUT_FILE)

    print(f"\n✅ Validation complete.\n- CSV: {CSV_OUTPUT_FILE}\n- JSON: {JSON_OUTPUT_FILE}")

if __name__ == '__main__':
    main()
