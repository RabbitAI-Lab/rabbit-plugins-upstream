## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague error messages into clearer explanations of what failed, why it failed, and what to do next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Application developers, support teams, SaaS operators, and users use this skill to draft, review, or improve error messages so troubleshooting guidance is actionable and easy to understand. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit triggers may cause the skill to appear during unrelated debugging or support requests. <br>
Mitigation: Invoke the skill explicitly when clearer error-message guidance is needed and ignore it when the task is unrelated. <br>
Risk: Generated troubleshooting text may omit important context from the user's environment. <br>
Mitigation: Check the final message against the stated failure, cause, next action, assumptions, and any remaining risks before using it. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-010622) <br>
- [Publisher Profile](https://clawhub.ai/user/kyro-ma) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, plain text, or code-oriented guidance depending on the user's request] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reusable checklists, workflows, assumptions, validation notes, and follow-up risks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
