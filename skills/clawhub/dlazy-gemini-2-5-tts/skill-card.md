## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech. 使用 Gemini 2.5 强大的文本转语音能力，生成多语言、高自然度的音频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate Chinese or English speech audio from prompts, choosing a voice for the output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted API, and local media may be uploaded to its storage service.

Mitigation: Submit only text and media that are appropriate to share with dLazy and its hosted service.

Risk: The CLI saves an API key in the user's local configuration, and generation consumes paid credits.

Mitigation: Protect the saved key, rotate or revoke it if exposed, and check credit costs before generating.

Risk: The external npm implementation and hosted service were not audited in the supplied security review.

Mitigation: Review the pinned CLI and relevant service terms before installation and use.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON result metadata]

**Output Format:** [Generated speech audio with JSON result metadata and output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice language (Chinese or English) and voice are configurable.]

## Skill Version(s):

1.3.37 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
