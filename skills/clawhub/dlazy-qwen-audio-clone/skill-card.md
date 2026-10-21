## Description:

Helps agents clone a voice from a clean audio sample using Alibaba Bailian Qwen3-TTS for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users provide an authorized voice sample to create a custom voice for subsequent text-to-speech requests through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a voice without the speaker's consent could enable impersonation.

Mitigation: Use only voice samples you own or have explicit permission to clone.

Risk: Voice samples and generated artifacts may leave the local machine for hosted processing.

Mitigation: Obtain consent before uploading sensitive audio and review the service's data-handling terms.

Risk: Conflicting command and output examples may cause failed or misleading agent actions.

Mitigation: Check the installed command's help and verify actual results before relying on the examples; the publisher should correct the documentation.

Risk: Saved credentials or global CLI installation increase local exposure.

Mitigation: Prefer per-invocation DLAZY_API_KEY and the pinned npx option when persistent credentials or a global install are unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service may return output URLs or an asynchronous task identifier; the documented image output example conflicts with the voice-cloning use case.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
