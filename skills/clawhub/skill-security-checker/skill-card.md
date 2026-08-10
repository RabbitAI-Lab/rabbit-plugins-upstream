## Description:

Skill Security Checker scans agent skill directories for static security issues, dependency and supply-chain risks, permission exposure, known malicious fingerprints, optional sandbox behavior, and CI/CD readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill before release or in CI/CD to scan skill directories for security findings, dependency and supply-chain risks, permission exposure, known malicious fingerprints, and optional sandbox behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ClawHub security review marked the skill suspicious because broad triggers, default network behavior, and persistent cache behavior are not tightly scoped or fully disclosed.

Mitigation: Use explicit command-line invocation, scan only intended paths, and use --skip-update when offline or when default network contact is not acceptable.

Risk: Supply-chain scanning may disclose dependency names to public vulnerability or package services.

Mitigation: Avoid --supply-chain for sensitive dependency sets unless the execution environment is approved for those external lookups.

Risk: The scanner reads target paths and may create cache files under the user's home directory.

Mitigation: Run it against a limited target directory and review local cache locations before and after use.

## Reference(s):

- [Scan Patterns Reference](references/scan-patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/skill-security-checker)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Text, JSON, HTML, SARIF, Markdown guidance, and CI configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write report files when an output path is provided; optional dynamic scanning requires Docker or Windows Sandbox.]

## Skill Version(s):

3.1.0 (source: SKILL.md frontmatter, ClawHub release evidence, artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
