## Description:

Helps people use Candor to examine personal finances, organize spending, plan budgets and goals, and keep supporting evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

People managing their finances use this skill to investigate account activity and spending, review investments and possible savings, and maintain budgets, goals, and follow-up in Candor. It requires an authenticated Candor workspace and compatible Candor tools or CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read sensitive financial records and potentially unnecessary health, payroll, or benefits information.

Mitigation: Review access before installation and share sensitive documents only when the task requires them.

Risk: Budgets, goals, notes, imports, or scheduled follow-ups may be saved with less explicit pre-save confirmation than expected.

Mitigation: Ask the agent to show exact proposed changes before saving them and verify the saved result.

## Reference(s):

- [Candor setup and documentation](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)
- [Evidence handling](references/evidence.md)
- [Setup and access](references/setup.md)
- [Scheduled work](references/monitoring.md)

## Skill Output:

**Output Type(s):** [Financial analysis, Guidance, Markdown, Shell commands]

**Output Format:** [Text and Markdown with task-specific Candor commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save authorized budgets, goals, notes, and follow-up in Candor.]

## Skill Version(s):

0.1.212 (source: ClawHub release metadata; bundled skill metadata lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
