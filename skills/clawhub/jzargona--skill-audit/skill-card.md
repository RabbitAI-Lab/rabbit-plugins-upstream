## Description:

Audit locally installed agent skills for security and policy issues using the SkillLens CLI (`skilllens scan`, `skilllens config`).

This skill is ready for commercial/non-commercial use.

## Publisher:

[jzargona](https://clawhub.ai/user/jzargona)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit locally installed Codex or Claude agent skills for security and policy risks. It supports CLI-based SkillLens scans and a manual fallback workflow that produces risk-focused findings and fix recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends running an unpinned external SkillLens CLI, which can read local skill files during an audit.

Mitigation: Verify the SkillLens package source, prefer a pinned version or lockfile-backed local install, avoid global install unless needed, run scans as an unprivileged user, and scan a specific target directory.

## Reference(s):

- [Skill Audit ClawHub page](https://clawhub.ai/jzargona/skills/skill-audit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown audit report with command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-skill verdicts, risk scores, evidence quotes, and fix recommendations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
