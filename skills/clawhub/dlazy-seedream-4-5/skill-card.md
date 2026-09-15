## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creators use this skill to generate or transform images through the dLazy CLI using Doubao Seedream 4.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be uploaded to dLazy for image generation.

Mitigation: Avoid sensitive prompts or media unless the user is comfortable sending them to dLazy.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use scoped credentials where available, rotate or revoke keys when needed, and prefer per-invocation environment variables for temporary use.

Risk: A global CLI installation persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation or a sandboxed environment when a persistent global install is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return hosted generated-image URLs or save generated image files to a local path.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
