## Description:

Use when generating or updating professional README.md and CHANGELOG.md files for a project, including repository analysis, stack detection, badge generation, structure diagrams, and alignment with Keep a Changelog and SemVer standards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate or refresh evidence-based README.md, README.pt-br.md, auxiliary docs, and CHANGELOG.md files for a repository before onboarding contributors or shipping a release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to make repository changes and a commit, and its sample commit message contains unrelated third-party attribution.

Mitigation: Review repository diffs before committing, remove or edit the fixed attribution, and require explicit approval before branch or commit actions.

Risk: Generated documentation can be misleading if repository claims are not traceable to files, commits, or configuration.

Mitigation: Keep the skill's discovery summary and evidence checks in the review path, and reject documentation sections that lack concrete source evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-readme)
- [Publisher source URL](https://github.com/afonsoft/skills)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Shields.io](https://shields.io/)
- [Make a README](https://www.makeareadme.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, Mermaid diagrams, and bilingual documentation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be based on repository evidence and may include README.md, README.pt-br.md, docs/en, docs/pt, and CHANGELOG.md content.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter metadata.version is 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
