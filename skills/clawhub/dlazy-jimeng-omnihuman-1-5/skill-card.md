## Description:

Helps generate digital-human broadcast videos from a portrait image and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request digital-human broadcast videos from portrait images and audio or text through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dLazy API key may be saved locally when using the CLI login flow.

Mitigation: Use DLAZY_API_KEY for per-session credentials when local key storage is undesirable, and rotate or revoke exposed keys.

Risk: Selected portrait images, audio, and prompts are sent to dLazy cloud services.

Mitigation: Confirm permission to upload the media and use dry-run before sending sensitive content.

Risk: The skill invokes a third-party CLI and may incur generation costs.

Mitigation: Review the CLI before installation and use dry-run to inspect the payload and cost estimate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may provide a generated media URL, saved file path, or asynchronous task ID.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
