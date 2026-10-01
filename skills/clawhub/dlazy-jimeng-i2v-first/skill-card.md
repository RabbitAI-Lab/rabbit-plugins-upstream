## Description:

Helps agents generate a video from a first-frame image and a text prompt using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a supplied first-frame image and prompt into a short generated video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be sent to dLazy's hosted service.

Mitigation: Share only content you are authorized to upload and review the service terms before use.

Risk: Login can save an API key locally.

Mitigation: Protect local credentials or use DLAZY_API_KEY per invocation to avoid saving a key.

Risk: The documented input flag and sample output conflict with the video-generation description.

Mitigation: Check current CLI help and verify the returned media type before relying on the result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned via hosted URLs; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
