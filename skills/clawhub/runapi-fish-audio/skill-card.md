## Description:

Generate MP3 or WAV speech with Fish Audio through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate speech audio with Fish Audio through RunAPI, either as one-off CLI requests or SDK-backed application integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to RunAPI/Fish Audio and may upload referenced local media inputs.

Mitigation: Use only approved inputs, review request files before submission, and work from a private directory.

Risk: RunAPI requests may incur paid API usage.

Mitigation: Authenticate deliberately and do not resubmit after terminal service failures without user authorization.

Risk: Request, response, and generated audio files may be saved locally.

Mitigation: Avoid secrets in request files and delete generated artifacts when they are no longer needed.

## Reference(s):

- [RunAPI Fish Audio Homepage](https://runapi.ai/models/fish-audio)
- [Model Overview, Pricing, and Rate Limits](https://runapi.ai/models/fish-audio.md)
- [Provider Overview](https://runapi.ai/providers/fish-audio.md)
- [Full Model Catalog](https://runapi.ai/models.md)
- [SDK Integration](https://github.com/runapi-ai/fish-audio-sdk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request files, SDK code, saved responses, and downloaded audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save request, response, and generated audio files locally; downloaded media is verified for non-empty audio MIME output.]

## Skill Version(s):

0.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
