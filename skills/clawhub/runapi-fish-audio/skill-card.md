## Description:

Generate MP3 or WAV speech with Fish Audio through RunAPI for one-off speech generation or application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate speech with Fish Audio through RunAPI, either through the RunAPI CLI for one-off requests or language SDKs for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text, reference audio, transcripts, and generated audio URLs are handled by a third-party service.

Mitigation: Treat these inputs and outputs as third-party service data and avoid sending sensitive content unless the deployment's data handling requirements allow it.

Risk: RunAPI API keys can grant access to speech generation services.

Mitigation: Store credentials in RUNAPI_API_KEY or saved RunAPI configuration and avoid embedding keys in prompts, source files, or request examples.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-fish-audio)
- [RunAPI Fish Audio Homepage](https://runapi.ai/models/fish-audio)
- [Fish Audio Model Overview](https://runapi.ai/models/fish-audio.md)
- [Fish Audio Provider Page](https://runapi.ai/providers/fish-audio.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [Fish Audio s1](https://runapi.ai/models/fish-audio/s1.md)
- [Fish Audio s2-pro](https://runapi.ai/models/fish-audio/s2-pro.md)
- [Fish Audio s2.1-pro](https://runapi.ai/models/fish-audio/s2.1-pro.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and SDK integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce request JSON guidance for text-to-speech inputs and audio response handling.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
