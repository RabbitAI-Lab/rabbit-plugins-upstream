## Description:

Helps developers, support teams, SaaS operators, and users turn vague errors into clear explanations of what failed, why it failed, and what to do next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and end users use this skill to produce practical rewrites, workflows, checklists, analysis, code changes, or decision support that make error messages actionable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad debugging or support-related trigger wording may activate the skill for unrelated tasks.

Mitigation: Review invocation behavior before deployment and tighten trigger wording if accidental activation is observed.

Risk: Generated error-message rewrites or troubleshooting guidance could be incomplete or misleading if the user provides limited context.

Mitigation: Check outputs against the stated failure, cause, next action, and known product constraints before using them in customer-facing support or application text.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown or plain text, with code or configuration snippets when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, checklists, workflows, or next steps tailored to the user's error-message task.]

## Skill Version(s):

0.20260905.61641 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
