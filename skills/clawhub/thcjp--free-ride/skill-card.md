## Description:

免费版 helps agents manage and call free OpenRouter AI models for SkillHub workflows, including model calls, conversational AI, and automation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and teams use this skill to configure and run OpenRouter-backed AI model calls, agent workflows, and automation tasks. It is not appropriate for critical decisions requiring fully deterministic results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send user content to external AI or API services.

Mitigation: Use only non-sensitive data unless the publisher documents API recipients, encryption responsibilities, and confirmation behavior.

Risk: The skill asks for broad file read/write and system command authority.

Mitigation: Run it in a constrained workspace and require review of command scope or a documented command whitelist before installation.

Risk: The evidence reports weak scoping and unsupported safety assurances.

Mitigation: Review the artifact and security guidance before use, and avoid relying on the skill for critical deterministic decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/free-ride)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an API key and may guide the agent to read files, write files, call external APIs, or run system commands.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
