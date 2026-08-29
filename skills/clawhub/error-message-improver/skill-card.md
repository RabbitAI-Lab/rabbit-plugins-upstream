## Description:

Helps developers, support teams, SaaS operators, and users rewrite vague error messages so they explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and affected users use this skill to turn vague or unhelpful errors into actionable messages, checklists, workflows, code changes, or decision support. It is intended for troubleshooting and user-support contexts where the reader needs to understand the failure, likely cause, and next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms may cause the skill to activate for general debugging or support requests.

Mitigation: Prefer explicit invocation by name when predictable behavior matters.

Risk: Generated error-message guidance may misstate the cause or next action when the request lacks enough failure context.

Mitigation: State assumptions clearly and validate proposed messages against logs, known failure modes, or the user's success criteria before publishing.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tailored artifacts, reusable checklists, workflows, analysis, code changes, and verification notes.]

## Skill Version(s):

0.20260828.40337 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
