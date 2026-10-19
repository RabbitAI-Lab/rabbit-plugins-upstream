## Description:

Helps agents clone a custom voice from a clean voice sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to provide a voice sample and request a cloned voice for text-to-speech work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples and related metadata may be sent to dLazy/ElevenLabs when the CLI is invoked.

Mitigation: Only provide voice samples and local files you intend to upload; confirm you are comfortable sharing them with those services.

Risk: The documentation mixes voice cloning with unrelated image and prompt examples, making the actual command behavior uncertain.

Mitigation: Review the installed command's help and check its payload and expected output with a dry run before submitting a real sample.

Risk: Persisted API keys may remain in local CLI configuration.

Mitigation: Prefer per-invocation API keys where practical and avoid exposing credentials in shared environments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI repository (skill metadata link; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and brief guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return a voice-cloning result or an asynchronous task identifier; the documented result example shows an unrelated image output.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
