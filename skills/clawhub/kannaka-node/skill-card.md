## Description:

Hand a fresh Linux server to an AI and get back a running Kannaka node with installation, configuration, systemd service setup, verification, and hand-off reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickflach](https://clawhub.ai/user/nickflach)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to provision a Linux VPS as a Kannaka node from SSH access, including preflight checks, binary installation, node identity configuration, optional credentials, service setup, verification, and an operator report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provisioning a long-running server node can introduce unsafe remote execution or persistent service changes if run without review.

Mitigation: Review or fix the provisioning script before use, require explicit approval before running the remote installer or sudo service step, and verify the installer, binary digest, systemd units, and timer before enabling persistence.

Risk: Untrusted environment values or configuration fields can create injection exposure during installation or service configuration.

Mitigation: Do not allow untrusted values for INSTALL_URL, BRAIN_EMAIL, NATS_USER, NATS_PASSWORD, display name, or config fields; use a dedicated, non-sensitive VPS and service user.

## Reference(s):

- [Oracle Cloud Free Tier](references/oracle-cloud.md)
- [Things That Have Actually Gone Wrong on Real Kannaka Nodes](references/traps.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational hand-off text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include preflight, verification, update, and uninstall instructions for the target host.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
