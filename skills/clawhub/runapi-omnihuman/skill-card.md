## Description:

Create OmniHuman audio-to-video tasks and helper tasks for human identification and subject-mask detection through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate talking-head video from an image and audio file through RunAPI, or to run OmniHuman helper tasks for human identification and subject-mask detection. It supports one-off CLI workflows and directs application integrations to the current RunAPI SDK and product contract.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local image and audio media to RunAPI.

Mitigation: Review request.json before submission and only include media the user has authorized for upload.

Risk: Submitting OmniHuman tasks may create paid RunAPI tasks.

Mitigation: Submit once, preserve task evidence, and do not create replacement paid tasks without explicit user authorization.

Risk: RunAPI authentication may expose credentials if handled carelessly.

Mitigation: Use a scoped RUNAPI_API_KEY or saved CLI authentication, and use browser login only when the user explicitly requests it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-omnihuman)
- [RunAPI OmniHuman Homepage](https://runapi.ai/models/omnihuman)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/omnihuman.md)
- [Provider overview](https://runapi.ai/providers/bytedance.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/omnihuman-sdk)
- [OmniHuman 1.5 variant](https://runapi.ai/models/omnihuman/1.5.md)
- [OmniHuman 1.5 human identification variant](https://runapi.ai/models/omnihuman/1.5-human-identification.md)
- [OmniHuman 1.5 subject detection variant](https://runapi.ai/models/omnihuman/1.5-subject-detection.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Text]

**Output Format:** [Markdown guidance with shell command examples and JSON request instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce instructions for request.json, task/result JSON files, and downloaded video deliverables when the agent follows the workflow.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
