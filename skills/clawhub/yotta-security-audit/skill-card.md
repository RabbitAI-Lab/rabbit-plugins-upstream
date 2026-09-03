## Description:

元安 yotta-security-audit audits AI skill directories for malicious patterns and checks Windows/Linux system security baselines while reporting findings without making changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent users use this skill to scan new or installed agent skills for supply-chain risks and to run authorized read-only system baseline checks before deployment or during review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer writes the skill into chosen agent skill folders and broad install options can affect multiple agent directories.

Mitigation: Install only from a trusted source, choose the target directory deliberately, and avoid broad installation unless it is intended.

Risk: System baseline mode may inspect sensitive local security files and settings.

Mitigation: Run system baseline checks only on systems you are authorized to audit and review the redacted findings before taking any action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-audit)
- [Threat patterns](references/threat-patterns.md)
- [System baseline checks](references/system-baseline.md)
- [Remediation guide](references/remediation-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text reports, optional JSON, and optional Markdown reports with shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are masked by default; high-risk findings require user review before remediation.]

## Skill Version(s):

0.2.3 (source: server release metadata; artifact frontmatter and package.json show 0.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
