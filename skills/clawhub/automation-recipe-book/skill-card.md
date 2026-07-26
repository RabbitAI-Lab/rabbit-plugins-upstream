## Description: <br>
Automation Recipe Book helps agents generate, validate, debug, share, import, schedule, and manage automation recipes for personal, team, and enterprise workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operations teams use this skill to create and manage automation recipes for approvals, notifications, reporting, data processing, content operations, scheduling, debugging, and rollback workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide command execution and recipe actions that save, import, install, schedule, enable, or run automation recipes. <br>
Mitigation: Require preview and explicit approval before any recipe is saved, imported, installed, scheduled, enabled, or executed. <br>
Risk: Community recipes or recipes that post content, touch business systems, send notifications, or call other skills may have side effects or trust-boundary issues. <br>
Mitigation: Review recipe source, dependencies, destinations, and permissions before enabling or running them. <br>
Risk: Generated recipes may contain incorrect triggers, actions, retry behavior, or integration assumptions. <br>
Mitigation: Validate generated recipes and run dry runs with mock input before production use. <br>


## Reference(s): <br>
- [ClawHub skill page: Automation Recipe Book](https://clawhub.ai/thcjp/skills/automation-recipe-book) <br>
- [ClawHub publisher profile: thcjp](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce automation recipe definitions, validation results, execution traces, flowchart instructions, import/export commands, version diffs, and rollback commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
