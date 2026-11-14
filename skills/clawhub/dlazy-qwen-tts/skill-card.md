## Description:

Alibaba Bailian Qwen3-TTS text-to-speech with curated system voices, including dialects, and custom voices designed from natural-language descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to turn text into speech with a selected system voice or a custom voice description, in supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI login behavior and pinned package release were not verified by the security review.

Mitigation: Before authenticating, review the pinned @dlazy/cli 1.2.3 package and confirm how login handles the API key; use a key that can be rotated or revoked.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (skill-declared link)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Audio files, JSON response metadata]

**Output Format:** [Generated audio asset with a JSON result envelope containing output details or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a generated asset URL or save the audio to a requested local path; asynchronous mode returns a task identifier.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
