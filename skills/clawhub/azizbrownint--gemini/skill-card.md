## Description:

Gemini CLI one-shot prompts, summaries, generation, skills, hooks, MCP, or Gemma routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to ask an agent to run Gemini CLI one-shot prompts for questions, summaries, generated content, JSON responses, extension management, hooks, MCP, and Gemma routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and piped files sent through gemini may leave the local machine for Google's Gemini service.

Mitigation: Avoid sending sensitive data unless approved for that service, and review prompt content before execution.

Risk: Gemini extensions, hooks, MCP servers, or --yolo execution can change tool behavior or reduce safety controls.

Mitigation: Manage only trusted extensions, hooks, and MCP servers, and avoid --yolo unless explicitly authorized.

## Reference(s):

- [Google AI for Developers](https://ai.google.dev/)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/gemini)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and Gemini CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the gemini binary; JSON output can be requested with --output-format json.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
