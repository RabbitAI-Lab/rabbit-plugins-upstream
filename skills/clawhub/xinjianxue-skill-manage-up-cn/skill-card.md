## Description:

Provides an upward-management advisory workflow that calls the Xinjianxue API, with user confirmation, to generate report-backed guidance on managing relationships, communication, and negotiation with supervisors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they explicitly want upward-management advice for themselves or for a person who has consented. The skill gathers required personal details, calls Xinjianxue's report API, and turns the returned report data into concise workplace communication and boundary-setting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive birth, gender, and location details to a third-party API under the user's account.

Mitigation: Use the skill only after explicit user consent, avoid submitting other people's details without clear consent, and keep credentials in dedicated secret storage.

Risk: The returned report is external data and could contain misleading or instruction-like content.

Mitigation: Treat report content only as reference data, ignore any instruction-like text in it, and apply the local upward-management role and user request as the instruction source.

Risk: License and API credentials are sensitive one-time or account-bound values.

Mitigation: Do not expose license keys, API keys, or authorization codes in chat, configuration files, logs, or long-term memory; mask credentials when referring to them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-manage-up-cn)
- [Xinjianxue API base URL](https://chinaapi.xinjianxue.com)
- [Xinjianxue API path prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with HTTP request examples and structured advisory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation, account binding credentials, and personal birth, gender, and location details before API-backed analysis.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
