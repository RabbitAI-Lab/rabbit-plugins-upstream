## Description:

Install and wire registry blocks and components into HyperFrames compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lucas-kay8](https://clawhub.ai/user/lucas-kay8)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install HyperFrames registry blocks or components, wire them into existing compositions, configure install locations, and discover registry items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be applied to unrelated block or component requests outside a HyperFrames project.

Mitigation: Confirm the workspace is a HyperFrames project and that the request concerns HyperFrames registry items before applying the workflow.

Risk: External registry snippets may add HTML, CSS, or JavaScript to a composition.

Mitigation: Review installed snippets before merging them into project files and run HyperFrames lint or preview checks after wiring.

## Reference(s):

- [Install Locations](references/install-locations.md)
- [Wiring Blocks](references/wiring-blocks.md)
- [Wiring Components](references/wiring-components.md)
- [Registry Discovery](references/discovery.md)
- [Demo HTML Convention](references/demo-html-pattern.md)
- [HyperFrames Registry](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry)
- [HyperFrames Registry Manifest](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json)
- [HyperFrames Configuration Schema](https://hyperframes.heygen.com/schema/hyperframes.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash, HTML, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local HyperFrames project edits and registry snippet integration steps.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
