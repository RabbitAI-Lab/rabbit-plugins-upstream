## Description:

Audits a local OpenClaw setup for security issues and reports prioritized findings and changes over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and administrators use this skill to audit their local agent setup, prioritize security findings, and check for changes since an earlier run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit can read sensitive local configuration, logs, session records, installed skills, and credential-store contents.

Mitigation: Run only when comfortable with that access; use --no-host, --no-sockets, --no-deptree, or --no-native to narrow the audit.

Risk: Audit history and optional monitoring can retain local state.

Mitigation: Use --no-history to skip routine history; enable --monitor or --watch only when local baseline storage is wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gl0di/skills/clawseccheck)
- [User guide](docs/USAGE.md)
- [Security model](SECURITY_MODEL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chat summary and optional text, JSON, SARIF, HTML, SVG, or PDF reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An A–F grade is shown only when all five audit layers run; otherwise the report identifies missing coverage.]

## Skill Version(s):

4.3.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
