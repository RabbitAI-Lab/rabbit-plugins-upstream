## Description:

Generates speech from text using Qwen3-TTS through the dLazy service, with preset voices or a voice designed from a description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn text into speech with a selected system voice or a custom voice description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the third-party dLazy CLI executes external software.

Mitigation: Review the pinned CLI package and its source before installation or use.

Risk: Authentication stores a dLazy API key locally, and prompts are sent to dLazy's hosted API.

Mitigation: Use only data suitable for the hosted service; protect the key and rotate or revoke it if needed.

Risk: The documented example shows image/png output despite this being a speech-generation skill.

Mitigation: Verify actual audio output using CLI help or a dry run before relying on the example.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands and audio result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI reports hosted result URLs in JSON; --save can download the result, and --no-wait returns an asynchronous task ID.]

## Skill Version(s):

1.3.25 (source: server release metadata; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
