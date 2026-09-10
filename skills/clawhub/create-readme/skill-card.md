## Description:

Use when generating or updating professional README.md and CHANGELOG.md files for a project. Covers repository analysis, stack detection, badge generation, structure diagrams, and alignment with Keep a Changelog and SemVer standards. Do NOT use for API-reference docs (use dedicated doc tooling), licenses/governance documents, or internal code documentation (use docstrings/JSDoc). Part of the afonsoft/skills collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to analyze a repository and produce evidence-based README.md, README.pt-br.md, CHANGELOG.md, and auxiliary documentation when repository documentation is missing, outdated, or inconsistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broader-than-expected repository changes while creating bilingual README, CHANGELOG, and auxiliary documentation files.

Mitigation: Require review of planned file additions and edits before allowing writes.

Risk: The skill may propose git branch or commit operations, including a hardcoded third-party attribution in the commit message.

Mitigation: Decline automatic git execution unless explicitly desired, and remove hardcoded attribution from any commit message before committing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-readme)
- [Skill metadata URL](https://github.com/afonsoft/skills)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Shields.io](https://shields.io/)
- [Make a README](https://www.makeareadme.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, tables, diagrams, and bilingual documentation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose repository file creation or updates; review planned writes and git operations before execution.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter metadata.version is 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
