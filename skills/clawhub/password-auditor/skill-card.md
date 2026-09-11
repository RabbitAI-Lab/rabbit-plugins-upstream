## Description:

Audits password vault exports from Bitwarden, 1Password, KeePass, Chrome, and Firefox for reuse, weakness, staleness, breach exposure, and 2FA gaps without storing or transmitting plaintext passwords.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to audit local password-manager exports, identify weak, reused, stale, breached, or 2FA-eligible credentials, and prioritize remediation without exposing plaintext passwords in reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTML reports can execute crafted content from vault entry titles.

Mitigation: Review the skill before installation, avoid opening HTML reports from untrusted or shared vault exports, and prefer terminal or JSON output until dynamic HTML fields are escaped.

Risk: Password-manager exports are plaintext and highly sensitive.

Mitigation: Run the skill only on an explicit local export, keep the export out of synced or shared folders, and delete the export after the audit.

Risk: Optional breach checks send SHA-1 password hash prefixes to HaveIBeenPwned.

Mitigation: Leave breach checks disabled unless the user accepts this network disclosure and wants breach exposure results.

Risk: Generated reports include account titles and findings.

Mitigation: Store JSON and HTML reports carefully and avoid sharing them outside the intended remediation workflow.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/voronindenis5/password-auditor)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/password-auditor)
- [Risk Model & Scoring Methodology](references/risk-model.md)
- [Supported Vault Export Formats](references/export-formats.md)
- [HaveIBeenPwned k-anonymity range API](https://api.pwnedpasswords.com/range/XXXXX)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell command examples; optional terminal text, JSON reports, and self-contained HTML dashboards.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis; optional breach checks send SHA-1 hash prefixes to HaveIBeenPwned; generated reports include account titles and findings but no plaintext passwords.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
