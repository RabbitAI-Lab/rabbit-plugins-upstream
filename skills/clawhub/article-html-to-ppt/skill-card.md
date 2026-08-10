## Description:

Build and QA editable PPT decks locally; probes required tools/fonts, runs subprocess renderers in isolated work/output folders, and uses cloud export only with explicit consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillmelody](https://clawhub.ai/user/skillmelody)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation builders, product teams, and knowledge creators use this skill to turn articles, Markdown, HTML, PRDs, project materials, and approved manuscripts into editable PowerPoint decks with local build, verification, and delivery reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local verification and packaging commands may delete user-specified work, output, or render folders if aimed at an important existing directory.

Mitigation: Use dedicated empty .ppt-work and final output directories, and never point output or render flags at a workspace root or unrelated folder.

Risk: The skill runs local Python, Node, and office-renderer subprocesses as part of deck production and QA.

Mitigation: Install and run it only in an environment where those local tools are acceptable, and review generated commands before execution.

Risk: Cloud export can transmit source content, generated slide text, and metadata to Feishu or Lark services.

Mitigation: Keep local PPTX export as the default for sensitive material and use cloud export only after reviewing the privacy summary and confirming the destination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt)
- [README.en.md](README.en.md)
- [v3.0.1 release notes](docs/v3.0.1-release-notes.md)
- [Export pipelines](references/export-pipelines.md)
- [Production readiness gates](references/production-readiness-gates.md)
- [Verification harness](references/verification-harness.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON contracts, shell commands, and generated deck artifacts such as PPTX files and verification reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local PPTX generation is the safer default; cloud export is off by default and requires explicit user intent.]

## Skill Version(s):

3.0.1 (source: SKILL.md frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
