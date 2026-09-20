## Description:

Helps agents set up, audit, repair, and restore deterministic 6-hour backups for Daniel-owned workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daniel-refahi-ikara](https://clawhub.ai/user/daniel-refahi-ikara)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Daniel-owned agent operators use this skill to configure and audit deterministic backups of agent memory and workspace state, then restore from the backup repository after host loss or migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The backup runner can push selected workspace state to git on a recurring schedule.

Mitigation: Confirm the Daniel-approved remote, branch, credential method, allowlist, .gitignore, scheduler payload, and notification target before enabling the runner.

Risk: Credentials, environment files, runtime stores, logs, transcripts, databases, or large private files could be included if backup boundaries are configured incorrectly.

Mitigation: Keep protected material out of git, stage only allowlisted restore-relevant paths, and run path and content safety checks before committing.

Risk: Backup failures may leave restore-relevant state stale if commit or push errors are not noticed.

Mitigation: Use separate health monitoring for scheduler status, runner availability, credentials, remote access, push results, freshness, and notification delivery.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with checklists and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes backup setup, audit, restore, scheduler, notification, allowlist, and exclusion guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
