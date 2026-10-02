## Description:

AI KEY·这生意靠谁 helps owner-operators identify who can unilaterally change the rules, prices, access, supply, staffing, or payment flow of their business and requires switching cost and switching time for every high-risk dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External business owners and operators use this skill to run a dependency checkup across channels, premises and licences, key people, suppliers, and payment rails. It produces a practical risk report focused on who can change the business without negotiation and what it would cost to switch away.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may elicit sensitive business dependency details, including suppliers, platforms, leases, licences, key staff, and payment channels.

Mitigation: Use it only where sharing those details with the agent is acceptable, and review memory behavior before entering sensitive facts.

Risk: Scoped memory can retain lessons and switching-cost facts for later calibration.

Mitigation: Review, limit, or clear stored memory according to the deployment's data-handling policy when business dependency details are sensitive.

## Reference(s):

- [理论底座 · 依赖](references/理论底座.md)
- [AI KEY README upgrade note](https://github.com/iamzifei/aikey#老用户升级zmm-已改名为-ai-key)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-dependency)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown dependency checkup report with tables and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dependency categories, severity levels, switching cost and time, backup-plan actions, expiration calendar entries, and unassessed items.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
