## Description:

Generate and edit images with Qwen 3 through RunAPI, using the RunAPI CLI for one-off tasks and SDKs for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform images with Qwen 3 through RunAPI. It guides one-off CLI use and points application integrations toward the RunAPI SDK path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, source images, or API credentials may be sent to RunAPI when using the skill.

Mitigation: Confirm RunAPI is trusted for the task, use RUNAPI_API_KEY or the documented CLI authentication flow, and avoid putting sensitive images or secrets in request files.

Risk: Generated file URLs are temporary and may be lost if treated as durable assets.

Mitigation: Download and store generated outputs in durable storage within 7 days when the user needs to retain them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-qwen-3)
- [RunAPI Qwen 3 Homepage](https://runapi.ai/models/qwen-3)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/qwen-3.md)
- [Provider comparison](https://runapi.ai/providers/alibaba.md)
- [Full model catalog](https://runapi.ai/models.md)
- [Text to image variant](https://runapi.ai/models/qwen-3/text-to-image.md)
- [Image edit variant](https://runapi.ai/models/qwen-3/edit-image.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands, SDK package names, authentication guidance, and storage guidance for generated files.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
