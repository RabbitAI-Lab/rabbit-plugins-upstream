## Description:

Use when auditing Android/Termux network exposure, connectivity, proxies, listeners, and unsafe ports from the device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and Android/Termux users use this skill to perform read-only local network audits, inspect connectivity, DNS, proxy settings, interfaces, and listening ports, and classify exposure risk before running services or sharing a network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain IP addresses, interface names, DNS settings, proxy hosts, and listening port details.

Mitigation: Review and redact reports before sharing them outside the intended private context.

Risk: The audit is intended for local Android/Termux network exposure inspection and should not be used on devices or networks without authorization.

Mitigation: Keep use limited to owned or explicitly authorized devices and preserve the skill's read-only posture unless the user separately requests remediation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/android-network-audit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown network audit report with shell command snippets and optional JSON summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include local network details such as IP addresses, interface names, DNS settings, proxy hosts, and listening ports; credentials should be masked.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
