## Description:

Guides agents through discovering, installing, wiring, and authoring HyperFrames registry blocks and components.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill to find HyperFrames registry items, install blocks or components, wire them into compositions, and author new registry items for upstream contribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HyperFrames add commands can modify the current project and fetch registry assets from the configured remote registry.

Mitigation: Use explicit item names, prefer --json for agent workflows, and review project diffs after installation.

Risk: Interactive or network actions such as --human-friendly, feedback, publish, PR, or auth commands may do more than deterministic catalog discovery.

Mitigation: Avoid those commands unless the user deliberately requests the interactive or network behavior.

## Reference(s):

- [HyperFrames Registry skill page](https://clawhub.ai/heygen-com/skills/hyperframes-registry)
- [Registry discovery](references/discovery.md)
- [Install locations](references/install-locations.md)
- [Wiring blocks](references/wiring-blocks.md)
- [Wiring components](references/wiring-components.md)
- [Contributing a block or component](references/contributing.md)
- [HyperFrames registry manifest](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json)
- [HyperFrames configuration schema](https://hyperframes.heygen.com/schema/hyperframes.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with command, JSON, HTML, CSS, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project file edits and network-backed HyperFrames CLI commands.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
