## Description:

Use Candor to organize personal financial records, review spending and investments, investigate savings, and keep budgets, goals, evidence, and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use this skill to examine financial records, plan budgets and goals, evaluate options, and keep authorized changes and follow-up in a Candor workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to an authenticated workspace exposes sensitive financial records.

Mitigation: Grant access only when comfortable with the Candor CLI reading the financial workspace; use Candor's secure sign-in flow rather than sharing credentials.

Risk: Budget and goal workflows can persist changes without confirmation of the exact saved plan.

Mitigation: Ask the agent to show the precise budget, goal, note, rule, or schedule and wait for confirmation before saving it.

## Reference(s):

- [Candor setup and access](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Evidence handling](references/evidence.md)

## Skill Output:

**Output Type(s):** [Financial analysis, Recommendations, Guidance]

**Output Format:** [Text or Markdown with supported figures and record links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save budgets, goals, and follow-up in an authenticated Candor workspace.]

## Skill Version(s):

0.1.219 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
