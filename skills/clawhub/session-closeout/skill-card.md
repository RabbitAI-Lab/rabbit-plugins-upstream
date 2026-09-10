## Description:

Run a read-only end-of-session audit of the current workspace and report what still needs attention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jkfaris94](https://clawhub.ai/user/jkfaris94)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill at explicit session closeout to check task, repository, project-documentation, and automation hygiene before recording the final session outcome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Printed workspace and project paths may be hard to review safely when directories have untrusted or unusual names.

Mitigation: Treat the report as advisory and manually review unexpected path names before acting on them.

Risk: The audit does not verify external automation health.

Mitigation: Check cron jobs and other automation health manually when closeout depends on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jkfaris94/skills/session-closeout)
- [OpenClaw project](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text key-value audit report with human-facing summary guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only audit output; the caller records any closeout notes separately.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
