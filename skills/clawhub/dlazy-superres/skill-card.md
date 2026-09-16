## Description:

Image super-resolution tool that enhances image clarity and detail and returns an enhanced image URL for low-resolution asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to submit an image URL or local image path to dLazy's hosted super-resolution service and receive a clearer upscaled image URL or saved output file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the skill executes a third-party npm CLI.

Mitigation: Use the pinned on-demand command `npx @dlazy/cli@1.2.3` when a persistent global install is not required.

Risk: The CLI may save a dLazy API key in the local user configuration.

Mitigation: Use the documented config location and rotate or revoke organization-scoped API keys from the dLazy dashboard when needed.

Risk: Images supplied to the skill are uploaded to dLazy's hosted service.

Mitigation: Avoid sending sensitive images unless dLazy's terms and account controls are acceptable for the intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, async task identifiers, or saved image files depending on CLI flags.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
