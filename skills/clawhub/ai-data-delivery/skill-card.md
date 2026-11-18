## Description:

CLI-first tool for importing SQL or selected database metadata, editing a source-linked semantic graph, and exporting or reading it locally with an Agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data teams, and Agent builders can turn database structure and approved source material into an editable semantic model, then export a scoped package for another local Agent to read. It supports local modeling and review, not production query execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan reports concerns about database profiling beyond a selected-metadata scope.

Mitigation: Connect only to databases you are authorized to inspect, explicitly select the intended schemas and tables, and verify the host's access and retention settings.

Risk: The scan raises concerns about stored data and starter-pack confirmation labels.

Mitigation: Limit imports and package exports to intended sources, review source excerpts and business meaning, and confirm definitions only after review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/franklinxkk/skills/ai-data-delivery)
- [Security boundaries and capabilities](artifact/SECURITY.md)
- [Architecture](artifact/references/architecture.md)
- [Semantic package and local reader](artifact/references/semantic-package.md)
- [Read-only metadata connections](artifact/references/readonly-metadata.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON, Semantic model files and packages]

**Output Format:** [Markdown guidance, CLI commands, JSON responses, and local semantic model or ZIP package files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Packages may include business definitions and selected source excerpts; business meaning requires review. The skill does not provide a production query executor.]

## Skill Version(s):

0.3.6 (source: server-resolved release, SKILL.md frontmatter, CHANGELOG.md; released 2026-11-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
