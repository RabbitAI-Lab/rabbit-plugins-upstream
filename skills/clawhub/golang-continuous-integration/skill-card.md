## Description:

CI/CD pipeline configuration using GitHub Actions for Go projects covering testing, linting, SAST, security scanning, coverage, dependency automation, code review automation, and release pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to set up or improve Go project CI/CD on GitHub Actions, including tests, linting, security checks, dependency automation, releases, and AI-assisted code review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The AI review workflow has broad automatic PR-commenting and workflow log-reading authority.

Mitigation: Review before installing on important repositories; scope AI review triggers to trusted contributors, protected branches, labels, or manual dispatch, and move permissions to the jobs that require them.

Risk: The AI review workflow includes id-token write access and remote skill installation behavior that may be broader than needed.

Mitigation: Remove id-token write access unless required, and pin or narrow the remote skill installation before enabling the workflow.

Risk: Auto-merge, release, and Docker publishing templates can modify repository content or publish artifacts when enabled.

Mitigation: Keep branch protection, required status checks, and required approvals enabled before using these templates.

Risk: Copilot review instructions include a hidden setup comment intended for installation.

Mitigation: Remove the hidden setup comment before copying the instructions into a repository.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-continuous-integration)
- [Project Homepage](https://github.com/samber/cc-skills-golang)
- [Repository Security Settings](references/repo-security.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with GitHub Actions YAML, JSON configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify GitHub Actions workflows and related CI/CD configuration for Go repositories.]

## Skill Version(s):

1.4.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
