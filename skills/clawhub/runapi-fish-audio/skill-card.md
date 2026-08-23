## Description:

Create account-owned Fish Audio voice resources, attempt to reuse their IDs, or generate MP3/WAV speech through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Fish Audio voice resources, build RunAPI requests, generate speech, and integrate Fish Audio through the RunAPI CLI or SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI requests may require API authentication, can incur billing, and can upload source audio selected by the user.

Mitigation: Install and use the skill only when RunAPI/Fish Audio is intended; provide only audio that the user has rights and consent to process, and confirm authentication before submitting requests.

Risk: Generated or retrieved voice IDs may not remain usable, and voice resources must be ready before reuse.

Mitigation: Check voice state and use a voice only after it is trained; treat returned voice IDs as best-effort references rather than permanent assets.

## Reference(s):

- [RunAPI Fish Audio homepage](https://runapi.ai/models/fish-audio)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/fish-audio.md)
- [Provider overview](https://runapi.ai/providers/fish-audio.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/fish-audio-sdk)
- [s1 variant](https://runapi.ai/models/fish-audio/s1.md)
- [s2-pro variant](https://runapi.ai/models/fish-audio/s2-pro.md)
- [s2.1-pro variant](https://runapi.ai/models/fish-audio/s2.1-pro.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Text, Audio files]

**Output Format:** [Markdown guidance with shell commands, JSON request files, integration code, text responses, and MP3/WAV outputs when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the runapi CLI or SDK, optional RUNAPI_API_KEY authentication, contract discovery before execution, and verification of downloaded audio MIME types.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
