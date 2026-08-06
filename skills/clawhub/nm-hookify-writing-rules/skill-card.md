## Description: <br>
Creates behavioral rules in markdown to block dangerous commands or restrict AI behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Claude Code users use this skill to draft local Hookify rule files that warn on or block unwanted commands, file edits, prompts, or stop conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may invoke the skill during generic conversations about rules or safety. <br>
Mitigation: Use the skill when authoring Hookify guardrails and ignore or dismiss it when the task is unrelated to local rule files. <br>
Risk: Generated block rules may interrupt legitimate commands or workflows if patterns are too broad. <br>
Mitigation: Review generated rule files before saving them, test regex patterns, and prefer warnings before blocks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-hookify-writing-rules) <br>
- [Hookify plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/hookify) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with YAML frontmatter examples, regex snippets, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for local .claude/hookify.*.local.md rule files; generated rules should be reviewed before saving or enabling.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
