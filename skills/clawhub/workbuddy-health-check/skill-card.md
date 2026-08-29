## Description:

Runs an eight-dimension local health check for a WorkBuddy environment, covering disk health, backup freshness, automation status, hardcoded credential scans, backup package integrity, configuration, memory sync, and cross-machine carrier readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators maintaining WorkBuddy environments use this skill to run a local safety and stability audit before synchronization, recovery, routine maintenance, or backup review. It produces prioritized P0/P1/P2 action guidance for issues such as stale backups, low disk space, automation failures, and credential-like strings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads WorkBuddy state, scans skill text for credential-like strings, inspects backup packages, and writes local reports that may contain sensitive operational findings or backup paths.

Mitigation: Run it only when a local WorkBuddy audit is intended, keep generated reports private by default, and review reports before sharing them.

Risk: The package security guidance says the privacy and integrity claims do not fully match the package contents.

Mitigation: Treat the ClawHub security verdict as requiring review, and validate the generated report contents against local disclosure expectations before operational use.

Risk: The package self-attestation hash is identified as unreliable until the publisher republishes consistent metadata.

Mitigation: Verify package and file hashes against server evidence before relying on the bundled attestation for integrity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/workbuddy-health-check)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report, machine-readable JSON summary, shell command usage, and prioritized remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local reports under ~/.workbuddy/health-check, keeps the most recent reports, uses exit codes 0/1/2 for pass/warn/critical status, and masks credential-like findings.]

## Skill Version(s):

1.0.0 (source: frontmatter, release metadata, manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
