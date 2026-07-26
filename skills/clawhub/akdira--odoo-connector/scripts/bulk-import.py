#!/usr/bin/env python3
"""
Odoo Bulk Import Script
========================

Imports records in bulk from a CSV file into any Odoo model.
Supports field mapping, dry-run mode, and batch processing.

Usage:
    python3 bulk-import.py --model res.partner --file contacts.csv
    python3 bulk-import.py --model product.product --file products.csv --dry-run
    python3 bulk-import.py --model sale.order --file orders.csv --batch-size 50

CSV Format:
    The CSV file must have a header row with Odoo field names.
    Example for res.partner:

    name,email,phone,city,customer_rank
    Acme Corp,contact@acme.com,+1-555-0100,Jakarta,1
    Tech Inc,info@tech.io,+62-21-1234,Bandung,1

    Example for product.product:

    name,default_code,list_price,type
    Widget A,WID-001,29.99,product
    Widget B,WID-002,49.99,product

Environment Variables:
    ODOO_URL, ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD

No external dependencies beyond Python standard library.
"""

import xmlrpc.client
import csv
import os
import sys
import argparse
import time

# ─── Configuration from environment ──────────────────────────
URL = os.environ.get("ODOO_URL", "")
DB = os.environ.get("ODOO_DB", "")
USERNAME = os.environ.get("ODOO_USERNAME", "")
PASSWORD = os.environ.get("ODOO_PASSWORD", "")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Bulk import records into Odoo")
    parser.add_argument("--model", required=True, help="Odoo model name (e.g., res.partner)")
    parser.add_argument("--file", required=True, help="Path to CSV file")
    parser.add_argument("--batch-size", type=int, default=100,
                        help="Number of records to create per batch (default: 100)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Validate CSV without creating records")
    parser.add_argument("--delimiter", default=",", help="CSV delimiter (default: comma)")
    return parser.parse_args()


def validate_csv(filepath, model_fields, delimiter=","):
    """Validate CSV headers against model fields."""
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        csv_fields = reader.fieldnames

        if not csv_fields:
            errors.append("CSV file is empty or has no header row")
            return errors, 0

        # Check for unknown fields
        for field in csv_fields:
            if field not in model_fields and field != 'id':
                errors.append(f"Unknown field: '{field}' (not found on model)")

        # Check for required fields
        required = [f for f, meta in model_fields.items() if meta.get('required')]
        missing = [f for f in required if f not in csv_fields and f != 'id']
        if missing:
            errors.append(f"Missing required fields: {', '.join(missing)}")

        # Count rows
        row_count = sum(1 for _ in reader)

    return errors, row_count


def create_records(models, db, uid, password, model, records, batch_size=100):
    """Create records in batches. Returns (created, failed) counts."""
    created = 0
    failed = 0

    for i in range(0, len(records), batch_size):
        batch = records[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (len(records) + batch_size - 1) // batch_size

        for record in batch:
            # Convert numeric strings to appropriate types
            clean_record = {}
            for key, value in record.items():
                if key == 'id':
                    continue
                if value == '':
                    continue
                clean_record[key] = value

            if not clean_record:
                continue

            try:
                models.execute_kw(
                    db, uid, password,
                    model, 'create',
                    [clean_record]
                )
                created += 1
            except xmlrpc.client.Fault as e:
                failed += 1
                print(f"  ERROR row: {e.faultString[:100]}")
            except Exception as e:
                failed += 1
                print(f"  ERROR row: {e}")

        print(f"  Batch {batch_num}/{total_batches} processed ({min(i + batch_size, len(records))}/{len(records)})")

    return created, failed


def main():
    args = parse_args()

    # Validate environment
    if not all([URL, DB, USERNAME, PASSWORD]):
        print("ERROR: Set ODOO_URL, ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD environment variables")
        sys.exit(1)

    if not os.path.exists(args.file):
        print(f"ERROR: File not found: {args.file}")
        sys.exit(1)

    # Connect
    print(f"Connecting to {URL}...")
    common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
    models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")

    uid = common.authenticate(DB, USERNAME, PASSWORD, {})
    if not uid:
        print("ERROR: Authentication failed")
        sys.exit(1)
    print(f"Connected as user {uid}\n")

    # Get model fields
    print(f"Model: {args.model}")
    fields = models.execute_kw(
        DB, uid, PASSWORD,
        args.model, 'fields_get',
        [[]],
        {'attributes': ['type', 'required']}
    )
    print(f"Model has {len(fields)} fields")

    # Validate CSV
    print(f"\nValidating {args.file}...")
    errors, row_count = validate_csv(args.file, fields, args.delimiter)

    if errors:
        print("VALIDATION ERRORS:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"  CSV valid — {row_count} records to import")

    # Dry run
    if args.dry_run:
        print("\n[DRY RUN] Validation passed. No records created.")
        sys.exit(0)

    # Import
    print(f"\nImporting with batch size {args.batch_size}...")
    with open(args.file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=args.delimiter)
        records = list(reader)

    start_time = time.time()
    created, failed = create_records(
        models, DB, uid, PASSWORD,
        args.model, records, args.batch_size
    )
    elapsed = time.time() - start_time

    # Summary
    print(f"\n{'=' * 50}")
    print(f"Import complete in {elapsed:.1f}s")
    print(f"  Created: {created}")
    print(f"  Failed:  {failed}")
    print(f"  Total:   {len(records)}")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
