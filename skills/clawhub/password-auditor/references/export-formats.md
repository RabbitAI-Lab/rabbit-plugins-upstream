# Supported Vault Export Formats

All major password managers export to CSV. `password_auditor.py` auto-detects the shape by header sniffing and normalizes to an internal record:

```python
Entry(title, username, password, url, last_modified, folder)
```

## Field Mappings

| Manager | title | username | password | url | last_modified | folder |
|---|---|---|---|---|---|---|
| Bitwarden | `name` | `username` | `password` | `login_uri` | `login_updated` (ISO) | `folder` |
| 1Password | `Title` | `Username` | `Password` | `URL` | `Date Modified` (epoch) | `Folder` |
| KeePass (CSV) | `Title` | `UserName` | `Password` | `URL` | — (falls back to export mtime) | `Group` |
| Chrome | `name` | `username` | `password` | `url` | — | — |
| Firefox | `url` | `username` | `password` | `url` | — | — |
| Generic | first text column | best-guess | longest secret-looking column | any http(s) column | any date column | any other text column |

**Generic JSON:** expects a top-level array (or `{"items": [...]}`) of objects; keys are matched case-insensitively against `title/name/label`, `username/user/login/email`, `password/secret/pass`, `url/uri/website`, `modified/updated/changed`.

## Detection Logic

1. Try JSON parse → if list-of-objects, use generic JSON path.
2. Read CSV header → exact match against known headers above.
3. Fall back to heuristic column typing (dates match ISO/epoch patterns, URLs start with a scheme or contain a dot-TLD).

## Exporting Safely

- **Bitwarden:** Tools → Export Vault (CSV, "file-protected" if offered).
- **1Password:** File → Export → All Items (CSV). Note the warning banner.
- **Chrome:** `chrome://password-manager/settings` → Export passwords (or `settings/passwords` on older builds).
- **KeePass:** File → Export → CSV (via plugin or built-in on 2.x).

**Golden rule:** export to a temp directory, audit, then `shred -u` the file. On macOS use `rm -P`. Never leave exports in Downloads or synced folders.

## TOTP Detection

TOTP secrets are looked for in fields named `totp`, `login_totp`, `otp`, `authenticator`, or a `otpauth://` URL anywhere in the row. Bitwarden CSVs carry `login_totp`; 1Password includes `OTPAuth` columns on newer exports.

## Extending the 2FA Seed List

The built-in list covers major sites (email, banking, social, gaming, government). To extend, pass a custom list:

```bash
python3 scripts/password_auditor.py --vault export.csv \
  --twofa-list my_2fa_domains.txt
```

One domain per line, bare registrable domain (`github.com`, not `https://github.com/login`). Sources like 2fa.directory export cleanly to this shape.
