## Description:

PixVerse C1 generates videos from text prompts, images, first and last frames, or reference images, with options for resolution, aspect ratio, duration, and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use this skill to call dLazy's PixVerse C1 cloud video-generation CLI from an agent workflow for text-to-video, image-to-video, first/last-frame video, and reference-image video tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media files are sent to dLazy/PixVerse cloud services for generation.

Mitigation: Avoid sending sensitive prompts or media unless the user is comfortable with that service flow.

Risk: The CLI uses a dLazy API key and can persist it in the user's local configuration.

Mitigation: Use device login, rotate or revoke keys from the dLazy dashboard when needed, or use per-invocation credentials if a stored key is not desired.

Risk: Broad video-generation trigger wording could route an agent to this skill unintentionally.

Mitigation: Prefer product-specific requests such as 'pixverse c1' when invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous task identifier; cloud calls require a dLazy API key.]

## Skill Version(s):

1.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
