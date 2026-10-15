## Description:

Helps agents generate multilingual speech from text using Gemini 2.5 TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can guide an agent to create Chinese or English speech from a text prompt, with a choice of voice, using the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media are sent to the third-party dLazy service.

Mitigation: Confirm the service is trusted and avoid sending sensitive content without authorization.

Risk: The dLazy CLI may save an API key on the device, and installation runs third-party software.

Mitigation: Review the CLI before use; consider on-demand npx invocation and per-call DLAZY_API_KEY rather than persistent installation or credentials.

Risk: The documented sample describes image/png output despite the skill's speech purpose.

Mitigation: Check actual response type and audio format rather than relying on the sample.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides speech generation; the CLI returns hosted output URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
