## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague errors into clearer messages that explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and affected users use this skill to design, rewrite, or review error messages so they state the failure, likely cause, next action, assumptions, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked too broadly for general debugging or support phrasing. <br>
Mitigation: Use it when the user explicitly asks to rewrite, explain, or design an error message with cause and next steps. <br>
Risk: Generated error-message guidance could be inaccurate if the failure context is incomplete. <br>
Mitigation: Require visible assumptions, limits, required inputs, and a verification note before using the message in support or product workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-140352) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Provide better error messages for invalid assignment shorthands](https://github.com/gleam-lang/gleam/issues/5915) <br>
- [error-messages](https://segmentfault.com/t/error-messages) <br>
- [Clojure 1.13 adds support for checked keys](https://news.ycombinator.com/item?id=48806658) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown prose with optional checklists, templates, code snippets, or configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a verification note, assumptions, limits, and follow-up work when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
