## Description:

Generates and edits images with GPT-4o Image through RunAPI, guiding agents to use the CLI for one-off tasks and SDKs for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to create, edit, or transform images through RunAPI. It helps agents choose CLI commands for one-off generation and SDK guidance for app, backend, worker, or service integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generated content are sent to RunAPI as part of normal image generation and editing workflows.

Mitigation: Confirm that using RunAPI as a third-party image generation provider is acceptable before installing or invoking the skill.

Risk: The skill may require installing the RunAPI CLI or SDKs and using a RunAPI API key.

Mitigation: Install dependencies from the documented RunAPI sources and prefer environment or saved-token authentication for agent and headless runs.

Risk: RunAPI-generated file URLs are temporary and should not be treated as durable assets.

Mitigation: Download generated images or other returned files into user-controlled durable storage within 7 days.

## Reference(s):

- [RunAPI GPT-4o Image model docs](https://runapi.ai/models/gpt-4o-image.md)
- [RunAPI GPT-4o Image homepage](https://runapi.ai/models/gpt-4o-image)
- [RunAPI OpenAI provider page](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and SDK package references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance distinguishes one-off CLI usage from production SDK integration and notes that generated file URLs are temporary.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
