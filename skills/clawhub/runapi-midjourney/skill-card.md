## Description: <br>
Generate and edit images, create or extend video from images, derive or shorten prompt suggestions, and look up seeds with Midjourney through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to integrate Midjourney through RunAPI for image generation, image editing, image-to-video, video extension, prompt derivation, prompt shortening, and seed lookup workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, API keys, and media URLs may be sent to RunAPI and downstream services during normal image and video generation. <br>
Mitigation: Confirm trust in RunAPI before installation, use environment authentication or saved CLI configuration, and avoid sending sensitive prompts or non-public media URLs unless authorized. <br>
Risk: Generated media URLs are temporary, and some operations depend on account-owned task IDs or publicly fetchable input media. <br>
Mitigation: Download generated media to durable storage, verify task ownership before extension or seed lookup, and ensure input URLs are intentionally public. <br>


## Reference(s): <br>
- [RunAPI Midjourney model overview](https://runapi.ai/models/midjourney) <br>
- [RunAPI Midjourney documentation](https://runapi.ai/models/midjourney.md) <br>
- [Midjourney V8.1 text-to-image documentation](https://runapi.ai/models/midjourney/v8.1.md) <br>
- [Midjourney image editing documentation](https://runapi.ai/models/midjourney/edit-image.md) <br>
- [Midjourney image-to-video documentation](https://runapi.ai/models/midjourney/image-to-video.md) <br>
- [RunAPI Midjourney provider page](https://runapi.ai/providers/midjourney.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill guidance](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, SDK package names, and integration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce RunAPI CLI commands, SDK integration direction, request-field checks, and result-handling guidance.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
