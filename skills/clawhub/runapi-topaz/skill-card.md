## Description:

Upscale and enhance media with Topaz through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to upscale or enhance images and videos with Topaz through RunAPI. It supports one-off CLI tasks and points application integrations toward RunAPI SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images or videos may be sent to RunAPI/Topaz for processing.

Mitigation: Install and use the skill only when third-party media processing is acceptable for the user's data and workflow.

Risk: API tokens may be saved locally when imported into CLI configuration.

Mitigation: Prefer environment-based authentication with RUNAPI_API_KEY for agent and headless runs when possible.

Risk: Generated file URLs are temporary and may expire.

Mitigation: Download and store generated media in durable storage within 7 days.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-topaz)
- [RunAPI Topaz model overview](https://runapi.ai/models/topaz)
- [Topaz model documentation](https://runapi.ai/models/topaz.md)
- [Topaz provider comparison](https://runapi.ai/providers/topaz.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Image upscale variant](https://runapi.ai/models/topaz/upscale-image.md)
- [Video upscale variant](https://runapi.ai/models/topaz/upscale-video.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and SDK guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference temporary generated media URLs that should be downloaded to durable storage within 7 days.]

## Skill Version(s):

0.2.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
