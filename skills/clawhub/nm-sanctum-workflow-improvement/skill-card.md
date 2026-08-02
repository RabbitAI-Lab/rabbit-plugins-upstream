## Description: <br>
Evaluates and improves skills, agents, commands, and hooks after a workflow slice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill after a slow, confusing, repetitive, or fragile workflow slice to identify friction and improve the involved skills, agents, commands, and hooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to inspect workflow history and logs, which may expose private or sensitive repository context. <br>
Mitigation: Review the skill before installation and avoid using it on private or sensitive repositories unless external-sharing steps are disabled. <br>
Risk: The workflow includes persistent repository changes such as editing workflow files and creating commits. <br>
Mitigation: Require explicit review and approval before applying file edits or committing changes. <br>
Risk: The workflow can create GitHub issues or post public Discussions entries. <br>
Mitigation: Require manual confirmation before any GitHub issue creation or public Discussions post. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-workflow-improvement) <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Auto issue creation module](modules/auto-issue-creation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured checklists, inline shell commands, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose workflow-asset edits and GitHub issue or discussion actions; require manual confirmation before external publication or persistent repository changes.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
