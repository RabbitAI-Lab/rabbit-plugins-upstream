## Description: <br>
Detects workflow failures and inefficient patterns then files GitHub issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to monitor agent workflow executions for failures, timeouts, retry loops, context pressure, and inefficient tool usage, then prepare structured issue reports for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad workflow-related trigger wording may activate the skill during ordinary workflow discussions. <br>
Mitigation: Review trigger wording before installation and narrow activation if the deployment needs stricter scope. <br>
Risk: Automated issue drafting or creation can produce noisy, duplicate, or misleading workflow issues if findings are not reviewed. <br>
Mitigation: Keep approval required, check for duplicate issues, rate-limit issue creation, and review evidence before filing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-workflow-monitor) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, issue templates, YAML configuration examples, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose GitHub or GitLab issue creation after duplicate checks and user approval.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
