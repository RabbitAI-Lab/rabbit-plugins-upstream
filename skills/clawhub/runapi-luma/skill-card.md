## Description:

Generate and edit video with Luma through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to create, edit, or transform video with Luma through RunAPI while validating request contracts, task status, and media deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use RunAPI credentials and make network requests to create potentially billable Luma generation tasks.

Mitigation: Confirm authentication, inspect request.json before submission when cost matters, submit exactly once, and do not create a replacement paid task without user authorization.

Risk: Referenced local media can be uploaded to RunAPI for generation or editing.

Mitigation: Review media paths and request fields before submission, and use only inputs the user intends to send to RunAPI.

Risk: A successful task status alone may not prove that the requested video deliverable is usable.

Mitigation: Validate the complete result contract, download every requested media URL, and require non-empty files with the expected video MIME type or family.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-luma)
- [RunAPI Luma homepage](https://runapi.ai/models/luma)
- [RunAPI Luma model documentation](https://runapi.ai/models/luma.md)
- [RunAPI Luma provider documentation](https://runapi.ai/providers/luma.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Luma SDK](https://github.com/runapi-ai/luma-sdk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands and JSON request/result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce downloaded video files after RunAPI task completion and deliverable verification.]

## Skill Version(s):

0.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
