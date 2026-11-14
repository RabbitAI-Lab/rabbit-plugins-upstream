---
name: macos-health-check
description: "Check a Mac used as a work computer: memory pressure, CPU load, disk use, startup items, app leftovers, backup state. Read-only commands, cleanup only as proposals with a rollback, deletes only to the Trash."
metadata:
  {
    "openclaw":
      {
        "emoji": "🩺",
      },
  }
---

# macOS Health Check

Measure first, then propose, then act only after the owner approves. Every command in the
section "Measurements" below is read-only, needs no `sudo`, and stays out of privacy-protected
folders. Cleanup is always a proposal with benefit, risk and rollback (section "Cleanup proposals").
Everything this skill needs is in this one file.

Works in two modes:

- **Shell on the Mac** (a paired macOS node, or an agent running on the Mac): run the commands
  yourself, one block at a time.
- **No shell on the Mac:** give the owner the command block to paste into Terminal and read the
  pasted output. Never ask for screenshots of private windows; ask for command output instead.

This skill has no `os` filter on purpose, so an agent on a Linux gateway can use it in paste mode.

## Boundaries

1. **Read-only measuring.** No `sudo`, no `tmutil` writes, no `defaults write`, no `launchctl`
   load/unload/bootout, no `kill`, no `mdutil -i`/`-E`, no `memory_pressure -l` (it simulates
   pressure instead of reading it).
2. **Protected places stay closed.** Do not list, size or search Desktop, Documents, Downloads,
   iCloud Drive (`~/Library/Mobile Documents`), `~/Library/CloudStorage`, the Photos library,
   Mail, Messages, Safari data, removable or network volumes, or other apps' containers
   (`~/Library/Containers`, `~/Library/Group Containers`). Reading them either fails silently,
   opens a macOS privacy dialog, or downloads cloud-only files. Do not use `osascript`/System
   Events, `sfltool`, or `security`. When a number from such a place matters, ask the owner to
   read it in Finder or System Settings → General → Storage.
3. **Never grant privacy permissions** (Full Disk Access, Accessibility, Screen Recording,
   Automation) to the process that runs your commands, and never suggest it as a shortcut.
4. **Announce dialogs.** If a step can open an admin or privacy dialog, say so before running it,
   prefer a variant without one, and let the owner decide.
5. **Delete only to the Trash.** Use `trash <path>` (`/usr/bin/trash`, built into current macOS) or Finder,
   never `rm`, `rm -rf`, `unlink`, `srm`, or tools that empty the Trash. Check the path still
   exists before and is gone after (`[ -e "<path>" ]`). If `trash` fails, stop and ask.
