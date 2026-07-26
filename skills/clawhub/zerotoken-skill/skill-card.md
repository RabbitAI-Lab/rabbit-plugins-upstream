## Description: <br>
Token-efficient assistant discipline for concise answers and task execution. Use when the user asks for direct, low-token work, or invokes this skill; includes optional file and Windows encoding utilities declared below. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phoenixlucky](https://clawhub.ai/user/phoenixlucky) <br>

### License/Terms of Use: <br>
GPL-3.0 <br>


## Use Case: <br>
Developers and agent users use this skill to keep assistant work concise, proportional, and task-focused while preserving necessary validation. It also provides optional local file-editing and encoding utilities for workflows that need them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad local file reads, writes, and batch edits. <br>
Mitigation: Review target paths and diffs before applying changes, and keep edits scoped to the user-requested files. <br>
Risk: Encoding repair and conversion utilities can rewrite file contents. <br>
Mitigation: Run scan or preview modes first, and use backup options before convert or fix operations. <br>
Risk: Browser or web search guidance may send query content to external services. <br>
Mitigation: Avoid sensitive data in search queries and prefer trusted sources for research. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phoenixlucky/skills/zerotoken-skill) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with concise text, inline commands, and code snippets when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Task-dependent concise responses; optional file edits, batch text replacements, and encoding utility commands when explicitly needed.] <br>

## Skill Version(s): <br>
1.8.2 (source: frontmatter, package.json, changelog, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
