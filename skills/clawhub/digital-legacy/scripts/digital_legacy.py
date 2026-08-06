#!/usr/bin/env python3
"""
Digital Legacy — Digital Inheritance Planner
=============================================

Create a digital inheritance plan: inventory accounts, subscriptions, crypto
wallets, and important files; generate an encrypted digital will; and produce
a printable emergency access guide for trusted family.

Usage:
    python3 digital_legacy.py setup              # interactive full setup
    python3 digital_legacy.py init               # initialize plan
    python3 digital_legacy.py add-account        # add an account
    python3 digital_legacy.py add-subscription   # add a subscription
    python3 digital_legacy.py add-wallet         # add a crypto wallet
    python3 digital_legacy.py list               # list inventory
    python3 digital_legacy.py generate-will      # encrypt the will
    python3 digital_legacy.py emergency-guide    # generate HTML guide
    python3 digital_legacy.py read-will <file>   # decrypt and read will

No third-party dependencies. Python 3.8+ stdlib only.

Encryption: AES-256-GCM (via hashlib + stdlib XOR-stream fallback).
Key derivation: PBKDF2-HMAC-SHA256, 100,000 iterations.
"""

from __future__ import annotations

import getpass
import hashlib
import json
import os
import secrets
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PBKDF2_ITERATIONS = 100_000
KEY_LENGTH = 32  # 256-bit key
SALT_LENGTH = 16
NONCE_LENGTH = 12
TAG_LENGTH = 16
VERSION = "1.0.0"

DEFAULT_INVENTORY_PATH = Path("accounts.json")
DEFAULT_WILL_PATH = Path("digital_will.enc")
DEFAULT_GUIDE_PATH = Path("emergency_guide.html")

TEMPLATE_DIR = Path(__file__).parent / "templates"
WILL_TEMPLATE = TEMPLATE_DIR / "template_will.md"
GUIDE_TEMPLATE = TEMPLATE_DIR / "template_guide.html"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Account:
    service: str = ""
    account_type: str = ""       # email, social, banking, cloud, etc.
    username: str = ""           # email or username (NOT password)
    access_method: str = ""      # password manager, 2FA app, etc.
    action: str = "archive"      # archive, memorialize, delete, transfer, maintain
    notes: str = ""


@dataclass
class Subscription:
    service: str = ""
    cost: float = 0.0
    cycle: str = "monthly"       # monthly, yearly
    action: str = "cancel"       # cancel, transfer, maintain
    notes: str = ""


@dataclass
class Wallet:
    wallet_type: str = ""        # hardware, software, exchange
    name: str = ""               # Ledger, MetaMask, Coinbase
    access_method: str = ""      # seed phrase location (NOT the phrase itself)
    approximate_value: str = ""  # e.g. "~$5000"
    notes: str = ""


@dataclass
class LegacyPlan:
    """Complete digital legacy inventory."""
    owner_name: str = ""
    trusted_person: str = ""
    accounts: List[Account] = field(default_factory=list)
    subscriptions: List[Subscription] = field(default_factory=list)
    wallets: List[Wallet] = field(default_factory=list)
    important_files: List[str] = field(default_factory=list)
    legacy_contacts: List[str] = field(default_factory=list)
    notes: str = ""
    created: str = ""
    updated: str = ""

    def to_dict(self) -> dict:
        return {
            "owner_name": self.owner_name,
            "trusted_person": self.trusted_person,
            "accounts": [asdict(a) for a in self.accounts],
            "subscriptions": [asdict(s) for s in self.subscriptions],
            "wallets": [asdict(w) for w in self.wallets],
            "important_files": self.important_files,
            "legacy_contacts": self.legacy_contacts,
            "notes": self.notes,
            "created": self.created,
            "updated": self.updated,
        }

    @classmethod
    def from_dict(cls, d: dict) -> 'LegacyPlan':
        plan = cls()
        plan.owner_name = d.get("owner_name", "")
        plan.trusted_person = d.get("trusted_person", "")
        plan.accounts = [Account(**a) for a in d.get("accounts", [])]
        plan.subscriptions = [Subscription(**s) for s in d.get("subscriptions", [])]
        plan.wallets = [Wallet(**w) for w in d.get("wallets", [])]
        plan.important_files = d.get("important_files", [])
        plan.legacy_contacts = d.get("legacy_contacts", [])
        plan.notes = d.get("notes", "")
        plan.created = d.get("created", "")
        plan.updated = d.get("updated", "")
        return plan


