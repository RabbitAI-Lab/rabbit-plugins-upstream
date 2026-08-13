## Description:

Install, discover, and wire registry blocks and components into HyperFrames compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill to find, install, configure, and wire HyperFrames registry blocks and components into compositions. It also guides contributors through creating and validating new registry items before upstream review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contribution workflows can involve publishing preview media or catalog images to external project infrastructure.

Mitigation: Confirm the media is approved for upload and publish only through authorized accounts and approved project channels.

Risk: The contribution workflow may include an AWS upload step.

Mitigation: Run that step only as an authorized internal contributor using the correct least-privilege profile.

## Reference(s):

- [HyperFrames registry source](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry)
- [HyperFrames registry manifest](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json)
- [HyperFrames project schema](https://hyperframes.heygen.com/schema/hyperframes.json)
- [Install Locations](references/install-locations.md)
- [Wiring Blocks](references/wiring-blocks.md)
- [Wiring Components](references/wiring-components.md)
- [Registry discovery](references/discovery.md)
- [Contributing a Block or Component to the Registry](references/contributing.md)
- [Contribute Templates](references/templates.md)
- [Component quality bar](references/component-quality-bar.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash, HTML, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are user-facing instructions and snippets for HyperFrames CLI, registry configuration, composition wiring, and contribution workflows.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
