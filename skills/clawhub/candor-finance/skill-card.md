## Description:

Helps agents use Candor to organize personal finances, review investments, investigate savings, and keep approved plans, evidence, and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People with an authenticated Candor workspace can ask their assistant to analyze accounts and spending, assess financial options, organize records, and track approved goals and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated agent may access sensitive account, transaction, benefits, insurance, retirement, and tax-adjacent information.

Mitigation: Install only if comfortable granting this level of workspace access; keep reported findings scoped to the user's task.

Risk: The agent can make internal financial-record changes or schedule future checks.

Mitigation: Require user authorization for changes and monitoring, honor narrower instructions, and verify completed changes.

Risk: Financial conclusions or recommendations may be incomplete or mistaken.

Mitigation: Ground claims in current records, disclose uncertainty, and verify material rates and terms from authoritative sources when needed.

## Reference(s):

- [Candor setup and documentation](https://candor.money/START.md)
- [Candor Finance on ClawHub](https://clawhub.ai/candor/skills/candor-finance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown with evidence-backed financial analysis and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include record links, uncertainty, proposed next steps, and authorized changes or scheduled checks in Candor.]

## Skill Version(s):

0.1.155 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
