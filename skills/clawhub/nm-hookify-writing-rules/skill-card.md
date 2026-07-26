## Description: <br>
Creates behavioral rules in markdown to block dangerous commands or restrict AI behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to draft persistent Hookify rules for Claude Code sessions, including guardrails that warn about or block risky commands, file edits, and prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent block rules can affect later agent commands until they are disabled or deleted. <br>
Mitigation: Review generated .claude/hookify.*.local.md files before relying on them, and disable or delete rules that are too broad. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-hookify-writing-rules) <br>
- [Hookify homepage](https://github.com/athola/claude-night-market/tree/master/plugins/hookify) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with YAML frontmatter examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance and rule-file examples for .claude/hookify.*.local.md files.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
