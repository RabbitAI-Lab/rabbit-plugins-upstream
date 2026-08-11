## Description:

Generate and edit images, create or extend video from images, derive or shorten prompt suggestions, and look up seeds with Midjourney through RunAPI. Use the RunAPI CLI for one-off work and the language SDKs for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate Midjourney images and videos, edit images, obtain prompt suggestions, shorten prompts, and retrieve seeds through RunAPI. It guides agents toward SDK-based application integrations and CLI-based one-off or manual verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI and Midjourney process prompts, generated-media requests, and publicly fetchable image or video input URLs.

Mitigation: Use only content appropriate for the external service, and avoid private images, videos, or sensitive prompt content unless approved for that service.

Risk: Production integrations that shell out to the CLI can be brittle and harder to operate.

Mitigation: Use the language SDK path for applications, backends, workers, libraries, and production workflows; reserve the CLI for one-off tasks and manual verification.

Risk: Generated media URLs are temporary.

Mitigation: Download and store required generated images or videos in durable storage before the URLs expire.

## Reference(s):

- [RunAPI Midjourney homepage](https://runapi.ai/models/midjourney)
- [RunAPI Midjourney model overview](https://runapi.ai/models/midjourney.md)
- [Midjourney V8.1 text-to-image](https://runapi.ai/models/midjourney/v8.1.md)
- [Midjourney image editing](https://runapi.ai/models/midjourney/edit-image.md)
- [Midjourney image to video](https://runapi.ai/models/midjourney/image-to-video.md)
- [RunAPI Midjourney provider page](https://runapi.ai/providers/midjourney.md)
- [RunAPI model catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands and SDK package identifiers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require the runapi binary, a RunAPI SDK, and RUNAPI_API_KEY or saved CLI authentication; generated media URLs are temporary.]

## Skill Version(s):

0.3.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
