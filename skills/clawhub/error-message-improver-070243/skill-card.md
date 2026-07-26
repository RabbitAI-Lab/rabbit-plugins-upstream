## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague errors into clearer messages that explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to rewrite vague failures into actionable troubleshooting guidance. It supports templates, checklists, workflows, analysis, code changes, and decision aids for clearer error communication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the skill to be selected for general debugging or support requests more often than intended. <br>
Mitigation: Narrow the trigger wording or disable implicit invocation when precise routing is required. <br>
Risk: Improved error text can be misleading if the agent lacks the underlying logs, environment details, or reproduction steps. <br>
Mitigation: State assumptions, request only material missing inputs, and validate the output against the user's success criteria before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver-070243) <br>
- [Requirement Plan](references/requirement-plan.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with templates, checklists, workflows, analysis, and optional code or command blocks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the user's error context, logs, constraints, and success criteria; no external service or credential requirement is declared.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
