## Description:

Use when generating or updating a project README.md or CHANGELOG.md.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate or refresh README and CHANGELOG documentation from repository evidence, including project structure, stack, git history, and existing documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent git commits and include unrelated generated-by attribution.

Mitigation: Before use, instruct the agent not to commit automatically and remove generated-by or third-party attribution unless repository policy explicitly permits it.

Risk: The skill can create extra bilingual documentation files beyond a simple README or CHANGELOG update.

Mitigation: Review the planned file list before generation and constrain output paths to the documentation files the repository actually needs.

Risk: Generated documentation can be incorrect if repository evidence is incomplete or stale.

Mitigation: Require a discovery summary and review generated claims against source files, configuration, and git history before accepting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-readme)
- [Source repository](https://github.com/afonsoft/skills)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Shields.io](https://shields.io/)
- [Make a README](https://www.makeareadme.com/)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown files and concise status summaries with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update README.md, README.pt-br.md, CHANGELOG.md, docs/en/, docs/pt/, and a git branch or commit when following the skill workflow.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; SKILL.md frontmatter lists 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
