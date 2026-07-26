## Description: <br>
Helps developers, support teams, SaaS operators, and users rewrite vague error messages so they explain what failed, why it failed, and what to do next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to turn unclear application errors into actionable explanations, checklists, workflows, documentation, or implementation support. It is intended for troubleshooting and support scenarios where the reader needs to understand the failure, likely cause, and next step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Overbroad trigger wording may activate the skill for general productivity or debugging requests where error-message improvement is not intended. <br>
Mitigation: Narrow trigger text to explicit error-message improvement requests or disable implicit invocation where accidental activation would be disruptive. <br>
Risk: Generated messages or guidance may be misleading if the user provides incomplete error context. <br>
Mitigation: Ask only for missing information that materially changes the output, then validate the result against the stated failure, cause, next action, and audience. <br>
Risk: Proposed copy, code, commands, or configuration may be incorrect for the target system. <br>
Mitigation: Review proposed changes before use and test them against the relevant logs, product behavior, support policy, or deployment environment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-060415) <br>
- [Dify issue on unclear deployment error](https://github.com/langgenius/dify/issues/39161) <br>
- [Aether issue on practical verbose logging](https://github.com/CluvexStudio/Aether/issues/39) <br>
- [SegmentFault error-messages topic](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with optional checklists, workflow steps, code blocks, shell commands, or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should make assumptions, limits, validation steps, and any remaining follow-up work visible.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
