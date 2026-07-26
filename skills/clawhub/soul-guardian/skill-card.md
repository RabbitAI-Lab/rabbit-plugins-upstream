## Description: <br>
Drift detection and baseline integrity guard for agent workspace files with automatic alerting support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davida-ps](https://clawhub.ai/user/davida-ps) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to monitor agent workspace instruction files for drift, review diffs and audit logs, and optionally restore critical files to approved baselines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Restore mode can overwrite protected workspace files back to approved baselines. <br>
Mitigation: Initialize baselines only from known-good files, and use --no-restore or an alert-only policy when automatic restoration is not desired. <br>
Risk: The guardian state directory can contain approved snapshots, diffs, audit data, and quarantined copies of sensitive workspace files. <br>
Mitigation: Keep the state directory private, prefer an external state directory, and use restrictive permissions such as chmod 700. <br>
Risk: Optional cron or launchd scheduling can run recurring local checks. <br>
Mitigation: Enable scheduling only after reviewing the exact command, state directory, agent identifier, and schedule. <br>
Risk: The skill cannot prove who changed a file and cannot protect the workspace if the same actor controls both the workspace and the state directory. <br>
Mitigation: Treat actor values as operational metadata, investigate drift sources separately, and maintain independent backups or mirrors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davida-ps/skills/soul-guardian) <br>
- [Project homepage](https://clawsec.prompt.security) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and plain-text drift alerts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create local state files, audit JSONL, patch files, quarantine copies, and optional launchd plist files when the documented commands are executed.] <br>

## Skill Version(s): <br>
0.0.6 (source: frontmatter, changelog, skill.json, server release evidence; released 2026-05-14) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