# ---------------------------------------------------------------------------
# Encryption (stdlib only)
# ---------------------------------------------------------------------------

def derive_key(passphrase: str, salt: bytes) -> bytes:
    """Derive a 256-bit key from passphrase + salt using PBKDF2."""
    return hashlib.pbkdf2_hmac(
        'sha256',
        passphrase.encode('utf-8'),
        salt,
        PBKDF2_ITERATIONS,
        dklen=KEY_LENGTH,
    )


def encrypt(data: str, passphrase: str) -> bytes:
    """Encrypt a string with AES-256-GCM or stdlib fallback.

    Uses the `cryptography` library if available (proper AES-GCM).
    Falls back to a stdlib XOR-stream cipher with HMAC authentication if not.
    The fallback is less secure but functional for personal use.
    """
    plaintext = data.encode('utf-8')
    salt = secrets.token_bytes(SALT_LENGTH)
    nonce = secrets.token_bytes(NONCE_LENGTH)
    key = derive_key(passphrase, salt)

    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, plaintext, None)
        return salt + nonce + ciphertext
    except ImportError:
        # Fallback: XOR-stream with HMAC-SHA256 authentication
        return _encrypt_fallback(plaintext, key, salt, nonce)


def _encrypt_fallback(plaintext: bytes, key: bytes, salt: bytes, nonce: bytes) -> bytes:
    """Stdlib-only encryption: XOR keystream + HMAC tag."""
    import hmac

    # Generate keystream from key + nonce (PBKDF2 as PRNG)
    keystream = b''
    counter = 0
    while len(keystream) < len(plaintext):
        block = hashlib.sha256(key + nonce + counter.to_bytes(4, 'big')).digest()
        keystream += block
        counter += 1

    # XOR encrypt
    ciphertext = bytes(a ^ b for a, b in zip(plaintext, keystream))

    # HMAC authentication tag
    tag = hmac.new(key, salt + nonce + ciphertext, hashlib.sha256).digest()[:TAG_LENGTH]

    return salt + nonce + ciphertext + tag


def decrypt(encrypted_data: bytes, passphrase: str) -> str:
    """Decrypt data encrypted by encrypt()."""
    if len(encrypted_data) < SALT_LENGTH + NONCE_LENGTH:
        raise ValueError("Encrypted data too short — file may be corrupted.")

    salt = encrypted_data[:SALT_LENGTH]
    nonce = encrypted_data[SALT_LENGTH:SALT_LENGTH + NONCE_LENGTH]
    key = derive_key(passphrase, salt)

    # Try AES-GCM first
    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        aesgcm = AESGCM(key)
        ciphertext = encrypted_data[SALT_LENGTH + NONCE_LENGTH:]
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        return plaintext.decode('utf-8')
    except ImportError:
        pass
    except Exception:
        pass  # Fall through to fallback decryption

    # Fallback decryption
    return _decrypt_fallback(encrypted_data, key, salt, nonce)


def _decrypt_fallback(encrypted_data: bytes, key: bytes, salt: bytes, nonce: bytes) -> str:
    """Stdlib-only decryption for fallback-encrypted data."""
    import hmac

    remaining = encrypted_data[SALT_LENGTH + NONCE_LENGTH:]
    if len(remaining) < TAG_LENGTH:
        raise ValueError("Encrypted data too short — file may be corrupted.")

    ciphertext = remaining[:-TAG_LENGTH]
    tag = remaining[-TAG_LENGTH:]

    # Verify HMAC
    expected_tag = hmac.new(key, salt + nonce + ciphertext, hashlib.sha256).digest()[:TAG_LENGTH]
    if not hmac.compare_digest(tag, expected_tag):
        raise ValueError("Authentication failed — wrong passphrase or corrupted file.")

    # Regenerate keystream
    keystream = b''
    counter = 0
    while len(keystream) < len(ciphertext):
        block = hashlib.sha256(key + nonce + counter.to_bytes(4, 'big')).digest()
        keystream += block
        counter += 1

    # XOR decrypt
    plaintext = bytes(a ^ b for a, b in zip(ciphertext, keystream))
    return plaintext.decode('utf-8')


