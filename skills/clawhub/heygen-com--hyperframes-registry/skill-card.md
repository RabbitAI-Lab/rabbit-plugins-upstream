## Description:

Helps agents find, install, and integrate reusable HyperFrames blocks and components into video compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to search the HyperFrames registry, add ready-made visual effects or compositions to a project, and wire them into HTML timelines. It also guides contributors creating new registry items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested commands may run npm packages or fetch registry files.

Mitigation: Prefer a project-pinned or locally installed HyperFrames CLI, and review downloaded files before publishing.

Risk: Reporting a search miss sends the query and requested item to a network service.

Mitigation: Run the feedback command only when you intend to submit that report.

## Reference(s):

- [HyperFrames Registry on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-registry)
- [Registry discovery guide](artifact/references/discovery.md)
- [Installing and wiring blocks](artifact/references/wiring-blocks.md)
- [Installing and wiring components](artifact/references/wiring-components.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with command, HTML, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can install registry files into a project.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
