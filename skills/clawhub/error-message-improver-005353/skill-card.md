## Description: <br>
Helps developers and support teams rewrite vague error messages so they explain what failed, why it happened, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to turn vague troubleshooting failures into actionable messages, checklists, workflows, or implementation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit triggers may cause the skill to be applied to general debugging or support requests where another skill would be more appropriate. <br>
Mitigation: Invoke the skill explicitly for error-message rewriting, or choose a more specific skill when the task is broader than improving user-facing error communication. <br>
Risk: Generated error-message guidance could omit important product or operational context supplied outside the prompt. <br>
Mitigation: Review the output against the actual failure mode, user audience, and support policy before publishing or deploying revised messages. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver-005353) <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown or plain text with optional code snippets, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should expose assumptions, limits, required inputs, and any remaining follow-up work.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
