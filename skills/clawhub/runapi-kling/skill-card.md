## Description:

Generate and edit video with Kling through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform video with Kling through RunAPI. It supports one-off CLI generation and SDK-oriented guidance for application integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI API keys or saved CLI credentials may be exposed if copied into source files, logs, or shared prompts.

Mitigation: Use environment-based auth or saved CLI config, and avoid hardcoding RUNAPI_API_KEY in project files or command histories.

Risk: Prompts, images, or videos submitted to RunAPI/Kling may include sensitive content.

Mitigation: Submit sensitive media or prompts only when the RunAPI account terms and data-handling expectations allow it.

Risk: Generated asset URLs are temporary and may expire before downstream workflows consume them.

Mitigation: Download generated videos or other assets into durable storage within the stated 7-day window.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-kling)
- [RunAPI Kling Homepage](https://runapi.ai/models/kling)
- [RunAPI Kling Model Overview](https://runapi.ai/models/kling.md)
- [RunAPI Kuaishou Provider Page](https://runapi.ai/providers/kuaishou.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include request-shaping guidance for Kling model variants, RunAPI CLI commands, SDK package choices, and temporary asset storage reminders.]

## Skill Version(s):

0.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
