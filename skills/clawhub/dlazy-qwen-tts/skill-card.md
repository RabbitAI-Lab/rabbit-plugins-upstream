## Description:

Generates speech from text with Alibaba Bailian Qwen3-TTS, using a system voice or a custom voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text into speech with a selected voice or a voice designed from a description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy's hosted API.

Mitigation: Confirm the service is suitable for the text before submitting sensitive prompts.

Risk: The skill relies on a third-party CLI and an API key.

Mitigation: Review the CLI before use, consider its pinned npx invocation instead of a global install, and use a key that can be rotated or revoked.

Risk: The documented example shows an image rather than the expected audio output.

Mitigation: Check the actual audio output before passing it to downstream tools.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speech generation produces audio; the documented output example mistakenly shows an image.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
