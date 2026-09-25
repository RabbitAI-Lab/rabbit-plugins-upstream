## Description:

Image super-resolution tool: enhances image clarity and details, returning enhanced URL, suitable for low-res asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send image URLs or local image paths to dLazy's hosted super-resolution service and receive enhanced image URLs or saved output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a dLazy account or API key, and saving credentials in the local CLI config may not match every user's credential-handling policy.

Mitigation: Use the DLAZY_API_KEY environment variable per run when you do not want the key saved in ~/.dlazy/config.json, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Image URLs or local image files supplied to the command are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only with images appropriate for processing by the dLazy hosted service, and review the service terms before sending sensitive or regulated media.

Risk: A global CLI install persists the dLazy command on the local system.

Mitigation: Use the pinned npx invocation, npx @dlazy/cli@1.2.3, when you prefer on-demand execution without a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [JSON responses and optional saved image files produced through CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The primary result is an enhanced image URL; with --save, the CLI can download the generated image to a local path.]

## Skill Version(s):

1.3.21 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
