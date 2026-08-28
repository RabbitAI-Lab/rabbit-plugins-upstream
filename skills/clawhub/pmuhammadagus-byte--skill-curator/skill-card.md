## Description:

Skill Curator audits OpenClaw skill folders for packaging metadata, guardrails, changelog coverage, broad authority language, token or secret patterns, hidden Unicode, raw execution or network patterns, duplicate slugs, namespace concerns, and remediation proposals without auto-editing files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to audit OpenClaw skills before publishing or during periodic maintenance. It produces quality scores, severity findings, and proposed remediation while preserving read-only behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans local skill files and may cover more directories than intended if run with the default skills path.

Mitigation: Run it with an explicit --skills directory when scope matters.

Risk: The built-in token allowlist suppresses known legitimate token-like strings, so allowlisted strings will not be reported as leaks.

Mitigation: Review the allowlist before relying on leak findings for a release audit.

Risk: Remediation proposals could be incorrect or misleading if applied without review.

Mitigation: Treat results as audit guidance and review proposed changes before editing or publishing skills.

## Reference(s):

- [Audit Criteria](references/audit-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-curator)
- [Publisher Profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown audit table and summary, or JSON when the script is run with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports quality scores, CRITICAL/HIGH/MEDIUM/LOW/INFO findings, and remediation proposals; scans local skill files and does not auto-edit.]

## Skill Version(s):

1.1.1 (source: server release metadata, artifact metadata, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
