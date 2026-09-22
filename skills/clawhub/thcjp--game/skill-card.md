## Description:

This skill helps an agent turn a short game concept into playable browser-game code and related game design guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers, prototypers, and creative builders use this skill to generate playable HTML game prototypes, game mechanics, level structures, and implementation guidance from concise game concepts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and shell command authority for game-generation workflows.

Mitigation: Use it only in a controlled workspace and explicitly review any package installs, shell commands, or file writes before execution.

Risk: The artifact describes generic API and network capabilities without clear operational boundaries.

Mitigation: Avoid providing API keys or sensitive credentials unless a specific endpoint, purpose, and handling plan are clear.

Risk: Generated game code may contain logic, dependency, or browser-runtime issues.

Mitigation: Review generated code, run it in a sandboxed browser or isolated project, and test gameplay, permissions, and dependency behavior before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/game)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub skill page](https://skillhub.cn/skill/)
- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and code-oriented outputs, commonly including self-contained HTML, JavaScript, CSS, JSON examples, and setup commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include playable single-file HTML games, project code, generated game metadata, controls, feature lists, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
