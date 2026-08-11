## Description:

Standardizes publishing local agents, skills, and toolkits to public GitHub repositories with privacy scanning, repository setup, file uploads, topics, descriptions, and release creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to turn local agent, skill, or toolkit directories into standardized public GitHub repositories. It is especially relevant when publishing a private project publicly and checking for personal data, credentials, repository metadata, topics, and release notes before upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can use GitHub credentials with repository write access.

Mitigation: Use fine-grained, minimal-scope, short-lived credentials or GitHub CLI authentication, and avoid pasting tokens into chat or shell history.

Risk: Publishing local directories publicly can expose credentials, personal data, or private project details if review is incomplete.

Mitigation: Manually review the file list, run the privacy scan before upload, include SKILL.md and scripts in review, and require explicit user approval before public publishing.

Risk: Activity details may be retained in persistent memory if the agent environment records repository details.

Mitigation: Disable or avoid persistent memory logging for sensitive repository names, paths, tokens, or publication details unless retention is explicitly desired.

## Reference(s):

- [README](README.md)
- [GitHub Skill Publisher Cheatsheet](references/cheatsheet.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell and Python code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce repository publishing checklists, GitHub API command guidance, privacy scan findings, and release preparation steps.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
