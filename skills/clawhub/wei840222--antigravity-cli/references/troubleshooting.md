# Troubleshooting

Source: <https://antigravity.google/docs/cli/troubleshooting/>. Delete a lock or change keychain settings only when the user asked to fix that symptom.

| Symptom | Cause | Section |
| --- | --- | --- |
| `agy: command not found` | Install dir missing from `PATH` | PATH |
| Hang, D-Bus warning, `secret keyring is locked` | Keyring locked or headless | Keyring |
| `local pasteboard is empty or unreachable over SSH connection` | Graphical clipboard not forwarded | SSH clipboard |
| Launch hang, upgrade skipped, `update.lock` warning | Stale lock or unwritable install dir | Updater |

## PATH

Installer path: `~/.local/bin`, or `C:\Users\<username>\AppData\Local\agy\bin`. Missing `PATH` entry:

```text
bash: agy: command not found
```

macOS and Linux: append to `~/.bashrc` or `~/.zshrc`, then `source` that same file. The official line quotes `~/.local/bin`, so the tilde does not expand. Use `$HOME`.

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Windows: run PowerShell as Administrator, then restart the terminal. The official command appends `C:\Program Files\Google\antigravity-cli`. That is not the documented install path `%LOCALAPPDATA%\agy\bin`. If the binary is in the Local AppData bin, add that directory instead.

```powershell
[System.Environment]::SetEnvironmentVariable("Path", [System.Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Program Files\Google\antigravity-cli", "User")
```

## Keyring

Tokens use Apple Keychain, Linux secret-service over D-Bus, or Windows Credential Manager. Locked or headless failure:

```text
Error: failed to retrieve token: secret keyring is locked
```

macOS: in Keychain Access, open the Antigravity CLI item and confirm Access Control allows `agy`. For headless SSH, set a 300-second auto-lock, unlock, then re-lock when finished:

```bash
security set-keychain-settings -l -u -t 300 ~/Library/Keychains/login.keychain-db
security unlock-keychain ~/Library/Keychains/login.keychain-db
security lock-keychain ~/Library/Keychains/login.keychain-db
```

Linux: unlock GNOME Keyring or KWallet. Over SSH, start D-Bus and confirm the keyring daemon is running:

```bash
export $(dbus-launch)
```

If it still fails, the official page points to keyring permissions or support. It does not document a file-based token fallback.

## SSH clipboard

`Ctrl+V` of a screenshot fails when the graphical clipboard is not forwarded. Use iTerm2 or Ghostty. In iTerm2: Preferences, General, Selection, allow terminal applications to access the clipboard (OSC 52 write). Inside tmux: `set -s set-clipboard on`.

## Self-updater

The updater is static and background. Under `~/.gemini/antigravity-cli/updater/`: `last_check.timestamp` is a 15-minute TTL, and `update.lock` is the advisory lock. A hung updater, a lock left after a crash, or a non-writable install dir blocks the next update.

```text
Warning: another background updater process is already active (update.lock)
```

For this symptom, in order:

1. `rm -f ~/.gemini/antigravity-cli/updater/update.lock`
2. Set `AGY_CLI_DISABLE_AUTO_UPDATE=true` in the shell profile.
3. Confirm the user can write `~/.local/bin/` (Unix) or `%LOCALAPPDATA%\agy\bin` (Windows).

Local `agy update` 1.4.12 accepts neither `-h` nor `--help`. It prints `Usage of update:` and exits.