# ---------------------------------------------------------------------------
# Inventory file operations
# ---------------------------------------------------------------------------

def load_inventory(path: Path = DEFAULT_INVENTORY_PATH) -> Optional[LegacyPlan]:
    """Load inventory from JSON file."""
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding='utf-8'))
    return LegacyPlan.from_dict(data)


def save_inventory(plan: LegacyPlan, path: Path = DEFAULT_INVENTORY_PATH) -> None:
    """Save inventory to JSON file."""
    plan.updated = datetime.now().strftime("%Y-%m-%d")
    path.write_text(
        json.dumps(plan.to_dict(), indent=2, ensure_ascii=False),
        encoding='utf-8',
    )


# ---------------------------------------------------------------------------
# Interactive prompts
# ---------------------------------------------------------------------------

def ask(prompt: str, default: str = "") -> str:
    """Prompt with optional default."""
    if default:
        val = input(f"{prompt} [{default}]: ").strip()
        return val if val else default
    return input(f"{prompt}: ").strip()


def ask_passphrase(confirm: bool = True) -> str:
    """Securely prompt for a passphrase."""
    while True:
        pw = getpass.getpass("Enter passphrase: ")
        if len(pw) < 8:
            print("Warning: passphrase is short (< 8 chars). Consider a stronger one.")
            cont = input("Continue anyway? (y/n) [n]: ").strip().lower()
            if cont != 'y':
                continue
        if confirm:
            pw2 = getpass.getpass("Confirm passphrase: ")
            if pw != pw2:
                print("Passphrases don't match. Try again.")
                continue
        return pw


# ---------------------------------------------------------------------------
# Will generation
# ---------------------------------------------------------------------------

def build_will_text(plan: LegacyPlan) -> str:
    """Build the plaintext will document from the inventory."""
    template = WILL_TEMPLATE.read_text(encoding='utf-8') if WILL_TEMPLATE.exists() else "{owner_name}"
    now = datetime.now().strftime("%Y-%m-%d")

    # Build sections
    accounts_lines = []
    for i, a in enumerate(plan.accounts, 1):
        accounts_lines.append(
            f"### {i}. {a.service}\n"
            f"- **Type:** {a.account_type}\n"
            f"- **Username/Email:** {a.username or 'N/A'}\n"
            f"- **Access:** {a.access_method}\n"
            f"- **Action:** {a.action}\n"
            f"- **Notes:** {a.notes}\n"
        )

    subs_lines = []
    for i, s in enumerate(plan.subscriptions, 1):
        subs_lines.append(
            f"### {i}. {s.service}\n"
            f"- **Cost:** ${s.cost:.2f} / {s.cycle}\n"
            f"- **Action:** {s.action}\n"
            f"- **Notes:** {s.notes}\n"
        )

    wallet_lines = []
    for i, w in enumerate(plan.wallets, 1):
        wallet_lines.append(
            f"### {i}. {w.name} ({w.wallet_type})\n"
            f"- **Access:** {w.access_method}\n"
            f"- **Approximate Value:** {w.approximate_value}\n"
            f"- **Notes:** {w.notes}\n"
        )

    files_lines = [f"- {f}" for f in plan.important_files] or ["- (none documented)"]
    legacy_lines = [f"- {l}" for l in plan.legacy_contacts] or ["- (none documented)"]

    return template.format(
        owner_name=plan.owner_name or "[Your Name]",
        trusted_person=plan.trusted_person or "[Trusted Person]",
        date=now,
        lawyer_contact="[Add lawyer contact]",
        advisor_contact="[Add advisor contact]",
        accounts_section="\n".join(accounts_lines) or "(none documented)",
        subscriptions_section="\n".join(subs_lines) or "(none documented)",
        wallets_section="\n".join(wallet_lines) or "(none documented)",
        files_section="\n".join(files_lines),
        legacy_section="\n".join(legacy_lines),
        notes_section=plan.notes or "(none)",
    )


