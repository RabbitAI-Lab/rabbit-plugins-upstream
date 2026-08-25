## Description:

Helps developers, support teams, SaaS operators, and users rewrite vague errors into clearer messages that explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and end users use this skill to turn unclear error messages into actionable troubleshooting guidance. It produces tailored guidance, reusable checklists or workflows, and a short verification note for the requested situation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad debugging or support phrasing, including cases where the user did not explicitly ask to rewrite or structure an error message.

Mitigation: Use it when the user clearly wants to clarify, rewrite, or structure an error message, and confirm intent when a general debugging request could require deeper diagnosis.

Risk: Generated troubleshooting guidance or revised errors could still be incorrect or omit relevant context.

Mitigation: Review the output against the original failure, available logs, user-facing constraints, and the skill's stated validation criteria before using it in product or support material.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Publisher Profile](https://clawhub.ai/user/kyro-ma)
- [Wrangler issue: missing default export error behavior](https://github.com/cloudflare/workers-sdk/issues/15309)
- [Rotkeeper issue: better error messages and summaries](https://github.com/drawmeanelephant/rotkeeper/issues/237)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code, command, checklist, workflow, or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should expose assumptions, limits, validation notes, and any useful next steps.]

## Skill Version(s):

0.20260825.44155 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
