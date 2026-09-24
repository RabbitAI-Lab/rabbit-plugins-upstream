## Description:

Searches, installs, and wires HyperFrames registry blocks and components into compositions, and guides contribution of new registry items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill to discover HyperFrames registry items, install blocks or components, wire them into composition HTML, and scaffold new registry contributions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides agents to install registry items and edit composition files, which can change project behavior or generated visuals.

Mitigation: Review generated file changes, run HyperFrames lint or preview checks, and inspect compositions before publishing.

Risk: Bare npx or networked CLI use can execute unpinned tooling or fetch registry files at install time.

Mitigation: Prefer pinned or project-local hyperframes, tsx, and oxfmt dependencies from trusted sources.

Risk: Search-miss feedback sends the described query and wanted effect when that explicit feedback command is run.

Mitigation: Avoid submitting sensitive project details in feedback text and use scoped credentials for GitHub, AWS, or hyperframes.dev workflows.

## Reference(s):

- [HyperFrames registry manifest](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json)
- [HyperFrames registry base URL](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry)
- [HyperFrames configuration schema](https://hyperframes.heygen.com/schema/hyperframes.json)
- [Registry discovery](artifact/references/discovery.md)
- [Install locations](artifact/references/install-locations.md)
- [Wiring blocks](artifact/references/wiring-blocks.md)
- [Wiring components](artifact/references/wiring-components.md)
- [Contributing a block or component](artifact/references/contributing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell, JSON, HTML, CSS, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to HyperFrames composition files and registry item files.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
