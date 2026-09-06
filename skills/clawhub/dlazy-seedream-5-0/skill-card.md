## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images. Suited to key visuals, posters and anything meant for large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-resolution images from prompts and up to 10 reference images through the dLazy hosted Seedream 5.0 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to a third-party hosted service.

Mitigation: Use the skill only with content suitable for dLazy processing, and avoid sending confidential or regulated files unless approved for that service.

Risk: The skill encourages persisting a dLazy API key in the local CLI configuration.

Mitigation: Prefer the DLAZY_API_KEY environment variable for per-run use, or verify permissions on ~/.dlazy/config.json and rotate or revoke the key when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON result examples; generated image outputs are returned as hosted URLs or saved files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous generation, asynchronous task IDs, dry-run cost estimates, selectable resolution and aspect ratio, and optional local save paths.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
