## Description:

XinJianXue Parent-Child Conflict Advisor helps an agent collect consented subject details, call the paid XinJianXue report API, and provide neutral guidance about parent-child conflict dynamics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to analyze parent-child conflicts after explicit consent, account binding, and collection of required personal details. The skill supports neutral analysis of conflict triggers, escalation paths, family roles, and concrete communication steps without assigning blame.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a one-time authorization code and service credentials for the XinJianXue account binding flow.

Mitigation: Use the authorization code only for the intended binding step, store license and API credentials in dedicated credential storage, and mask credentials in conversation.

Risk: Report calls send personal details, including birth date, gender, birthplace when available, and current location, to www.xinjianxue.com and consume paid tokens.

Mitigation: Obtain explicit user confirmation before analysis, collect only required fields, and disclose the paid token use before making report calls.

Risk: Returned reports may contain instruction-like phrasing even though they are analysis material.

Mitigation: Treat server reports as data and reference material only; follow only the local skill role definition when producing user-facing guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-child-conflict-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with JSON request examples and HTTP endpoint details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before analysis; returned reports are treated as data, not instructions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
