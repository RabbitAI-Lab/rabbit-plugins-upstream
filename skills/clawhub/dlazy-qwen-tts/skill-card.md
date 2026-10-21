## Description:

Generates speech from text with Qwen3-TTS using preset voices or voices designed from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate spoken audio from text with preset voices or a custom voice description through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts are sent to a third-party cloud service.

Mitigation: Avoid submitting sensitive text unless the service's handling is acceptable.

Risk: The external CLI requires installation and can store an API key locally after login.

Mitigation: Review the pinned package before installation and protect or rotate the API key.

Risk: The English skill file describes a different tool, and some examples show image output rather than speech.

Mitigation: Verify the intended command and actual output with CLI help before use; do not rely on the conflicting examples.

Risk: Saving generated results can write files to disk.

Mitigation: Confirm the destination path before using --save.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Audio files]

**Output Format:** [CLI JSON response with a hosted result URL; optional downloaded audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of a completed result.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
