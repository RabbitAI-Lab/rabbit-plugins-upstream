# Aegis4All High-Risk Operation Guides

> Based on Zheng, J., Tan, J., & Lin, J. (2026). Understanding and mitigating the risks of OpenClaw for non-technical users: A practical guide with Skill. arXiv preprint arXiv:2606.11007. 

>
> Five guides covering system-level security operations. Each guide includes Windows and Linux/macOS paths with verification steps.

---

## Guide 1: Create a Standard User for OpenClaw

> Strategy: **LP (Least Privilege)** | Critical | Estimated: 10-15 minutes

### Why

When OpenClaw runs as Administrator/root, a compromised agent can modify the OS kernel, install backdoors, and access all files.
Running as a standard user limits the blast radius to that user's directory only.

> **Important: Copy the config directory to the new user BEFORE switching.**
> Switching without copying leaves the new user with no OpenClaw config -- OpenClaw will not start.

---

### Windows

#### Step 0: Open PowerShell as Administrator, backup and copy config

```powershell
# 0a. Backup current config
$backupDir = "$env:USERPROFILE\openclaw-backup-$(Get-Date -Format 'yyyyMMdd')"
Copy-Item -Recurse "$env:USERPROFILE\.openclaw-autoclaw" $backupDir -ErrorAction SilentlyContinue
Copy-Item -Recurse "$env:USERPROFILE\.openclaw" $backupDir -ErrorAction SilentlyContinue
Write-Host "Backup created: $backupDir"

# 0b. Find OpenClaw config directory
$ocDirs = @("$env:USERPROFILE\.openclaw", "$env:USERPROFILE\.openclaw-autoclaw", "$env:USERPROFILE\.clawdbot")
$ocSource = ""
foreach ($d in $ocDirs) { if (Test-Path $d) { $ocSource = $d; break } }
Write-Host "OpenClaw config dir: $ocSource"

# 0c. Copy to new user directory
$targetPath = "C:\Users\openclaw-user\$(Split-Path $ocSource -Leaf)"
Copy-Item -Recurse $ocSource $targetPath
Write-Host "Copied to: $targetPath"

# 0d. Grant read/write to new user
icacls $targetPath /grant "openclaw-user:(OI)(CI)F" /T
Write-Host "Permissions granted to openclaw-user"
Write-Host ">>> Config copied. Now proceed with steps 1-4 below. <<<"
```

#### Steps 1-4: Create the standard user

1. `Win + I` -> "Accounts" -> "Family & other users"
2. "Add someone else to this PC" -> "I don't have this person's sign-in information" -> "Add a user without a Microsoft account"
3. Username: `openclaw-user`. Set strong password (12+ chars, upper+lower+digits+symbols).
4. After creating, click the account -> "Change account type" -> select "Standard User"

#### Steps 5-6: Switch and verify

5. Sign out -> Sign in as `openclaw-user`
6. OpenClaw should start normally (config was pre-copied in Step 0)

> Verify: `Win + R` -> `cmd` -> `whoami` shows `COMPUTERNAME\openclaw-user`. `net localgroup administrators` does NOT include this user.

---

### Linux / macOS

#### Step 0: Backup and copy config (in current terminal)

```bash
NEW_USER="openclaw-user"

# Find OpenClaw config directory
OC_DIR=""
for d in ~/.openclaw ~/.openclaw-autoclaw ~/.clawdbot; do
    [ -d "$d" ] && OC_DIR="$d" && break
done
echo "OpenClaw config dir: $OC_DIR"

# Backup
cp -r "$OC_DIR" ~/openclaw-backup-$(date +%Y%m%d)

# Copy to new user home
sudo cp -r "$OC_DIR" "/home/$NEW_USER/$(basename "$OC_DIR")"
sudo chown -R "$NEW_USER:$NEW_USER" "/home/$NEW_USER/$(basename "$OC_DIR")"
echo "Config copied. Now create user and switch."
```

#### Steps 1-3: Create user and verify

```bash
sudo useradd -m -s /bin/bash openclaw-user
sudo passwd openclaw-user
groups openclaw-user    # should NOT contain sudo or wheel
```

#### Steps 4-5: Verify Node.js + config + switch

```bash
# 4a. Verify Node.js is accessible to the new user
# Option A (recommended): Node in system path
which node && which npm       # typically /usr/local/bin/node or /usr/bin/node
sudo -u openclaw-user node -v  # verify new user can see it

# Option B: Node lives in root homedir (e.g. nvm), install separately for new user
# su - openclaw-user
# curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
# nvm install --lts
# Once done, exit back to root

# 4b. If Gateway port < 1024, grant capability
sudo setcap cap_net_bind_service=+ep $(which node)

# 4c. Verify config is in place
ls /home/openclaw-user/.openclaw*   # should show config files

# 4d. Switch user (NOTE: su - not su -- the dash loads full environment!)
# ** IMPORTANT: Gateway must restart under the new user. Brief disconnection is normal.
#    If you stopped Gateway before switching -> start it in Step 5 below.
#    If you did NOT stop Gateway -> old process still runs as root.
#    Kill it (sudo kill PID), then start fresh as new user.
#    Goal: Gateway runs as openclaw-user.
su - openclaw-user
```

#### Step 5: Start Gateway under the new user

```bash
# Check environment
whoami          # should show openclaw-user
node -v         # verify Node is available
ls ~/.openclaw-autoclaw/  # verify config files

# Start
openclaw gateway start

# Verify Gateway is alive
ps aux | grep openclaw
```

