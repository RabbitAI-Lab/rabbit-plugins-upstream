## Description:

Generate diagrams from descriptions with Mermaid, PlantUML, or ASCII for architecture, flows, sequences, and data models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers, architects, and technical writers use this skill to turn system, workflow, architecture, sequence, and data model descriptions into concise diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering diagrams to images can involve running an unpinned third-party Mermaid CLI package fetched from the npm registry.

Mitigation: Review and pin the renderer dependency, install it through a lockfile, and run rendering with limited filesystem and environment access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/diagram)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Mermaid, PlantUML, ASCII, SVG, HTML, or shell command snippets when appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce renderable diagram source or instructions for creating PNG/SVG image files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
