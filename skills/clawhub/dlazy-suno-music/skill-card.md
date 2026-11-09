## Description:

Generates Suno music from prompts in inspiration mode with automatic lyrics or custom mode with supplied lyrics, with vocals or instrumental-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate music from a text prompt, choosing automatic or supplied lyrics, a vocal or instrumental result, and optional style settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan notes that the supplied login behavior is not demonstrated to support the stated music-generation purpose.

Mitigation: Review the complete skill and CLI install details before installing, as the scan guidance recommends.

Risk: Prompts and any local media supplied to the CLI are sent to dLazy hosted services.

Mitigation: Avoid sending sensitive prompts or media unless you are comfortable sharing them with the service.

## Reference(s):

- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands, Guidance]

**Output Format:** [JSON response with generated audio URLs; audio files can optionally be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-driven generation with optional style, title, vocal, and instrumental settings; asynchronous runs can return a task ID.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
