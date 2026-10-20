## Description:

Audits a local OpenClaw setup for security risks and changes, reporting findings and an A–F grade only when all five check layers complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and administrators use this skill to inspect local configuration, installed skills, logs, and host security posture, then track changes and prioritize findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads local configuration, logs, installed skills, and credential-adjacent stores that may contain sensitive information.

Mitigation: Run only on an OpenClaw setup you are authorized to inspect; use --no-host or --no-native to narrow inspection.

Risk: History and optional monitoring retain local audit state, and exported reports may contain sensitive findings.

Mitigation: Use --no-history when persistence is unwanted, enable monitoring deliberately, protect exported reports, and use --purge to remove local state.

## Reference(s):

- [ClawSecCheck on ClawHub](https://clawhub.ai/gl0di/skills/clawseccheck)
- [User guide](docs/USAGE.md)
- [Audit scope](docs/playbook/SCOPE.md)
- [Output schema](docs/OUTPUT_SCHEMA.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Chat summary and text report; optional JSON, SARIF, HTML, or PDF reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A–F grade requires all five check layers; otherwise reports missing layers and prioritized findings.]

## Skill Version(s):

4.4.1 (source: ClawHub release, skill frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
