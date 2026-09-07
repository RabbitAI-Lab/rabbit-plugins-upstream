## Description:

Generates dynamic videos with Kling v3 Omni from prompts and multimodal references through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to ask an agent to invoke dLazy's Kling v3 Omni workflow for text-to-video, image-to-video, and reference-based video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or invokes the external dLazy CLI package rather than vendoring executable code.

Mitigation: Install only after trusting the dLazy CLI and npm package; prefer the npx invocation or an unprivileged sandbox when avoiding a persistent global binary.

Risk: Prompts and local media references can be uploaded to dLazy's hosted API and media storage.

Mitigation: Avoid sending private or sensitive media unless the user is comfortable with upload to dLazy's service and has reviewed applicable terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [npm package @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result payload with generated media URLs; optional downloaded media file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and referenced local media may be sent to dLazy API and file-hosting endpoints.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
