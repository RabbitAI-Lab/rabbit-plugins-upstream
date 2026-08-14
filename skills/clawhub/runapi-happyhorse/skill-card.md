## Description:

Generate text, image, or edit-video clips with HappyHorse through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through HappyHorse video generation with RunAPI, including text-to-video, image-to-video, reference-to-video, and edit-video workflows. It supports one-off CLI generation and SDK-oriented application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using this skill can submit paid RunAPI generation jobs.

Mitigation: Authenticate first, submit exactly one task per approved request, and do not submit a replacement task after a terminal service failure without user authorization.

Risk: Requests can include sensitive prompts or local media paths that may be uploaded to RunAPI.

Mitigation: Review request.json before execution when prompts or source media are sensitive, and only include local media paths the user intends to send.

Risk: A successful task status may not prove that all requested media deliverables are present and usable.

Mitigation: Validate the complete response, download every requested media deliverable, and require non-empty files with the expected MIME type before reporting completion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-happyhorse)
- [RunAPI HappyHorse Model](https://runapi.ai/models/happyhorse)
- [RunAPI HappyHorse Model Documentation](https://runapi.ai/models/happyhorse.md)
- [Alibaba Provider Overview](https://runapi.ai/providers/alibaba.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [HappyHorse SDK Integration](https://github.com/runapi-ai/happyhorse-sdk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to create request.json, submit RunAPI tasks, wait for results, validate response JSON, and download generated video media.]

## Skill Version(s):

0.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
