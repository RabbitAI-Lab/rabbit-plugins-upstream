# Changelog

## 1.2.0 — 2026-10-27

Security hardening after a ClawHub audit export (ClawScan / AIG / SkillSpector).
The audit verdict was `suspicious`, driven by one reachable coding defect and
two over-broad capabilities. All material findings are addressed below.

### Fixed — unscoped process termination (audit: AIG T09, SDI-2, MEDIUM)

`scripts/install_watchdog_admin.bat` killed every process by image name:

```bat
taskkill /f /im wscript.exe
taskkill /f /im node.exe
```

Run with an elevated token, this could terminate unrelated Node.js and Windows
Script Host workloads on the machine. Replaced with a scoped restart of the
named task:

```bat
schtasks /End /TN "OpenClaw Gateway"
schtasks /Run /TN "OpenClaw Gateway"
```

No `taskkill` and no `/im` remain anywhere in the installer.

### Fixed — arbitrary command execution (audit: SDI-2, MEDIUM)

`scripts/watchdog-maintenance.ps1` executed `$Command[0]` with any arguments
supplied. It now validates the full argument vector against a fixed allowlist,
resolves the `openclaw` executable from known paths instead of trusting `PATH`,
and exits 3 on anything not listed. Run with `list` to print the allowlist.

### Changed — auto-repair is now off by default (audit: SDI-1, MEDIUM)

The watchdog previously ran `openclaw doctor --fix --non-interactive`
automatically whenever a restart attempt failed, letting a hidden long-running
process modify local OpenClaw state without operator approval.

New switch, at the top of `scripts/watchdog.ps1`:

```powershell
$AUTO_DOCTOR = $false   # set to $true to opt in
```

Default behaviour is now restart-only. `Invoke-DoctorFix` returns immediately
when the switch is off and logs that it was skipped.

### Fixed — contradictory self-refresh message (audit: SDI-4, LOW)

`$SELF_REFRESH_HOURS` was 24 but the log line claimed a "72h limit". The message
now reports the actual configured interval:

```
>> Self-refresh: relaunching watchdog (interval 24h)
```

### Added — disclosure and reversibility (audit: SQP-2, MEDIUM)

- `README.md` rewritten: an explicit "What this does to your machine" table,
  a confirmation prompt in the installer, disable and uninstall procedures,
  and a known-limitations section.
- `SKILL.md` gained "Security & scope disclosure" and "Uninstall" sections.
- The installer now lists its changes and requires typing `Y`.

### Not changed — audit false positives

Two SkillSpector findings were reviewed and dismissed:

- **AR2 (Anti-Refusal, HIGH)** — the phrase `do NOT judge` in `watchdog.ps1` is a
  comment explaining that the maintenance lock suspends health judgement. It is
  not an instruction to suppress user warnings. The auditor itself recorded this
  as not accepted.
- **EA3 (Excessive Agency, LOW)** — matched the string `NOT LIMITED TO` inside the
  MIT-0 warranty disclaimer. Not a capability statement.

### Carried over from 1.1.0

Single-instance mutex (`Global\OpenClawWatchdog_SingleInstance`). Version 1.0.0
combined a `while($true)` loop with a 5-minute repetition trigger and stacked
eight concurrent copies in 25 minutes. The mutex makes an accidental second
launch exit immediately.

---

## 1.1.0 — 2026-10-27

- Added single-instance mutex to `watchdog.ps1`
- `SKILL.md`: new "Single-instance guard" section explaining why a long-running
  loop must not be launched by a repeating trigger

## 1.0.0 — 2026-10-10

- Initial release: 5s health checks, restart on crash, hidden operation,
  tray status icon, maintenance lock, dynamic path resolution, log rotation,
  self-refresh, admin installer
