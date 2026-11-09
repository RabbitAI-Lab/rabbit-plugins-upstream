## Description:

Generates speech from text with Alibaba Bailian Qwen3-TTS, using a curated system voice or a voice designed from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can turn text into spoken audio with a selected system voice, including dialect options, or a custom voice described in natural language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media sent for generation are shared with the dLazy service.

Mitigation: Avoid submitting confidential or sensitive content unless its use with the service is approved.

Risk: The security scan had partial coverage and did not verify the referenced CLI and some local references.

Mitigation: Review the CLI project and service terms before installing or sending content.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated audio (hosted URL or saved file) with JSON response metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before the audio is ready.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
