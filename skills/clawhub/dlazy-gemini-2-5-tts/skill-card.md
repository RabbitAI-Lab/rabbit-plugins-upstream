## Description:

Guides agents in generating multilingual speech from text using Gemini 2.5 TTS through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to guide an agent in turning text into speech with selectable voices and languages through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected parameters, and explicitly supplied local files may be sent to dLazy's cloud service.

Mitigation: Avoid sending sensitive content or files unless authorized to share them with dLazy.

Risk: Login can save an API key locally, and a global CLI installation persists on the device.

Mitigation: Protect and rotate the API key as needed; use the pinned on-demand CLI invocation if a persistent installation is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses can include hosted result URLs or asynchronous task IDs.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; skill files list 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