def generate_will(plan: LegacyPlan, output: Path = DEFAULT_WILL_PATH) -> None:
    """Generate the encrypted will document."""
    will_text = build_will_text(plan)
    print(f"\nWill document ({len(will_text)} chars) ready for encryption.")
    passphrase = ask_passphrase()
    encrypted = encrypt(will_text, passphrase)
    output.write_bytes(encrypted)
    print(f"\n✓ Encrypted will saved to: {output}")
    print(f"  Size: {len(encrypted)} bytes")
    print(f"  Encryption: AES-256-GCM (or stdlib fallback)")
    print(f"\n⚠ TEST DECRYPTION NOW:")
    print(f"  python3 digital_legacy.py read-will {output}")


def read_will(path: Path) -> None:
    """Decrypt and display the will."""
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(2)

    encrypted = path.read_bytes()
    passphrase = getpass.getpass("Enter passphrase: ")

    try:
        text = decrypt(encrypted, passphrase)
        print("\n" + "=" * 60)
        print(text)
        print("=" * 60)
    except ValueError as e:
        print(f"\n✗ Decryption failed: {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Emergency guide generation
# ---------------------------------------------------------------------------

def generate_emergency_guide(plan: LegacyPlan, output: Path = DEFAULT_GUIDE_PATH) -> None:
    """Generate the printable HTML emergency guide."""
    if not GUIDE_TEMPLATE.exists():
        print(f"Error: guide template not found at {GUIDE_TEMPLATE}", file=sys.stderr)
        sys.exit(2)

    template = GUIDE_TEMPLATE.read_text(encoding='utf-8')
    now = datetime.now().strftime("%Y-%m-%d")

    # Use safe string replacement (HTML template has CSS braces that break .format())
    replacements = {
        "{owner_name}": plan.owner_name or "[Your Name]",
        "{trusted_person}": plan.trusted_person or "[Trusted Person]",
        "{date}": now,
        "{will_location}": "~/Documents/DigitalLegacy/digital_will.enc (see notes)",
        "{script_source}": "https://github.com/voronindenis5/digital-legacy",
        "{passphrase_hint}": "[Add a hint that only your trusted person would understand]",
        "{lawyer_contact}": "[Add name and phone]",
        "{advisor_contact}": "[Add name and phone]",
        "{tech_contact}": "[Add name and phone]",
        "{medical_contact}": "[Add doctor name and phone]",
        "{version}": VERSION,
    }

    html = template
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    output.write_text(html, encoding='utf-8')
    print(f"\n✓ Emergency guide saved to: {output}")
    print(f"\n⚠ EDIT the guide to add:")
    print(f"  - Passphrase hint (NOT the passphrase itself)")
    print(f"  - Actual file location")
    print(f"  - Contact information")
    print(f"\nThen PRINT and give to your trusted person.")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_init() -> None:
    """Initialize a new legacy plan."""
    if DEFAULT_INVENTORY_PATH.exists():
        overwrite = input(f"{DEFAULT_INVENTORY_PATH} exists. Overwrite? (y/n) [n]: ")
        if overwrite.strip().lower() != 'y':
            print("Aborted.")
            return

    plan = LegacyPlan()
    plan.owner_name = ask("Your name")
    plan.trusted_person = ask("Trusted person's name")
    plan.created = datetime.now().strftime("%Y-%m-%d")
    save_inventory(plan)
    print(f"\n✓ Initialized legacy plan at {DEFAULT_INVENTORY_PATH}")
    print(f"  Owner: {plan.owner_name}")
    print(f"  Trusted person: {plan.trusted_person}")
    print(f"\nNext steps: add-account, add-subscription, add-wallet")


def cmd_add_account() -> None:
    """Add an account to the inventory."""
    plan = load_inventory()
    if not plan:
        print("No plan found. Run 'init' first.")
        return

    account = Account()
    account.service = ask("Service name (e.g. Gmail, Chase Bank)")
    account.account_type = ask("Type (email/social/banking/cloud/etc.)")
    account.username = ask("Username or email (NOT password)")
    account.access_method = ask("Access method (password manager, 2FA, etc.)")
    account.action = ask("Action (archive/memorialize/delete/transfer/maintain)", "archive")
    account.notes = ask("Notes (optional)")

    plan.accounts.append(account)
    save_inventory(plan)
    print(f"\n✓ Added account: {account.service}")


def cmd_add_subscription() -> None:
    """Add a subscription to the inventory."""
    plan = load_inventory()
    if not plan:
        print("No plan found. Run 'init' first.")
        return

    sub = Subscription()
    sub.service = ask("Service name (e.g. Netflix)")
    cost_str = ask("Cost ($)")
    try:
        sub.cost = float(cost_str)
    except ValueError:
        sub.cost = 0.0
    sub.cycle = ask("Billing cycle (monthly/yearly)", "monthly")
    sub.action = ask("Action (cancel/transfer/maintain)", "cancel")
    sub.notes = ask("Notes (optional)")

    plan.subscriptions.append(sub)
    save_inventory(plan)
    print(f"\n✓ Added subscription: {sub.service}")


def cmd_add_wallet() -> None:
    """Add a crypto wallet to the inventory."""
    plan = load_inventory()
    if not plan:
        print("No plan found. Run 'init' first.")
        return

    wallet = Wallet()
    wallet.wallet_type = ask("Type (hardware/software/exchange)")
    wallet.name = ask("Name (e.g. Ledger, MetaMask, Coinbase)")
    wallet.access_method = ask(
        "Access method (seed phrase LOCATION — do NOT enter the phrase itself)"
    )
    wallet.approximate_value = ask("Approximate value (e.g. ~$5000)")
    wallet.notes = ask("Notes (optional)")

    plan.wallets.append(wallet)
    save_inventory(plan)
    print(f"\n✓ Added wallet: {wallet.name}")


def cmd_list() -> None:
    """List the full inventory."""
    plan = load_inventory()
    if not plan:
        print("No plan found. Run 'init' first.")
        return

    print(f"\n{'='*60}")
    print(f"Digital Legacy Inventory")
    print(f"{'='*60}")
    print(f"Owner: {plan.owner_name}")
    print(f"Trusted person: {plan.trusted_person}")
    print(f"Created: {plan.created} | Updated: {plan.updated}")

    print(f"\n📋 Accounts ({len(plan.accounts)}):")
    for i, a in enumerate(plan.accounts, 1):
        print(f"  {i}. {a.service} ({a.account_type}) → {a.action}")

    print(f"\n💳 Subscriptions ({len(plan.subscriptions)}):")
    total_monthly = sum(
        s.cost if s.cycle == 'monthly' else s.cost / 12
        for s in plan.subscriptions
    )
    for i, s in enumerate(plan.subscriptions, 1):
        print(f"  {i}. {s.service} — ${s.cost:.2f}/{s.cycle} → {s.action}")
    if plan.subscriptions:
        print(f"  Total: ~${total_monthly:.2f}/month")

    print(f"\n💰 Crypto Wallets ({len(plan.wallets)}):")
    for i, w in enumerate(plan.wallets, 1):
        print(f"  {i}. {w.name} ({w.wallet_type}) — {w.approximate_value}")

    print(f"\n📁 Important Files ({len(plan.important_files)}):")
    for f in plan.important_files:
        print(f"  - {f}")

    print(f"\n👤 Legacy Contacts ({len(plan.legacy_contacts)}):")
    for l in plan.legacy_contacts:
        print(f"  - {l}")

    print(f"\n{'='*60}")


def cmd_generate_will() -> None:
    """Generate the encrypted will."""
    plan = load_inventory()
    if not plan:
        print("No plan found. Run 'init' first.")
        return
    if not plan.accounts and not plan.wallets and not plan.subscriptions:
        print("Inventory is empty. Add accounts/subscriptions/wallets first.")
        return
    generate_will(plan)


def cmd_emergency_guide() -> None:
    """Generate the emergency guide."""
    plan = load_inventory()
    if not plan:
        print("No plan found. Run 'init' first.")
        return
    generate_emergency_guide(plan)


def cmd_setup() -> None:
    """Interactive full setup."""
    print("=" * 60)
    print("Digital Legacy — Full Setup")
    print("=" * 60)
    print("This will guide you through creating a complete digital legacy plan.\n")

    cmd_init()

    plan = load_inventory()
    if not plan:
        return

    # Add accounts
    print("\n" + "=" * 40)
    print("Step 1: Email Accounts (highest priority)")
    print("=" * 40)
    while True:
        cmd_add_account()
        plan = load_inventory()
        if input("\nAdd another email/account? (y/n) [n]: ").strip().lower() != 'y':
            break

    # Add subscriptions
    print("\n" + "=" * 40)
    print("Step 2: Subscriptions")
    print("=" * 40)
    while True:
        cmd_add_subscription()
        plan = load_inventory()
        if input("\nAdd another subscription? (y/n) [n]: ").strip().lower() != 'y':
            break

    # Add wallets
    print("\n" + "=" * 40)
    print("Step 3: Crypto Wallets")
    print("=" * 40)
    while True:
        cmd_add_wallet()
        plan = load_inventory()
        if input("\nAdd another wallet? (y/n) [n]: ").strip().lower() != 'y':
            break

    # Important files
    print("\n" + "=" * 40)
    print("Step 4: Important Files")
    print("=" * 40)
    while True:
        f = ask("Important file or location (e.g. 'Tax returns in ~/Documents')")
        if f:
            plan.important_files.append(f)
            save_inventory(plan)
        if input("Add another? (y/n) [n]: ").strip().lower() != 'y':
            break

    # Legacy contacts
    print("\n" + "=" * 40)
    print("Step 5: Social Media Legacy Contacts")
    print("=" * 40)
    while True:
        l = ask("Legacy contact setting (e.g. 'Google Inactive Account Manager — set to 6 months')")
        if l:
            plan.legacy_contacts.append(l)
            save_inventory(plan)
        if input("Add another? (y/n) [n]: ").strip().lower() != 'y':
            break

    # Show inventory
    cmd_list()

    # Generate will
    print("\n" + "=" * 40)
    print("Step 6: Generate Encrypted Will")
    print("=" * 40)
    generate_input = input("Generate encrypted will now? (y/n) [y]: ").strip().lower()
    if generate_input != 'n':
        cmd_generate_will()

    # Generate guide
    print("\n" + "=" * 40)
    print("Step 7: Generate Emergency Guide")
    print("=" * 40)
    guide_input = input("Generate emergency guide now? (y/n) [y]: ").strip().lower()
    if guide_input != 'n':
        cmd_emergency_guide()

    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print(f"Inventory: {DEFAULT_INVENTORY_PATH}")
    print(f"Will:      {DEFAULT_WILL_PATH}")
    print(f"Guide:     {DEFAULT_GUIDE_PATH}")
    print("\nNext steps:")
    print("  1. TEST decrypting the will (python3 digital_legacy.py read-will digital_will.enc)")
    print("  2. EDIT the emergency guide with real details")
    print("  3. PRINT the guide and give it to your trusted person")
    print("  4. Store the passphrase securely (NOT with the encrypted file)")
    print("  5. Review annually")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv or argv[0] in ('-h', '--help', 'help'):
        print(__doc__)
        return 0

    cmd = argv[0]

    if cmd == 'init':
        cmd_init()
    elif cmd == 'setup':
        cmd_setup()
    elif cmd == 'add-account':
        cmd_add_account()
    elif cmd == 'add-subscription':
        cmd_add_subscription()
    elif cmd == 'add-wallet':
        cmd_add_wallet()
    elif cmd in ('list', 'ls'):
        cmd_list()
    elif cmd == 'generate-will':
        cmd_generate_will()
    elif cmd in ('emergency-guide', 'guide'):
        cmd_emergency_guide()
    elif cmd == 'read-will':
        if len(argv) < 2:
            print("Usage: read-will <file.enc>", file=sys.stderr)
            return 2
        read_will(Path(argv[1]))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print(f"Run 'python3 digital_legacy.py --help' for usage.", file=sys.stderr)
        return 2

    return 0


if __name__ == '__main__':
    sys.exit(main())
