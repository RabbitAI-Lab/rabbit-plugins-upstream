## Description:

Synthesize natural-sounding speech from text using Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate spoken narration from text in Chinese or English with selectable voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to the dLazy hosted service, and generated results are hosted there.

Mitigation: Use only content you are comfortable sharing with dLazy and review selected file paths before invoking the CLI.

Risk: Logging in saves an API key locally, while a global CLI installation remains installed.

Mitigation: Use DLAZY_API_KEY and the pinned npx command if you prefer not to store a key or install a persistent CLI.

Risk: Default voice language or output path may not match the intended result.

Mitigation: Specify voice language and output path explicitly when generating speech.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation results are hosted by dLazy; asynchronous requests return a task ID for later retrieval.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
