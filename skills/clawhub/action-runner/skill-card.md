## Description: <br>
Action Runner turns skill recommendations into dry-run, risk-classified action plans and, after approval, executes scoped actions through connected tools while logging what was done. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to turn recommendations into scoped GitHub, Linear, Slack, Notion, email, or calendar actions, with a dry-run plan and risk gating before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approved actions can change external systems or send outbound messages. <br>
Mitigation: Review the dry-run carefully, keep target scopes narrow, and require explicit approval before execution. <br>
Risk: High-risk actions such as posting, sending, deleting, merging, deploying, or charging can have visible or destructive effects. <br>
Mitigation: Confirm red or high-risk actions one by one and execute only the actions that were approved. <br>
Risk: Acting outside the requested repo, channel, project, or account could create unintended changes. <br>
Mitigation: Limit execution to named targets and use only the connected action tools selected for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/action-runner) <br>
- [Action Runner homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/action-runner.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with JSON action plans, tabular previews, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes proposed actions, per-action risk levels, approval gate results, executed action links or IDs, and a record of what was logged.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
