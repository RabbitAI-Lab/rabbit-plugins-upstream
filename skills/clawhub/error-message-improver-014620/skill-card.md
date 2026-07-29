## Description: <br>
Helps developers, support teams, and SaaS operators turn vague errors into clear messages that explain what failed, why it failed, and what to do next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and end users use this skill to rewrite or design error messages, troubleshooting workflows, checklists, and implementation support that make failures actionable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be selected for broad debugging or support prompts because its triggers and implicit invocation policy are broad. <br>
Mitigation: Review activation behavior before deployment and tighten trigger wording if predictable routing is required. <br>
Risk: Generated error-message guidance could be incorrect or omit context-specific troubleshooting constraints. <br>
Mitigation: Validate proposed messages against the affected product behavior, support policy, and the user's stated success criteria before release. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-014620) <br>
- [Add comprehensive form validation error messages with resolution guidance](https://github.com/StellarLock/StellarLock/issues/164) <br>
- [error-messages](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code, command, checklist, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include visible assumptions, limits, validation notes, and next steps when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
