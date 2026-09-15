## Description:

Use when generating or updating a project README.md or CHANGELOG.md.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to generate or update evidence-based README and CHANGELOG documentation for software repositories. It is intended for projects with missing, stale, or incomplete documentation before releases, restructuring, or contributor onboarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may direct an agent to create branches and commits automatically.

Mitigation: Review proposed git operations before execution and require human approval for branch creation or commits in protected repositories.

Risk: The skill includes hardcoded third-party attribution in commit message guidance.

Mitigation: Confirm generated commit messages match the user's project policy and remove unrelated attribution before committing.

Risk: The skill can force an English and Portuguese documentation layout even when it does not match an existing project convention.

Mitigation: Check the repository's language and documentation conventions before accepting generated README, README.pt-br, docs/en, or docs/pt changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-readme)
- [Publisher metadata URL](https://github.com/afonsoft/skills)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown files, discovery summaries, changelog entries, shell commands, and concise implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be grounded in repository evidence and may include proposed file edits, branch commands, commit commands, bilingual documentation, and Mermaid diagrams when supported by evidence.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
