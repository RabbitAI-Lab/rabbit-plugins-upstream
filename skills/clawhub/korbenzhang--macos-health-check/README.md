# macOS Health Check

An OpenClaw skill for keeping a Mac that is used as a work computer fast and tidy.

- **Measures** memory pressure, CPU load, disk use and the largest folders, startup items and
  background services, leftovers of uninstalled apps, and backup state, with read-only commands.
- **Proposes** cleanup as a list with measured benefit, risk and rollback; nothing changes
  without the owner's approval.
- **Never removes system or network extensions**; it reports them.
- **Deletes only to the Trash** (`trash`), never with `rm`, and never empties the Trash.
- **Stays out of protected places** (Desktop, Documents, Downloads, iCloud Drive, Photos, Mail,
  other apps' containers), uses no `sudo`, grants no privacy permissions, reads no secrets, and
  never starts a macOS upgrade.

Works with a paired macOS node (`exec` on the Mac) or without one: the agent hands the owner a
command block and reads the pasted output.

Everything is in `SKILL.md`: boundaries, workflow, the read-only measurement blocks, the
proposal format, Trash discipline, and the log format.

Tested read-only on macOS 26 (Apple silicon), November 2026.
