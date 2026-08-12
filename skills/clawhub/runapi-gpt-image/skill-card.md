## Description:

Generate and edit images with GPT Image through RunAPI. Use when the user asks an agent to create, edit, or transform images with GPT Image. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate, edit, or transform images through RunAPI's GPT Image service. For production integrations, the skill directs agents to use the current RunAPI SDK reference instead of shelling out to the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, source media, generated request files, task responses, result URLs, and downloaded image outputs may contain sensitive project information.

Mitigation: Use RunAPI only for content appropriate to that service, prefer environment or saved CLI authentication, and clean up or store generated JSON and media files according to the project's data-handling requirements.

Risk: A malformed request or contract mismatch can produce failed or unintended paid RunAPI tasks.

Mitigation: Discover the current CLI and API contract before execution, submit only once by default, preserve task evidence, and retry only under the bounded recovery rules described by the skill.

## Reference(s):

- [RunAPI GPT Image model page](https://runapi.ai/models/gpt-image)
- [RunAPI GPT Image documentation](https://runapi.ai/models/gpt-image.md)
- [RunAPI OpenAI provider documentation](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI GPT Image SDK](https://github.com/runapi-ai/gpt-image-sdk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON file examples, and integration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create request.json, task.json, result.json, downloaded image files, and local authentication status evidence during agent execution.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
