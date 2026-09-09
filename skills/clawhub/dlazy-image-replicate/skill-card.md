## Description:

Analyzes a source image's visuals, composition, colors, lighting, and style, then uses the dLazy image-replicate workflow to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create style-similar images from reference images through the dLazy CLI. It is suited for agent workflows that need image replication guidance, command invocation, and generated image result handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party CLI and hosted dLazy service.

Mitigation: Review the linked dLazy CLI source and npm package before use, and prefer npx or a least-privilege environment if a persistent global binary is not desired.

Risk: The workflow requires a dLazy API key for authenticated requests.

Mitigation: Store credentials only in the expected dLazy CLI configuration or per-invocation environment variable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Reference media supplied as local paths may be uploaded to dLazy-hosted storage for processing.

Mitigation: Only provide media files that are acceptable to send to dLazy's hosted service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return image output URLs or async task identifiers from dLazy; local save paths are supported by the CLI.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
