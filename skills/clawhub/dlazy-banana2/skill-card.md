## Description:

Generate/edit high-quality images with Nano Banana 2.0. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy Nano Banana 2 cloud image service from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to the dLazy cloud service.

Mitigation: Confirm that prompts and media are appropriate for a third-party cloud image service before invoking the skill.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Use the documented authentication flow only on trusted systems, and rotate or revoke the API key when access is no longer needed.

Risk: A persistent global CLI install may remain on the system.

Mitigation: Use npx or the pinned CLI version when a non-persistent or reproducible invocation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [npm package @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON image-result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs or save generated image files locally when requested.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
