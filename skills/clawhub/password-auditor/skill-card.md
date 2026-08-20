## Description:

Audits password vault exports from major password managers for reuse, weakness, staleness, breach exposure, and 2FA gaps without storing or transmitting plaintext passwords.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and security-conscious users use this skill to audit password-manager exports, identify weak or reused credentials, check optional breach exposure, and produce a prioritized remediation plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plaintext vault exports can expose credentials if they are left in synced or shared folders after an audit.

Mitigation: Use only vault exports intentionally provided for the audit, keep exports and generated reports out of synced/shared folders, and delete the plaintext export after auditing.

Risk: Optional breach checking may conflict with policies that forbid sending password-derived hash prefixes to an external service.

Mitigation: Run the skill without --check-breaches when policy forbids external breach checks.

## Reference(s):

- [Risk Model & Scoring Methodology](references/risk-model.md)
- [Supported Vault Export Formats](references/export-formats.md)
- [Password Auditor on ClawHub](https://clawhub.ai/voronindenis5/skills/password-auditor)
- [Publisher Profile](https://clawhub.ai/user/voronindenis5)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML files, shell commands, guidance]

**Output Format:** [Markdown guidance with bash commands; generated audit reports may be terminal text, JSON, or self-contained HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis of user-provided vault exports; optional breach checking sends only password-derived hash prefixes.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
