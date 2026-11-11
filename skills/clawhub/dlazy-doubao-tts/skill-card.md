## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can turn supplied text into spoken audio with Doubao TTS, choosing a supported language, voice, and speed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts to dLazy's hosted API; local media paths passed to media options are uploaded to its storage.

Mitigation: Avoid sending sensitive text or media unless the service terms and your data policy allow it.

Risk: ClawScan reports a benign verdict with medium confidence and notes that some documented CLI steps do not clearly match the stated text-to-speech purpose; the documented behavior does not establish a demonstrated TTS operation.

Mitigation: Review the pinned CLI installation and authentication steps, then check the command with non-sensitive sample text before relying on it.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Shell commands]

**Output Format:** [Generated audio asset, returned with JSON result metadata or saved to a requested file path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports Chinese and English voice options, configurable speed, and asynchronous task identifiers.]

## Skill Version(s):

1.3.39 (source: evidence.json release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
