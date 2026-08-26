## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or transform images through the dLazy Seedream 4.5 CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and user-supplied media paths may be sent to dLazy cloud endpoints for generation.

Mitigation: Confirm the user intends to use the hosted dLazy service before sending sensitive prompts or local files.

Risk: Saved API keys can persist in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for temporary authentication when a persistent saved key is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: Image generation can consume paid API credits.

Mitigation: Use dry-run or explicit user confirmation when cost sensitivity matters before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated image URLs; optional saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may send prompts, parameters, and user-supplied media paths to dLazy cloud endpoints.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
