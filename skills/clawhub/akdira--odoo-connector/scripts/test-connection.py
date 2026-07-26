#!/usr/bin/env python3
"""
Odoo Connection Test Script
============================

Tests the XML-RPC connection to an Odoo instance and verifies
authentication, database access, and basic operations.

Usage:
    # Option 1: Environment variables (recommended)
    export ODOO_URL="https://your-odoo.com"
    export ODOO_DB="your_database"
    export ODOO_USERNAME="your_user"
    export ODOO_PASSWORD="****"
    python3 test-connection.py

    # Option 2: Edit the configuration below directly
    # (not recommended for production)

No external dependencies required — uses only Python standard library.
"""

import xmlrpc.client
import os
import sys

# ─── Configuration ───────────────────────────────────────────
URL = os.environ.get("ODOO_URL", "https://your-odoo-instance.com")
DB = os.environ.get("ODOO_DB", "your_database")
USERNAME = os.environ.get("ODOO_USERNAME", "your_api_user")
PASSWORD = os.environ.get("ODOO_PASSWORD", "your_api_key")

# ─── Test Functions ──────────────────────────────────────────

def test_server_reachable(common):
    """Test 1: Server is reachable and returns version info."""
    try:
        version = common.version()
        server_version = version.get('server_version', 'unknown')
        server_serie = version.get('server_serie', 'unknown')
        print(f"  [PASS] Server reachable — Odoo {server_version} (series {server_serie})")
        return True
    except Exception as e:
        print(f"  [FAIL] Server not reachable: {e}")
        return False

def test_authentication(common):
    """Test 2: Credentials are valid and authentication succeeds."""
    try:
        uid = common.authenticate(DB, USERNAME, PASSWORD, {})
        if uid:
            print(f"  [PASS] Authentication successful — UID: {uid}")
            return uid
        else:
            print(f"  [FAIL] Authentication returned no UID")
            return False
    except Exception as e:
        print(f"  [FAIL] Authentication failed: {e}")
        return False

def test_basic_read(models, db, uid, password):
    """Test 3: Basic read operation works (read company info)."""
    try:
        company = models.execute_kw(
            db, uid, password,
            'res.company', 'search_read',
            [[]],
            {'fields': ['name'], 'limit': 1}
        )
        if company:
            print(f"  [PASS] Read operation works — Company: {company[0]['name']}")
            return True
        else:
            print(f"  [WARN] Read returned no results (database may be empty)")
            return True
    except Exception as e:
        print(f"  [FAIL] Read operation failed: {e}")
        return False

def test_search_count(models, db, uid, password):
    """Test 4: Search count operation works."""
    try:
        count = models.execute_kw(
            db, uid, password,
            'res.partner', 'search_count',
            [[]]
        )
        print(f"  [PASS] Search count works — {count} partners in database")
        return True
    except Exception as e:
        print(f"  [FAIL] Search count failed: {e}")
        return False

# ─── Main ────────────────────────────────────────────────────

def main():
    print("Odoo Connection Test")
    print("=" * 50)
    print(f"Target: {URL}")
    print(f"Database: {DB}")
    print(f"User: {USERNAME}")
    print("=" * 50)

    # Create XML-RPC proxies
    try:
        common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
        models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
    except Exception as e:
        print(f"FATAL: Could not create XML-RPC proxies: {e}")
        sys.exit(1)

    results = []

    # Test 1: Server reachable
    print("\n[1/4] Testing server connectivity...")
    results.append(test_server_reachable(common))

    # Test 2: Authentication
    print("\n[2/4] Testing authentication...")
    uid = test_authentication(common)
    results.append(bool(uid))

    if not uid:
        print("\n" + "=" * 50)
        print("RESULT: FAILED — Cannot proceed without authentication")
        print("Check your URL, database name, username, and password.")
        sys.exit(1)

    # Test 3: Basic read
    print("\n[3/4] Testing read operation...")
    results.append(test_basic_read(models, DB, uid, PASSWORD))

    # Test 4: Search count
    print("\n[4/4] Testing search/count operation...")
    results.append(test_search_count(models, DB, uid, PASSWORD))

    # Summary
    passed = sum(1 for r in results if r)
    total = len(results)

    print("\n" + "=" * 50)
    if all(results):
        print(f"RESULT: ALL TESTS PASSED ({passed}/{total})")
        print("Your Odoo connection is working correctly.")
    else:
        print(f"RESULT: SOME TESTS FAILED ({passed}/{total} passed)")
        print("Review the failures above and check your configuration.")
        sys.exit(1)

if __name__ == "__main__":
    main()
