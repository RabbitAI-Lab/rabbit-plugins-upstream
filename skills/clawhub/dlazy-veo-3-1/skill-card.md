## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Veo 3.1 service for agent-assisted video generation, including prompt-based generation, frame-guided generation, reference-image generation, and video extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media may be sent to dLazy hosted endpoints for generation.

Mitigation: Install and invoke the skill only when the user intends to use dLazy's hosted service, and avoid sending sensitive prompts or media unless that service use is acceptable.

Risk: API keys may be stored in the local dLazy CLI configuration.

Mitigation: Prefer a per-invocation DLAZY_API_KEY for temporary use, or rotate and revoke stored keys from the dLazy dashboard when access should change.

Risk: Local image, video, or audio files passed to the CLI can be uploaded to dLazy media storage.

Mitigation: Review file paths before invocation and pass only media files intended for cloud processing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous generation IDs, or downloaded media files when saving is requested.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
