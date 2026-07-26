#!/usr/bin/env python3
"""
Space Duck — Ed25519 signing-key setup / status / rotation for envelope v3.

INTENT: Generate a per-duck Ed25519 keypair on the owner's box, register the
        PUBLIC key with the Space Duck backend, and enable v3-signed pecks.
        The private key never leaves this machine (LANE-IS-IMMUTABLE
        doctrine — see docs/spec/BEAK-V3-ASYMMETRIC-IDENTITY.md §3.1).

CALLS:  POST <api>/beak/duck/sign-key/bootstrap  (X-Beak-Key auth)
        Space Duck's own backend only. No third-party hosts.

AUTH:   X-Beak-Key header from ~/.space-duck/config.json (chmod 600).
        The bootstrap endpoint is the ALREADY-PAIRED lane — it takes a
        first sign-key on a duck that has a beak_key but no live Cognito
        JWT (the Lane A common case). Rotation still requires owner-auth
        + old-key attestation, which is a Mission Control job.

Files:
  ~/.space-duck/sign_key.hex  — 64 lowercase hex chars = 32 raw Ed25519
                                private-key bytes. Written 0600. NEVER
                                transmitted.
  ~/.space-duck/config.json   — updated with `sign_key_id` and
                                `envelope_v3: true` on successful setup.

Usage:
  python3 sign_key.py setup     # generate, register, wire config
  python3 sign_key.py status    # show local + registered state
  python3 sign_key.py rotate    # (currently print-only guidance; see docstring)
"""
import argparse, json, os, stat, sys, urllib.error, urllib.request
from pathlib import Path

CONFIG_DIR  = Path.home() / '.space-duck'
CONFIG_PATH = CONFIG_DIR / 'config.json'
SIGN_KEY_PATH = CONFIG_DIR / 'sign_key.hex'
DEFAULT_API = 'https://beak.spaceduckling.com'


def _load_config():
    if not CONFIG_PATH.exists():
        print('ERROR: No Space Duck config found. Run scripts/pair.py or scripts/setup.py first.')
        sys.exit(1)
    return json.loads(CONFIG_PATH.read_text())


def _save_config(cfg):
    CONFIG_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))
    try:
        CONFIG_PATH.chmod(0o600)
    except OSError:
        pass


def _api_base(cfg):
    # Match send_peck.py's resolver: config wins, default to prod.
    return cfg.get('api_base', DEFAULT_API)


def _ensure_cryptography():
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey  # noqa: F401
    except ImportError:
        print('ERROR: v3 signing needs the `cryptography` package.')
        print('  Install with: pip install cryptography')
        sys.exit(1)


def _generate_keypair():
    _ensure_cryptography()
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives import serialization
    priv = Ed25519PrivateKey.generate()
    raw_priv = priv.private_bytes(
        serialization.Encoding.Raw,
        serialization.PrivateFormat.Raw,
        serialization.NoEncryption(),
    )
    raw_pub = priv.public_key().public_bytes(
        serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    return raw_priv.hex(), raw_pub.hex()


def _write_sign_key(privkey_hex):
    CONFIG_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
    # Write via a private temp then rename so we never leave a world-readable
    # window on the private key.
    tmp = SIGN_KEY_PATH.with_suffix('.hex.tmp')
    with open(tmp, 'w') as f:
        f.write(privkey_hex + '\n')
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass
    os.replace(tmp, SIGN_KEY_PATH)


def _post_bootstrap(api, beak_key, pubkey_hex):
    body = json.dumps({'sign_pubkey': pubkey_hex}).encode()
    req = urllib.request.Request(
        f'{api}/beak/duck/sign-key/bootstrap',
        data=body, method='POST',
        headers={'Content-Type': 'application/json',
                 'X-Beak-Key': beak_key})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except Exception:
            return e.code, {'error': f'http_{e.code}'}
    except Exception as e:
        return 0, {'error': f'transport: {e}'}


# Import the shared envelope helper so status + future signing use the same
# derive_key_id / load_sign_key logic as send_peck.py. Sibling-dir import
# pattern mirrors send_peck.py's `sys.path.insert` recipe.
import pathlib as _pl
_script_dir = str(_pl.Path(__file__).resolve().parent)
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)
from _envelope import derive_key_id, load_sign_key


