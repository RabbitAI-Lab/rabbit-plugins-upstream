## Description:

Helps users review their financial records, organize spending, plan budgets and goals, investigate savings opportunities, and track supporting evidence and follow-up in Candor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People using a signed-in Candor workspace can ask an agent to investigate their accounts and spending, review financial priorities, and maintain budgets, goals, and related records within their instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated workspace can expose sensitive personal financial records.

Mitigation: Limit access to the user's stated task and avoid including sensitive details in feedback or unnecessary outputs.

Risk: The agent can save budgets, goals, and other planning changes without a separate exact-draft confirmation.

Mitigation: Give narrow instructions; request the exact proposed change before saving when desired, and review reported saved changes.

## Reference(s):

- [Candor setup and documentation](https://candor.money/START.md)
- [Candor Finance release](https://clawhub.ai/candor/skills/candor-finance)
- [Setup and access](references/setup.md)
- [Evidence handling](references/evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite financial records, distinguish estimates from verified facts, and report saved changes.]

## Skill Version(s):

0.1.210 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
