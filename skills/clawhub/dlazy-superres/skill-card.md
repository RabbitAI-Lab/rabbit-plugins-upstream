## Description:

Image super-resolution tool: enhances image clarity and details, returning enhanced URL, suitable for low-res asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to upscale low-resolution images through the dLazy hosted super-resolution service and receive enhanced image URLs or saved image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs and prompts may be sent to dLazy's hosted API and media storage.

Mitigation: Use only images appropriate for third-party cloud processing and review dLazy service terms before sending sensitive content.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration.

Mitigation: Use a revocable dLazy API key, rotate or revoke it when needed, and consider per-invocation use of DLAZY_API_KEY for tighter credential handling.

Risk: Installing the dLazy CLI globally adds a persistent npm-managed binary to the environment.

Mitigation: Prefer the pinned npx invocation when a persistent global install is not needed, and review the package or source before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses containing generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an async task identifier when --no-wait is used; --save can download the generated image to a local path.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
