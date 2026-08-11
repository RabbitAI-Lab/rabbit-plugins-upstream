## Description:

Generates or edits high-quality images with Nano Banana 2.0 from text prompts and optional input images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate or edit images through the dLazy hosted API using the pinned dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad image-generation triggers can route prompts and selected local media to dLazy.

Mitigation: Review requests before invocation and use the skill only when the user is comfortable sending the prompt and referenced media to dLazy.

Risk: Persistent login stores a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation or rotate and revoke organization keys from the dLazy dashboard when local key storage is a concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [JSON responses with hosted image URLs and Markdown guidance for command usage and errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when no-wait mode is used; generated image assets are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
