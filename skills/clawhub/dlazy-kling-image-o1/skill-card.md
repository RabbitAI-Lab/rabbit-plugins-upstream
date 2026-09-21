## Description:

Generate images with the Kling o1 model through the dLazy CLI/API, supporting text-to-image and reference image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Kling o1 through dLazy's hosted API. It is suited for workflows that can send prompts and optional reference images to a cloud image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media may be uploaded to dLazy's hosted API and generated outputs may be hosted by dLazy.

Mitigation: Use the skill only for content that is appropriate to send to the hosted service, and review dLazy's service terms before processing sensitive media.

Risk: Authentication can store a dLazy API key in the user's local CLI configuration.

Mitigation: Prefer per-invocation credentials or the pinned npx invocation when persistent local configuration is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result envelopes containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are returned as hosted file URLs and may be downloaded locally with the CLI save option.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
