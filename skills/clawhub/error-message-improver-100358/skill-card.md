## Description: <br>
Helps developers, support teams, and SaaS operators turn vague errors into clear messages that explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to rewrite or design clearer error messages, troubleshooting workflows, checklists, and implementation guidance. It is intended for situations where vague failures slow support or debugging and the user needs an actionable explanation and next step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broad trigger language may invoke the skill for general support or debugging tasks that are not primarily about error-message clarity. <br>
Mitigation: Confirm that the requested work is about improving or designing error messages before applying the skill's workflow. <br>
Risk: Users may paste secrets, credentials, or sensitive log data while seeking help with error messages. <br>
Mitigation: Redact tokens, passwords, keys, customer data, and other sensitive values before using logs or support details as inputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-100358) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Dify Agent Backend Issue](https://github.com/langgenius/dify/issues/39161) <br>
- [AWS VPC Controller Issue](https://github.com/VladAdochitei/aws-api-vpc-assignment-platform/issues/8) <br>
- [DBA Dash IOStats Issue](https://github.com/trimble-oss/dba-dash/issues/1981) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text, with code blocks or configuration snippets when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a reusable checklist, workflow, assumptions, validation note, and follow-up work.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
