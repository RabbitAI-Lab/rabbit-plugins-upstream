## Description:

Helps an agent discover and call paid APIs using the user's prepaid taskfuel.ai balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving external users and developers can find, price, and call paid search, market-data, and other APIs using the user's taskfuel.ai account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may spend the user's prepaid balance on small paid calls without per-call approval.

Mitigation: Set a task budget up front, quote calls before paying, cap each call at its quoted price, and require explicit approval for larger spends.

Risk: The installation command downloads and executes a remote installer.

Mitigation: Review the installer before running it.

Risk: Requests to paid endpoints or feedback reports may disclose sensitive information.

Mitigation: Avoid sending secrets or sensitive personal data through paid endpoints or feedback reports.

Risk: Retrying a timed-out paid call may charge for the same work twice.

Mitigation: Check the existing call's result or balance before attempting another paid call.

## Reference(s):

- [taskfuel ClawHub skill page](https://clawhub.ai/taskfuel.ai/skills/taskfuel)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell commands and API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls draw from the user's prepaid balance; report total spend per task.]

## Skill Version(s):

0.5.2 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