6. **Backup before larger cleanup.** Before removing anything beyond caches, confirm a recent
   backup (Time Machine or the owner's own) exists; if unknown, ask the owner first.
7. **No secrets.** Do not read the keychain, password stores, tokens, browser profiles or
   private files. Leave out user names, host names and serial numbers when quoting output.
8. **No OS upgrade or firmware change.** Report available updates; never start them.
9. **No scratch files by default.** The measurement blocks write nothing to disk. If a step really
   needs a scratch file, create it only with `mktemp` (never a fixed, predictable name), tell the owner its path in the report, and propose moving it to the Trash
   when done.
10. **Extensions stay untouched.** Never remove or disable system or network extensions (VPN,
   firewall, antivirus, endpoint security, content filters) and never give removal steps; report
   them and leave the decision to the owner.
11. **Approval is per step.** An approval covers exactly the item and command shown; if the item,
   path, or command changes, ask again. Measurement output with personal data (file or account
   names) stays with the owner and goes nowhere else without their explicit consent.
12. **Leave other tools alone.** Do not remove the agent runtime, package managers, their taps or
   launch agents, or developer checkouts without the owner naming them explicitly.

## Workflow

1. **Intake.** Ask what feels wrong (slow, full disk, fan, battery, beach balls), since when, and
   what changed (new app, update, uninstall). Note macOS version and RAM from section 1.
2. **Measure.** Run the blocks of section "Measurements" that fit the complaint; for a general check run all. Record each value with date, time and
   the exact command. Old measurements are not evidence for today: measure again.
3. **Interpret.** Name what a number counts (Chrome renderer processes are not tabs; compressed
   memory is not swap). Separate measured facts from guesses.
4. **Propose.** Build a numbered list of actions, each with benefit (expected effect, measured
   size), risk, rollback, and whether a dialog or admin password is needed
   (section "Cleanup proposals"). Biggest effect first.
5. **Approval.** Wait for the owner's explicit choice per action. No approval, no change.
6. **Act.** One action at a time, with `trash` for anything removed. Stop at the first surprise.
7. **Measure again.** Repeat the measurement that motivated the action and show before/after.
8. **Log.** Keep a short log: date, action, command, before/after, rollback. Keep open findings
   in a list so nothing is lost.

## Done when

- Every value in the report names its command and time.
- Every proposed action has benefit, risk and rollback, and nothing ran without approval.
- Every executed action has a before/after measurement and a log entry.
- Places that were not checked (protected folders, admin-only paths) are named in the report.

## Measurements (read-only)

All commands run as the logged-in user, without `sudo`, and avoid privacy-protected folders.
macOS has no `timeout` command; set time limits in the tool that runs the command. Paste mode:
hand the owner one section at a time and ask for the full output.

### M1. System basics

```sh
sw_vers
sysctl -n hw.model hw.memsize hw.ncpu machdep.cpu.brand_string
uptime
softwareupdate --history | tail -5
```

- `hw.memsize` is bytes (divide by 1073741824 for GiB).
- `uptime` matters for memory and swap: long uptimes pile up compressed memory and swap.
- Do not run `softwareupdate --list`/`-l` repeatedly; it contacts Apple and can take minutes.
  Never `--install`.

### M2. Memory pressure

```sh
memory_pressure | tail -1
sysctl vm.swapusage kern.memorystatus_vm_pressure_level
vm_stat | head -12
top -l 1 -o mem -n 15 -stats pid,command,mem,cmprs
```

- `memory_pressure` without options only reads. Never add `-l` (simulates pressure).
- `kern.memorystatus_vm_pressure_level`: 1 normal (green), 2 warning (yellow), 4 critical (red).
- `vm_stat` counts pages; page size is in its first line (16384 bytes on Apple silicon).
- Swap in use with pressure level 1 is history, not a current problem; pressure 2 or 4 with
  growing swap is.
- Group `top` output by app: browsers spread over many helper processes.

### M3. CPU load

```sh
sysctl -n vm.loadavg
top -l 2 -s 3 -o cpu -n 10 -stats pid,command,cpu,time | tail -12
pmset -g therm
```

- The first `top` sample has no CPU percentages; the second (after `-s 3` seconds) does. `tail`
  keeps only the second.
- Load average above the core count (`hw.ncpu`) for minutes means the Mac is busy, not only one
  spike.
- `pmset -g therm` shows thermal or CPU speed limits if any are active.

### M4. Disk use and largest folders

```sh
df -h / /System/Volumes/Data
diskutil apfs list | grep -E "Capacity (In Use|Not Allocated)|Name:" | head -20
tmutil listlocalsnapshots /
```

Largest visible folders in the home folder, skipping protected places (hidden folders are not
measured; they hold settings and keys):

```sh
cd ~ && for d in *; do
  case "$d" in
    Desktop|Documents|Downloads|Library|Pictures|Movies|Music|Public) continue;;
  esac
  [ -d "$d" ] && [ ! -L "$d" ] && du -xsk "$d" 2>/dev/null
done | sort -n | tail -15
```

Size of the three `~/Library` folders that usually grow without holding private data:

```sh
cd ~/Library && du -xsk Caches Logs Developer 2>/dev/null | sort -n
```

Everything else in `~/Library` (app support data, browser data, containers, mail) is not measured;
the owner reads it under System Settings → General → Storage.

Drill down only into a folder found above, one level at a time:

```sh
du -xsk "$HOME/Library/Caches"/* 2>/dev/null | sort -n | tail -15
```

- Large hidden tool caches (for example package-manager caches) are not measured; ask the owner
  which tools they use and where those tools report their cache size.
- `du -k` prints KiB; divide by 1048576 for GiB.
- `df` on APFS shows the shared container; "free" includes purgeable space macOS can reclaim.
- Local Time Machine snapshots use space that macOS frees on demand; do not delete them.
- Desktop, Documents, Downloads, Pictures, Movies, Music: ask the owner to read sizes in Finder
  (Get Info) or System Settings → General → Storage. Desktop and Documents may live in iCloud
  Drive; sizing them can download cloud-only files.

### M5. Startup items and background services

```sh
ls -1 ~/Library/LaunchAgents /Library/LaunchAgents /Library/LaunchDaemons 2>/dev/null
launchctl list | awk 'NR==1 || $3 !~ /^com\.apple\./' | head -60
systemextensionsctl list
```

For one launch agent or daemon, read what it starts and who signed it:

```sh
plutil -p ~/Library/LaunchAgents/<label>.plist
codesign -dv --verbose=2 "<path of Program or ProgramArguments[0]>" 2>&1 | grep -E "Identifier|TeamIdentifier|Authority=Developer"
```

- `launchctl list` columns: PID (`-` = not running), last exit status, label.
- If the program is a shell or interpreter (`/bin/sh`, `python3`, `node`), `codesign` shows the
  Apple binary; check the script path in `ProgramArguments` instead.
- A helper is only orphaned if no installed app shares its **Team ID** or vendor; app names change
  (renamed products, acquisitions). Check the Team ID before calling anything a leftover.
- Login items and "Allow in the background" switches: ask the owner to read System Settings →
  General → Login Items & Extensions. `sfltool dumpbtm` needs an admin password; do not use it
  without announcing it.
- System and network extensions (VPN, firewall, antivirus, endpoint security, filters): **never
  remove or disable them, and never give removal steps.** Removing the wrong one can cut the
  network, a VPN, or security protection. Report each one with its developer and state and leave
  the decision to the owner (and their IT or security vendor if the Mac is managed).

### M6. App leftovers

Vendor prefixes of installed apps (including helper apps inside bundles), then support folders
named like a bundle ID whose vendor matches no installed app:

```sh
vendor_of() { sed -E 's/^group\.//; s/^[A-Z0-9]{10}\.//' | tr 'A-Z' 'a-z' | cut -d. -f1-2; }
vendors=$( { mdfind -onlyin /Applications "kMDItemContentType == 'com.apple.application-bundle'"
  ls -d ~/Applications/*.app 2>/dev/null; } | while read -r a; do
  /usr/libexec/PlistBuddy -c "Print :CFBundleIdentifier" "$a/Contents/Info.plist" 2>/dev/null
done | vendor_of | sort -u )
echo "installed vendors: $(printf '%s\n' "$vendors" | wc -l)"
for base in Preferences Caches "Application Support" "Saved Application State" LaunchAgents Logs; do
  ls -1 "$HOME/Library/$base" 2>/dev/null | sed 's/\.plist$//; s/\.savedState$//' |
  grep -E '^[A-Za-z0-9-]+\.[A-Za-z0-9-]+\.' | grep -iv -e '^com\.apple\.' -e '^systemgroup\.' |
  while read -r n; do
    v=$(echo "$n" | vendor_of)
    printf '%s\n' "$vendors" | grep -qxF "$v" || echo "$base/$n"
  done
done | sort | head -150
```

- Nothing is written to disk; the vendor list lives in a shell variable for this block only.
- The block only lists folder names; it opens and sizes nothing.
- Vendor matching compares the first two parts of the bundle ID, case-insensitive, after dropping
  a leading `group.` or Team ID. Country domains such as `jp.co.<vendor>` collapse to two parts;
  check those by hand.
- This is a candidate list, not proof. Typical false positives: vendors whose app uses another
  bundle ID prefix (scanner or printer suites, renamed products), SDK names that apps write
  under their own name (`com.amplitude`, `org.chromium`, `org.webkit`, `com.github`),
  command-line tools and package managers, the agent runtime itself, background helpers from
  M5, and the owner's own scripts. Check vendor and Team ID before proposing anything.
- Size a candidate with `du -sk <exact path>` only after the owner has picked it for removal; skip anything inside `Containers` or
  `Group Containers` (privacy dialog). Ask the owner to check those in Finder.
- Apps that wrote folders into Documents, Desktop or Downloads are not visible here; say so in
  the report and let the owner look in Finder.
- Leftovers in `/Library` (system-wide) need an admin password to move; list them, size them,
  and give the owner one exact command to run in their own Terminal.

### M7. Backup state

```sh
tmutil destinationinfo
tmutil status
```

- `destinationinfo` lists Time Machine targets and whether one is mounted; `status` shows a
  running backup (`Running = 1`).
- `tmutil listlocalsnapshots /` (M4) shows the newest local snapshot; Time Machine makes
  one with each backup, so its timestamp is a good hint for the last run.
- `tmutil latestbackup` needs Full Disk Access for the calling process and fails without it. Do
  not grant that; ask the owner to read the last backup time in System Settings → General → Time
  Machine.
- No Time Machine target does not mean no backup: ask what else the owner uses.

### M8. Spotlight and indexing (when the Mac is busy without a visible app)

```sh
mdutil -s /
top -l 2 -s 3 -o cpu -n 20 -stats pid,command,cpu | grep -E "mds|mdworker|backupd|photoanalysisd|bird|cloudd" | tail -10
```

- `mdutil -s` only reads the indexing status. Rebuilding the index (`-E`) needs approval.
- `bird`/`cloudd` busy for a long time point to iCloud sync, `backupd` to Time Machine.

## Cleanup proposals

Nothing in this file runs without the owner's explicit approval of the specific action.

### Proposal format

One numbered row per action, biggest measured effect first:

| # | Action | Benefit (measured) | Risk | Rollback | Dialog / admin |
|---|---|---|---|---|---|
| 1 | Move `~/Library/Caches/<vendor>` to the Trash | 2.9 GiB, `du -sk` 14:02 | App rebuilds the cache, first start slower | Put back from Trash | none |
| 2 | Quit and remove login item `<app helper>` | ~400 MB RAM, `top` 14:05 | Feature of `<app>` stops starting at login | Re-enable in Login Items | System Settings, owner clicks |

Rules for the list:

1. Every benefit is a measurement with command and time, not an estimate. If only an estimate is
   possible, write "estimate" and why.
2. Name what the owner loses (sync, a background feature, saved window state).
3. Rollback must be concrete: "Put back from Trash", "re-enable switch X", "reinstall from
   vendor". If there is no rollback, say so and put the item last.
4. Mark anything that needs an admin password, a privacy dialog, or the owner's own Terminal.
5. Say which places were not checked (protected folders, containers, `/Library`) and how the
   owner can check them in Finder.

### Common actions and their safe form

| Finding | Safe action | Avoid |
|---|---|---|
| Large user cache of one app | `trash ~/Library/Caches/<folder>` with the app quit | Emptying all of `~/Library/Caches`, cleaner apps that empty the Trash |
| Leftovers of an uninstalled app | `trash` each exact path from the checked candidate list | Wildcards, vendor names without Team ID check |
| Leftovers in `/Library` | Give the owner one exact command with exact paths for their own Terminal; they type the admin password | Running `sudo` yourself |
| Leftovers inside `~/Library/Containers` | Owner opens the folder in Finder (`open ~/Library/Containers`) and drags exact folders to the Trash | Sizing or listing inside containers from the agent's shell |
| Orphaned launch agent | Quit the program, `trash` the plist, log out and in, check `launchctl list` | `launchctl bootout`/`unload` without approval |
| System or network extension | Report it with developer and state; the owner decides, with their IT or security vendor if managed | Removing, disabling, or giving removal steps for any extension |
| High memory from a browser | Show per-app totals, suggest closing tabs or enabling the browser's memory saver | Killing processes |
| Swap high after long uptime | Suggest a restart at a convenient time, then measure again | Purge tools |
| Disk almost full | List the five biggest measured folders; suggest moving archives to external or network storage (copy, verify count and size, then Trash the original) | Deleting local Time Machine snapshots, moving files the owner has not named |
| Spotlight busy for hours | Show `mdutil -s /` and the busy processes; suggest waiting or excluding a build folder in System Settings → Spotlight | `mdutil -E` without approval |

### Trash discipline

1. Check the exact path exists: `[ -e "<path>" ] && echo present`.
2. Quit the app that owns it.
3. `trash "<path>"` (one path per argument, no wildcards).
4. Check it is gone: `[ -e "<path>" ] || echo gone`.
5. Moving to the Trash frees no space until the owner empties it. Tell them; never empty it
   yourself.

### Log entry

```text
YYYY-MM-DD HH:MM  <action>
command:  <exact command>
before:   <value, command>
after:    <value, command>
rollback: <how>
```
