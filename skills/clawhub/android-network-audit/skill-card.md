## Description:

Audits Android/Termux network exposure by checking connectivity, interfaces, DNS, proxies, listening ports, and exposure risk without modifying the device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to audit local Android or Termux network exposure before running services, debugging connectivity, or checking DNS, proxy, interface, and listening-port posture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit reports can expose local IP addresses, DNS settings, proxy presence, and listening port or process details.

Mitigation: Keep reports private, redact sensitive environment details, and share only the minimum findings needed for review or remediation.

Risk: Network auditing can be misused on devices or networks where the user lacks authorization.

Mitigation: Use the skill only for local Android or Termux environments the user is authorized to inspect, and do not use it for unauthorized penetration testing.

Risk: Changing network or proxy settings based on findings could disrupt connectivity or weaken security.

Mitigation: Treat findings as read-only guidance unless the user explicitly requests a remediation action and understands the change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/android-network-audit)
- [Skill instructions](artifact/SKILL.md)
- [Audit script](artifact/scripts/audit_net.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown audit report with optional JSON output from the bundled shell script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local audit output; keep full reports private because they may contain local IPs, DNS settings, proxy presence, and listening port or process details.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
