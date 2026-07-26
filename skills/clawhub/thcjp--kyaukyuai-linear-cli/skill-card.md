## Description: <br>
Use the linear-cli agent-native runtime to read and mutate Linear from Claude Code, Codex, or other agent runtimes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to let agents inspect Linear state, preview changes, and apply issue, project, comment, webhook, label, and raw API updates through the local linear CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to change Linear issues, projects, comments, webhooks, labels, or raw API data. <br>
Mitigation: Use dry-run previews or explicit confirmation for write operations and avoid broad Linear invocations unless those changes are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/kyaukyuai-linear-cli) <br>
- [Linear GraphQL API](https://api.linear.app/graphql) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the local linear CLI; write operations should be previewed with dry-run or explicit confirmation when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
