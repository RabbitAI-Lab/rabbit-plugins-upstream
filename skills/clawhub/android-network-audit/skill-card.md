## Description:

Use when auditing Android/Termux network exposure, connectivity, proxies, listeners, and unsafe ports from the device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to run read-only Android or Termux network audits, check connectivity, DNS, proxy settings, interfaces, and listening ports, and summarize local exposure risk before running or deploying services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network audit reports can reveal local device details such as IP addresses, DNS settings, proxy presence, and listening ports.

Mitigation: Keep reports private, redact sensitive details before sharing, and review any remediation suggestion before allowing configuration changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/android-network-audit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with inline shell commands and optional JSON audit output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local audit output that masks proxy credentials and classifies exposure risk.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
