## Description:

Scans Linux servers for common configuration vulnerabilities, reviews logs for suspicious activity, and prepares security reports and guarded remediation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cmccadmin12](https://clawhub.ai/user/cmccadmin12)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and server administrators use the skill to assess authorized Linux hosts, review security events, and plan or perform carefully confirmed hardening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repair and rollback routines may damage files or weaken security settings.

Mitigation: Review scan and dry-run previews, verify each selected file, correct symbolic-link handling, and restore recorded original kernel values before applying changes.

Risk: An exposed local web interface or untrusted rollback file could enable unintended changes.

Mitigation: Keep the web UI bound to localhost and use only trusted rollback files.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/cmccadmin12/skills/srv-guard)
- [Scan checklist](references/scan-checklist.md)
- [Fix playbook](references/fix-playbook.md)
- [Attack signatures](references/attack-signatures.md)
- [Defense strategies](references/defense-strategies.md)
- [HTML report template](assets/report-template.html)

## Skill Output:

**Output Type(s):** [JSON security findings and action results, HTML security report, Remediation guidance]

**Output Format:** [JSON result files and an HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanning and monitoring are read-only; repair and defense default to dry-run and require explicit confirmation to apply changes. Some checklist items require manual review and are not implemented in the scripts.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
