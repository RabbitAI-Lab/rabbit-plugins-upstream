## Description:

Scans Linux servers for common vulnerabilities, monitors logs for attack indicators, applies selected hardening or defenses, and generates security reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cmccadmin12](https://clawhub.ai/user/cmccadmin12)

### License/Terms of Use:

MIT-0

## Use Case:

System administrators and developers use this skill to assess and respond to security issues on Linux servers they are authorized to manage. It supports read-only vulnerability scans and log monitoring, reviewed remediation or defenses, and HTML reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privileged repairs may affect unrelated files.

Mitigation: Prefer ordinary-user scans, then verify the exact server and files affected before approving changes.

Risk: Recovery safeguards may be incomplete during hardening or remediation.

Mitigation: Keep an independent recovery login and retain backups before approving changes.

Risk: Rollback JSON can execute commands.

Mitigation: Inspect rollback data and accept it only from trusted sources.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/cmccadmin12/skills/srv-guard)
- [Vulnerability scan checklist](references/scan-checklist.md)
- [Remediation playbook](references/fix-playbook.md)
- [Attack detection signatures](references/attack-signatures.md)
- [Defense strategies](references/defense-strategies.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, HTML report, Shell commands]

**Output Format:** [JSON scan, remediation, monitoring, and defense results; HTML security report; concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets local or SSH-accessible Linux servers; scanning and monitoring are read-only, while remediation and defense default to dry-run.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
