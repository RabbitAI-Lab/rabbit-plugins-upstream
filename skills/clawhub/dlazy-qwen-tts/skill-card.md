## Description:

Alibaba Bailian qwen3-tts text-to-speech with curated system voices, dialect options, and custom voice design from natural-language descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Qwen TTS service, generating speech from text with either curated voices or a natural-language voice description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local file paths may be sent to dLazy's hosted service.

Mitigation: Use the skill only when cloud processing is acceptable and choose input paths carefully.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or review local config storage if persistent credentials are not desired.

Risk: Generated files may be hosted on files.dlazy.com.

Mitigation: Avoid submitting sensitive prompts or media unless the hosted-output behavior is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response with generated media URLs, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; supports dry-run, asynchronous task polling, timeout, and optional save path.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
