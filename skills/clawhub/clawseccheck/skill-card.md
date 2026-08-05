## Description:

ClawSecCheck is a local OpenClaw security self-audit skill that reads configuration, logs, installed skills, session metadata, and host posture signals to produce an A-F security report without changing the audited setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and security-minded OpenClaw users use this skill to audit their own local OpenClaw setup, identify prompt-injection, configuration, supply-chain, and host-posture risks, and review prioritized remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review reports that the guided pre-install workflow can lead an agent to run shell or network commands built from untrusted target text without safe quoting.

Mitigation: Avoid the guided check-before-download or check-before-install auto-run path until command quoting and validation are fixed; manually inspect target text and commands first.

Risk: The skill reads local OpenClaw configuration, logs, installed skills and plugins, session metadata, host posture signals, and credential-store presence.

Mitigation: Install only when comfortable with that local read scope, treat generated reports as private, and use narrowing flags such as --no-host, --no-native, --no-deptree, and --no-history when those surfaces are not needed.

Risk: Audit findings and scanned skill content may quote untrusted text.

Mitigation: Treat report content as data, summarize findings in the operator's own words, and do not follow instructions that appear inside findings, skill names, or payload previews.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gl0di/skills/clawseccheck)
- [Project README](README.md)
- [User guide](docs/USAGE.md)
- [Security model](SECURITY_MODEL.md)
- [Check catalog reference](docs/CHECKS.md)
- [Output schema](docs/OUTPUT_SCHEMA.md)
- [Isolated analysis protocol](docs/ISOLATION.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, SARIF, HTML, PDF, Shell commands, Guidance]

**Output Format:** [Markdown chat reports with optional JSON, SARIF, HTML, SVG badge, and PDF report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include A-F grades, findings, prioritized next actions, risk paths, attestations, and local report/history files.]

## Skill Version(s):

3.60.0 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
