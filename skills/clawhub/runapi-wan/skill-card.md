## Description:

Generate and edit video with Wan through RunAPI. Use when the user asks an agent to create, edit, or transform video with Wan. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform Wan video assets through RunAPI. It guides one-off CLI generation and SDK-based application or backend integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI API credentials and submitted generation inputs may be handled by the RunAPI service.

Mitigation: Prefer RUNAPI_API_KEY environment authentication and use saved CLI credentials only when intentionally configured.

Risk: RunAPI-generated file URLs are temporary and should not be treated as long-term assets.

Mitigation: Download generated images, videos, audio, or other files into durable storage within 7 days.

Risk: Using the CLI as a production integration layer can create brittle application behavior.

Mitigation: Use the SDK integration path for apps, backends, workers, services, and production workflows; reserve the CLI for one-off tasks and manual testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-wan)
- [RunAPI Wan model overview](https://runapi.ai/models/wan)
- [RunAPI Wan model overview, pricing, and rate limits](https://runapi.ai/models/wan.md)
- [RunAPI Alibaba provider comparison](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)
- [Wan 2.2 A14B text to video turbo](https://runapi.ai/models/wan/2.2-a14b-text-to-video-turbo.md)
- [Wan 2.2 A14B image to video turbo](https://runapi.ai/models/wan/2.2-a14b-image-to-video-turbo.md)
- [Wan 2.2 A14B speech to video turbo](https://runapi.ai/models/wan/2.2-a14b-speech-to-video-turbo.md)
- [Wan 2.2 animate move](https://runapi.ai/models/wan/2.2-animate-move.md)
- [Wan 2.2 animate replace](https://runapi.ai/models/wan/2.2-animate-replace.md)
- [Wan 2.5 text to video](https://runapi.ai/models/wan/2.5-text-to-video.md)
- [Wan 2.5 image to video](https://runapi.ai/models/wan/2.5-image-to-video.md)
- [Wan 2.6 text to video](https://runapi.ai/models/wan/2.6-text-to-video.md)
- [Wan 2.6 image to video](https://runapi.ai/models/wan/2.6-image-to-video.md)
- [Wan 2.6 edit video](https://runapi.ai/models/wan/2.6-edit-video.md)
- [Wan 2.6 flash image to video](https://runapi.ai/models/wan/2.6-flash-image-to-video.md)
- [Wan 2.6 flash edit video](https://runapi.ai/models/wan/2.6-flash-edit-video.md)
- [Wan 2.7 text to video](https://runapi.ai/models/wan/2.7-text-to-video.md)
- [Wan 2.7 image to video](https://runapi.ai/models/wan/2.7-image-to-video.md)
- [Wan 2.7 image](https://runapi.ai/models/wan/2.7-image.md)
- [Wan 2.7 image pro](https://runapi.ai/models/wan/2.7-image-pro.md)
- [Wan 2.7 R2V text to video](https://runapi.ai/models/wan/2.7-r2v.md)
- [Wan 2.7 video edit](https://runapi.ai/models/wan/2.7-edit-video.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference temporary generated file URLs that should be downloaded to durable storage within 7 days.]

## Skill Version(s):

0.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
