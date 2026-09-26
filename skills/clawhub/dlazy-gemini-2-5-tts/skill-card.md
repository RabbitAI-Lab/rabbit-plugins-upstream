## Description:

使用 Gemini 2.5 文本转语音生成多语言、高自然度音频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate multilingual text-to-speech audio through the dLazy CLI and hosted Gemini 2.5 TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and selected local media inputs to dLazy's hosted service.

Mitigation: Avoid passing private prompts or local files unless uploading them to dLazy is intended.

Risk: The dLazy API key may be stored in the local CLI config.

Mitigation: Use OS account protections, prefer per-invocation environment variables where appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on an external pinned npm CLI package.

Mitigation: Review the publisher's CLI source or npm package before installation when supply-chain trust matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [CLI commands and JSON responses containing generated audio output URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated output URLs are hosted by dLazy, and async requests can return a generateId for later polling.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
