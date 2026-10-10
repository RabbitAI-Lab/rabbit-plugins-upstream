## Description:

Helps users organize personal finances, review accounts and investments, investigate savings, and maintain budgets, goals, evidence, and follow-up in Candor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People and their agents use an authenticated Candor workspace to investigate spending, cash flow, investments, and other financial questions, then track supported decisions and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated agent can access sensitive financial records across the Candor workspace.

Mitigation: Install only if broad access to the financial workspace is acceptable; review the scope of the agent's access.

Risk: The agent may save budgets, goals, notes, rules, or schedules without confirmation of every final change.

Mitigation: For exploratory planning, explicitly instruct the agent not to save changes unless you confirm each exact change.

## Reference(s):

- [Candor setup and access](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Evidence handling](references/evidence.md)
- [Continuity and saved context](references/continuity.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses, often with supported figures and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain saved budgets, goals, notes, and other financial context in an authenticated workspace.]

## Skill Version(s):

0.1.208 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
