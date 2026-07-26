## Description: <br>
Recover from developer disasters with step-by-step runbooks for git mistakes, leaked credentials, disk exhaustion, runaway processes, database failures, deploy rollbacks, access lockouts, SSL expiry, and network failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill as an emergency runbook for diagnosing, fixing, and verifying recovery from common software, infrastructure, and access incidents. It is intended for time-sensitive incidents where commands and checklists must still be reviewed before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recovery commands can alter git history, remove local artifacts, prune containers or volumes, modify firewall or sudo access, restart services, or affect production systems. <br>
Mitigation: Confirm the exact repo, branch, host, database, account, and production impact before running commands; make backups or snapshots where feasible; coordinate with collaborators; and require explicit human approval for high-impact actions. <br>
Risk: Credential leak procedures can disrupt access or collaborators if revocation or history rewriting is applied to the wrong target. <br>
Mitigation: Identify the exact leaked credential and repository, revoke compromised credentials before cleaning history, coordinate collaborator re-clones, and verify the secret no longer appears after cleanup. <br>
Risk: Database and deploy recovery steps can cause data loss or downtime when applied without environment-specific context. <br>
Mitigation: Use backups, snapshots, transactions, and rollback tooling where available, then verify database state, service status, and health checks after each action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/emergency-rescue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with annotated shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes non-destructive defaults, flagged destructive steps, verification checks, and required human review before executing high-impact commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, released 2026-02-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
