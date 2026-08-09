## Description: <br>
Self-reflect, self-critique, self-learn, and organize memory with structured logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add structured self-reflection, correction logging, memory organization, and local learning workflows to AI coding agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can record broad user-profile information without clear consent or scope controls. <br>
Mitigation: Install only when persistent local agent memory is intended; prefer passive or strict mode and require confirmation before writes. <br>
Risk: Memory and learning logs can expose sensitive workspace information if raw messages, command output, or secrets are captured. <br>
Mitigation: Disable raw-message logging and proactive profiling in sensitive workspaces, redact secrets, and periodically inspect or delete ~/self-improving/, .learnings/, USER.md, and notes/*.md. <br>
Risk: Global hooks can cause self-improvement behavior to run in contexts where it was not expected. <br>
Mitigation: Avoid global hooks unless they are explicitly required; scope hooks to trusted workspaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/self-improving) <br>
- [Hook Setup Guide](references/hooks-setup.md) <br>
- [OpenClaw Integration](references/openclaw-integration.md) <br>
- [Entry Examples](references/examples.md) <br>
- [Rule Categories](references/rule_categories.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to create or update local memory and learning logs.] <br>

## Skill Version(s): <br>
2.6.0 (source: SKILL.md frontmatter, server release metadata, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