> Verify: `whoami` shows `openclaw-user`. `id` output does NOT contain `0(root)` or `27(sudo)`. `ps aux | grep openclaw` shows Gateway process.
>
> **Common failures:**
> - `node: command not found` -> Node not in new user's PATH. Go back to 4a and install.
> - Environment variables all empty after `su` -> you used `su` without `-`. Exit and use `su -`.
> - Port already in use -> `sudo lsof -i :port` and kill the old process.
> - To switch back to original user -> `exit` returns to root. All files intact.
> - **If QQ/Discord/WeChat channels are unresponsive after Gateway restart -> NORMAL! Re-authorize them.**
>   The new Gateway process has a fresh session; old channel tokens must be reconnected.

---

### Rollback

If anything goes wrong: **switch back to the original admin account.** All original files are untouched and the config directory is preserved.

---

## Guide 2: Bind to localhost + Change Default Token

> Strategy: **LP (Least Privilege)** | Critical | Estimated: 3-5 minutes

### Why

Over 140,000 OpenClaw instances were found publicly exposed in early 2026. Port bound to `0.0.0.0` means anyone who can reach your IP can connect to and control your Agent. Change to `127.0.0.1` for local-only access.

### Steps

1. Find config: `~/.openclaw/config.yaml` or `~/.clawdbot/config.yaml`
2. Search for `host`. Ensure it is `127.0.0.1` (NOT `0.0.0.0` or `lan`)
3. Search for `token`. Ensure it is NOT a default value (admin/password/openclaw/123456)
4. Generate strong random token:

```powershell
# Windows PowerShell
-join ((48..57)+(65..90)+(97..122) | Get-Random -Count 32 | % {[char]$_})
```

```bash
# Linux / macOS
openssl rand -hex 32
```

5. Set in config: `token: "generated-random-string"`
6. Save -> `openclaw gateway restart`

> Verify: `netstat -an | findstr "port"` shows `127.0.0.1:port`, not `0.0.0.0`.

---

## Guide 3: API Key Secure Storage

> Strategy: **CG (Credential Guard)** | Critical | Estimated: 8-12 minutes

### Why

In 2026, OpenClaw config leaks exposed 1.5+ million API tokens. Key in config file -> git push -> leak -> fraudulent charges.

The fix: store keys in environment variables. Config file references variable names only.

### Step 1: Write to environment variables

**Windows**: `Win+R` -> `sysdm.cpl` -> Advanced -> Environment Variables -> User variables -> New:

| Variable | Value |
|----------|-------|
| `OPENAI_API_KEY` | `sk-yourKey` |
| `ANTHROPIC_API_KEY` | `sk-ant-yourKey` |
| `GLM_API_KEY` | `yourKey` |

Restart to apply. (Only set the ones you use.)

**Linux/macOS**: Edit `~/.bashrc` or `~/.zshrc`, append:

```bash
export OPENAI_API_KEY="sk-yourKey"
export ANTHROPIC_API_KEY="sk-ant-yourKey"
```

`source ~/.bashrc` to apply.

### Step 2: Update config file

```yaml
# Dangerous
apiKey: "sk-abc123..."

# Safe
apiKey: ${OPENAI_API_KEY}
```

### Step 3: Add to .gitignore

```bash
cd ~/.openclaw
echo "config.yaml" >> .gitignore
echo ".env" >> .gitignore
```

### Step 4: Rotate regularly

Every 90 days: log in to API platform -> generate new key -> update env var -> delete old key. If compromise suspected -> rotate **immediately**.

---

## Guide 4: API Prepaid Billing + Usage Alerts

> Strategy: **PB (Prepay Breaker)** | Medium | Estimated: 5-8 minutes

### Why

Credit card with no spending cap -> one runaway task can burn hundreds of dollars. Prepaid = hard circuit breaker: balance hits zero, service stops.

### Platform-specific setup

| Platform | Action |
|----------|--------|
| OpenAI | Billing -> Remove credit card -> Add to credit balance -> Disable auto-recharge -> Set usage limit |
| Anthropic | Billing -> Prepaid mode -> Disable auto-recharge -> Set spend limit |
| GLM | Billing center -> Top up balance; confirm NOT on post-paid |
| DeepSeek | platform.deepseek.com/top_up -> Top up; confirm auto-recharge is off |

### Set usage alerts

Enable alerts on each platform's Billing / Notifications page:

| Threshold | Alert |
|-----------|-------|
| 50% | Info notification |
| 80% | Email warning |
| 90% | Email + SMS |

### Daily habits

- Simple task running >2 min or complex >10 min -> tell Agent to stop, check usage
- Spend 1 minute weekly checking API usage dashboard

---

## Guide 5: Safe OpenClaw Upgrade

> Strategy: **CU (Cautious Updates)** | Medium | Estimated: 5 min + wait 3-5 days

### Upgrade philosophy

**Patches immediately. Features can wait.**

### 1. Backup

```bash
cp -r ~/.openclaw ~/openclaw-backups/backup-$(date +%Y%m%d)
```

### 2. Read Release Notes

<https://github.com/openclaw/openclaw/releases>

- Contains security/vulnerability/CVE -> **upgrade immediately**
- Contains new feature/improvement -> **wait 3-5 days**

### 3. Observe community

- Discord: <https://discord.com/invite/clawd>
- GitHub Issues: <https://github.com/openclaw/openclaw/issues>
- Many problem reports -> keep waiting

### 4. Execute upgrade

```bash
npm update -g openclaw
# or: openclaw self-update
```

### 5. Post-upgrade

```bash
openclaw doctor --fix    # fix config drift
```

Tell agent "safe check" to verify ports, tokens, and sandbox settings weren't reset.

### Rollback

```bash
openclaw gateway stop
rm -rf ~/.openclaw
cp -r ~/openclaw-backups/backup-YYYYMMDD ~/.openclaw
openclaw gateway start
```

### Cloud platforms

Use managed upgrade path (not manual file overwrite). Create disk snapshot before upgrade. Roll back snapshot on failure.
