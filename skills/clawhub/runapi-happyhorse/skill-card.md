## Description:

Generate text, image, or edit-video clips with HappyHorse through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create or edit HappyHorse video clips through RunAPI, using the CLI for one-off generation and SDKs for application or backend integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, or source videos may be sent to RunAPI for media generation.

Mitigation: Use the skill only for content that may be shared with RunAPI and avoid sending sensitive media unless approved.

Risk: API key use can create credential exposure or local credential persistence.

Mitigation: Prefer environment-based RUNAPI_API_KEY authentication unless saved CLI credentials are intentional.

Risk: Generated file URLs are temporary and should not be treated as durable assets.

Mitigation: Download generated media and store it in approved durable storage within 7 days.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/runapi-ai/skills/runapi-happyhorse)
- [RunAPI HappyHorse model overview](https://runapi.ai/models/happyhorse)
- [HappyHorse model documentation](https://runapi.ai/models/happyhorse.md)
- [HappyHorse text-to-video documentation](https://runapi.ai/models/happyhorse/text-to-video.md)
- [HappyHorse character documentation](https://runapi.ai/models/happyhorse/character.md)
- [HappyHorse image-to-video documentation](https://runapi.ai/models/happyhorse/image-to-video.md)
- [HappyHorse edit-video documentation](https://runapi.ai/models/happyhorse/edit-video.md)
- [Alibaba provider comparison](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill guidance](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide RunAPI media generation requests and temporary output URLs; durable asset storage is user-managed.]

## Skill Version(s):

0.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
