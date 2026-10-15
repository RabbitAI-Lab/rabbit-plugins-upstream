## Description:

Helps agents discover, install, and integrate reusable HyperFrames registry blocks and components into video compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to find suitable visual effects, install registry items, wire blocks and components into HyperFrames compositions, and prepare new items for contribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned CLI commands can run changing external tooling.

Mitigation: Use a locally installed or version-pinned HyperFrames CLI rather than floating npx commands.

Risk: Installing registry items downloads files into a project.

Mitigation: Review fetched registry item files before merging them into a composition.

Risk: Feedback can send search details, and interactive selection can trigger installation.

Mitigation: Run feedback or interactive install commands only when you intend to send or install that data; prefer JSON catalog results and explicit installs in automation.

## Reference(s):

- [HyperFrames Registry on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-registry)
- [Registry discovery](artifact/references/discovery.md)
- [Install locations](artifact/references/install-locations.md)
- [Wiring blocks](artifact/references/wiring-blocks.md)
- [Wiring components](artifact/references/wiring-components.md)
- [Contributing registry items](artifact/references/contributing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command, HTML, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include registry item selection and composition wiring instructions.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
