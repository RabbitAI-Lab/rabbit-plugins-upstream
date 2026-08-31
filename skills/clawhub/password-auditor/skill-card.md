## Description:

Audit password vault exports (Bitwarden, 1Password, KeePass, Chrome, Firefox) for reuse, weakness, staleness, breach exposure, and 2FA gaps without ever storing or transmitting a plaintext password.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to audit local password manager exports, identify weak, reused, stale, breached, or 2FA-missing credentials, and prioritize remediation without placing plaintext passwords in generated reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires users to export a password vault, and vault exports may contain plaintext credentials before analysis.

Mitigation: Run the audit locally, keep the export out of synced or shared folders, and securely delete the plaintext export after use.

Risk: Optional breach checks contact an external service.

Mitigation: Run offline unless breach checking is intentionally enabled; when enabled, only password hash prefixes are sent for k-anonymity matching.

Risk: Generated JSON and HTML reports can contain sensitive account titles, usernames, metadata, and findings even without plaintext passwords.

Mitigation: Protect report files as sensitive security artifacts and delete or store them securely after review.

## Reference(s):

- [Risk Model & Scoring Methodology](references/risk-model.md)
- [Supported Vault Export Formats](references/export-formats.md)
- [Server-resolved source repository](https://github.com/voronindenis5/password-auditor)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/password-auditor)
- [Have I Been Pwned password range API](https://api.pwnedpasswords.com/range/XXXXX)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, HTML]

**Output Format:** [Markdown guidance with inline shell commands; generated audit reports may be terminal text, JSON, or self-contained HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are intended to omit plaintext passwords; breach checks are optional and use only SHA-1 hash prefixes.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
