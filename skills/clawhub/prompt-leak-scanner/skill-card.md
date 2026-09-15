## Description:

Scans prompts and system prompts before sharing for secrets, internal paths, PII, custom sensitive terms, and self-leak prompt backdoors, blocking high-risk findings with a non-zero exit code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill as a local pre-publication gate to check prompts and system prompts for likely secrets, private infrastructure details, PII, sensitive keywords, and prompt-leak instructions before sharing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer instructions include a global npx path that may be risky if the installer or source is not trusted.

Mitigation: Install only from a pinned, reviewed commit or verified release, and avoid global installation unless the installer is trusted.

Risk: Scanner output can include snippets of the sensitive material it detects.

Mitigation: Treat scan results as sensitive and avoid sharing logs or JSON output outside the review boundary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-leak-scanner)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON CLI findings with process exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes indicate pass, blocked high-risk findings, or usage/environment errors.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.json; artifact SKILL.md frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