def cmd_setup(args):
    """Generate a keypair (or reuse the one on disk) and bootstrap-register
    the pubkey with the backend. Idempotent — a re-run with the same on-disk
    key hits the 200 `already:true` branch on the server."""
    cfg = _load_config()
    api = _api_base(cfg)
    beak_key = cfg.get('beak_key', '')
    sdid = cfg.get('spaceduck_id', '')
    if not beak_key or not sdid:
        print('ERROR: config.json missing beak_key or spaceduck_id — repair pairing first.')
        sys.exit(1)

    # Reuse an existing on-disk key if present; regenerate only with --force.
    existing_priv, existing_pub, existing_kid = load_sign_key()
    if existing_priv and not args.force:
        print(f'🔑 Reusing existing sign key at {SIGN_KEY_PATH} (key_id={existing_kid})')
        priv_hex, pub_hex = existing_priv, existing_pub
    else:
        _ensure_cryptography()
        priv_hex, pub_hex = _generate_keypair()
        _write_sign_key(priv_hex)
        print(f'🔑 Generated new Ed25519 keypair — private key at {SIGN_KEY_PATH} (0600)')

    key_id = derive_key_id(pub_hex)
    print(f'   Public key:  {pub_hex[:16]}…  key_id={key_id}')
    print(f'📡 Registering with backend (POST /beak/duck/sign-key/bootstrap)...')
    status, resp = _post_bootstrap(api, beak_key, pub_hex)
    if status == 200:
        server_kid = resp.get('key_id', '')
        if server_kid and server_kid != key_id:
            print(f'⚠️  Server-derived key_id {server_kid} != local {key_id} — refusing to update config.')
            sys.exit(2)
        if resp.get('already'):
            print(f'✅ Already registered on this duck (key_id={server_kid}).')
        else:
            print(f'✅ Registered (key_id={server_kid}).')
        cfg['sign_key_id'] = server_kid or key_id
        cfg['envelope_v3'] = True
        _save_config(cfg)
        print(f'💾 Config updated: envelope_v3=true, sign_key_id={cfg["sign_key_id"]}')
        return 0
    if status == 409:
        current = resp.get('current_key_id', '')
        print('⚠️  A DIFFERENT sign_pubkey is already registered on this duck.')
        print(f'   current server key_id: {current}')
        print(f'   local key_id:          {key_id}')
        print()
        print('   Bootstrap is first-writer-wins (TOFU). To replace an existing key,')
        print('   an owner must sign in to Mission Control and rotate via:')
        print(f'     POST /beak/duck/{sdid}/sign-key/rotate')
        print('   (requires JWT + an attestation signed by the OLD key).')
        return 3
    if status == 403:
        print(f'❌ Backend refused (403): {resp.get("error", "invalid beak_key")}')
        print('   Check config.json beak_key; re-pair if it was rotated.')
        return 4
    print(f'❌ Bootstrap failed: HTTP {status} — {json.dumps(resp)[:220]}')
    return 1


def cmd_status(args):
    cfg = _load_config()
    priv_hex, pub_hex, key_id = load_sign_key()
    cfg_kid = cfg.get('sign_key_id', '')
    v3 = bool(cfg.get('envelope_v3'))
    print(f'sign_key.hex:   {"present" if priv_hex else "absent"}   ({SIGN_KEY_PATH})')
    if priv_hex:
        try:
            mode = stat.S_IMODE(os.stat(SIGN_KEY_PATH).st_mode)
            print(f'  perms:        {oct(mode)}  (want 0o600)')
        except OSError:
            pass
        print(f'  key_id:       {key_id}')
        print(f'  pubkey:       {pub_hex[:32]}…')
    print(f'config.sign_key_id:  {cfg_kid or "(unset)"}')
    print(f'config.envelope_v3:  {v3}')
    if priv_hex and cfg_kid and key_id != cfg_kid:
        print('⚠️  On-disk key_id does not match config.sign_key_id — '
              'run `sign_key.py setup` to re-sync (or investigate a rotate).')
    if priv_hex and not v3:
        print('ℹ️  A local sign key exists but envelope_v3 is not enabled in config. '
              'Run `sign_key.py setup` to register + enable.')
    return 0


def cmd_rotate(args):
    """Rotation lives at POST /beak/duck/<sdid>/sign-key/rotate. The Phase 1
    handler requires BOTH owner-auth (Cognito JWT via `_require_auth`) AND an
    attestation envelope signed by the OLD key. The skill holds the old key
    but has no JWT — so the box cannot rotate autonomously. Print the exact
    Mission Control lane instead of pretending we can drive it."""
    cfg = _load_config()
    sdid = cfg.get('spaceduck_id', '(unknown)')
    print('Rotation is owner-driven — the Phase 1 rotate endpoint requires a')
    print('Cognito-authenticated caller AND an attestation signed by the OLD key.')
    print()
    print('To rotate:')
    print(f'  1. Open Mission Control for this duck (spaceduck_id={sdid}).')
    print('  2. Trigger "Rotate sign key" — Mission Control will use the browser')
    print(f'     session\'s JWT to POST /beak/duck/{sdid}/sign-key/rotate with the')
    print('     attestation, and hand the new privkey back to your box out-of-band.')
    print()
    print('Break-glass (owner-only, lost old key):')
    print(f'  Same endpoint with `recovery: true` — owner-auth only, no old-key')
    print('  attestation. Loudly audited as security.sign_key_recovered.')
    return 2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Manage the local Ed25519 signing key (envelope v3).')
    sub = parser.add_subparsers(dest='cmd', required=True)

    p_setup = sub.add_parser('setup', help='Generate + register the sign key (idempotent).')
    p_setup.add_argument('--force', action='store_true',
                         help='Force-generate a fresh keypair even if one exists on disk. '
                              'Only useful when the server has NO key yet '
                              '(otherwise the bootstrap returns 409 — use rotate).')

    sub.add_parser('status', help='Show local + registered sign-key state.')
    sub.add_parser('rotate', help='Print rotation guidance (owner-driven path).')

    args = parser.parse_args()
    if args.cmd == 'setup':
        sys.exit(cmd_setup(args))
    if args.cmd == 'status':
        sys.exit(cmd_status(args))
    if args.cmd == 'rotate':
        sys.exit(cmd_rotate(args))
    parser.print_help()
    sys.exit(1)
