## Description: <br>
Pure local file backup for a Mac workspace that inventories selected roots, plans guarded destinations, copies incrementally, verifies results, and reports backup status without deleting source files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual workspace owners use this skill to back up local project directories to an approved fixed folder and external drive, then check what is safe, stale, offline, or not yet backed up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and copy substantial private workspace data, including secret files. <br>
Mitigation: Review the configured sources and destinations before real runs, inspect the secret-file list, and use only destinations you intentionally want. <br>
Risk: Sensitive files may be exposed if a destination is inside iCloud or another synced folder. <br>
Mitigation: Avoid iCloud and other cloud-synced destinations unless you explicitly accept cloud exposure for the copied data. <br>
Risk: The first full backup may copy a large amount of data and reveal configuration mistakes. <br>
Mitigation: Keep the dry-run review step, inspect byte totals and destination verdicts, and supervise the first full backup. <br>
Risk: Changing the rsync binary or flags can alter backup behavior. <br>
Mitigation: Keep the default rsync path unless you have reviewed the compatibility notes and the run output. <br>


## Reference(s): <br>
- [First-run setup](references/first-run-setup.md) <br>
- [Destination policy](references/destination-policy.md) <br>
- [Ledger format](references/ledger-format.md) <br>
- [openrsync compatibility](references/openrsync-compat.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-backed backup status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses dry-run planning before writes and reports verification status from observed backup state.] <br>

## Skill Version(s): <br>
0.2.3 (source: server release metadata and CHANGELOG, released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
