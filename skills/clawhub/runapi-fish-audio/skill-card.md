## Description:

Create account-owned Fish Audio voice resources, attempt to reuse their IDs, or generate MP3/WAV speech through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external teams use this skill to create or inspect account-owned Fish Audio voice resources and generate MP3/WAV speech through RunAPI for one-off work or application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio and voice data can be sensitive and may require rights or consent before use.

Mitigation: Confirm trust in RunAPI/Fish Audio and only create or reuse voices when the user has appropriate rights and consent.

Risk: Submitted RunAPI requests may incur billing.

Mitigation: Submit only after authentication and contract checks, and avoid repeated paid requests without user authorization.

Risk: The RUNAPI_API_KEY can grant access to the user's RunAPI account.

Mitigation: Prefer environment authentication or saved CLI configuration, keep the key scoped and protected, and use browser login only when explicitly requested.

Risk: Voice IDs and voice readiness can change over time.

Mitigation: Use a voice only after its state is trained, treat returned voice IDs as best-effort references, and preserve service evidence when a request fails.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/runapi-ai/skills/runapi-fish-audio)
- [RunAPI Fish Audio model overview](https://runapi.ai/models/fish-audio)
- [RunAPI Fish Audio documentation](https://runapi.ai/models/fish-audio.md)
- [Fish Audio provider overview](https://runapi.ai/providers/fish-audio.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Fish Audio SDK integration](https://github.com/runapi-ai/fish-audio-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request files, CLI or SDK responses, and downloaded audio files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses and media deliverables should be preserved and verified against the discovered RunAPI contract.]

## Skill Version(s):

0.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
