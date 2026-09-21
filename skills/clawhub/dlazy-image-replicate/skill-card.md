## Description:

Image replicate tool: analyzes the visuals, composition, colors, lighting, and style of the source image, builds a replicate prompt, and hands it off to Seedream 4.5 to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to invoke dLazy's image-replicate workflow for producing a new image in the style and composition of a supplied reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths supplied to the CLI may be uploaded to dLazy-hosted services for processing.

Mitigation: Avoid submitting sensitive prompts or media unless the user's policy allows third-party cloud processing.

Risk: Authentication can save a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation environment variables or rotate and revoke keys from dLazy when access changes.

Risk: A persistent global npm install adds and updates a third-party CLI on the host.

Mitigation: Use the pinned npx invocation when a persistent global installation is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, image]

**Output Format:** [CLI commands and JSON responses containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, optional local saving, and remotely hosted generated outputs.]

## Skill Version(s):

1.3.19 (source: server evidence release; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
