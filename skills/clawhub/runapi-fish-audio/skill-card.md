## Description:

Create account-owned Fish Audio voice resources, attempt to reuse their IDs, or generate MP3/WAV speech through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Fish Audio voice resources and generate speech through their RunAPI account for one-off artifacts or application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use RunAPI credentials and can potentially incur service billing.

Mitigation: Confirm authentication and user authorization before submitting requests; do not retry a paid request unless evidence shows no task was created and retrying is safe.

Risk: The skill may upload source audio or other media inputs and create account-owned voice resources.

Mitigation: Review Fish Audio handling of source audio and voice resources before submitting sensitive recordings.

Risk: A generated media URL is not itself proof that the requested deliverable is usable.

Mitigation: Download every requested media deliverable and verify that each file is non-empty and matches the expected audio MIME type before reporting completion.

Risk: Voice IDs and reusable voice resources may not remain available, and this release has no update, delete, revoke, or voice-library management workflow.

Mitigation: Treat returned voice IDs as best-effort references and avoid claiming lifecycle controls that the skill does not provide.

## Reference(s):

- [RunAPI Fish Audio Model Page](https://runapi.ai/models/fish-audio)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/fish-audio.md)
- [Provider overview](https://runapi.ai/providers/fish-audio.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/fish-audio-sdk)
- [Fish Audio s1 variant](https://runapi.ai/models/fish-audio/s1.md)
- [Fish Audio s2-pro variant](https://runapi.ai/models/fish-audio/s2-pro.md)
- [Fish Audio s2.1-pro variant](https://runapi.ai/models/fish-audio/s2.1-pro.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to create request JSON, run RunAPI CLI commands, inspect SDK references, save service responses, and verify downloaded audio files.]

## Skill Version(s):

0.4.0 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
