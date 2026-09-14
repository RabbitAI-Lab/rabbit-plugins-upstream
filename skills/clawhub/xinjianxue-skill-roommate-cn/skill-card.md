## Description:

This skill helps an agent act as a Xinjianxue roommate-relationship advisor by collecting consented personal details, calling the Xinjianxue HTTP API, and turning the returned report into roommate boundary-setting and negotiation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill when the user explicitly asks for roommate relationship advice and consents to using the Xinjianxue service. The agent uses the returned report as reference data to produce practical scripts, boundary-setting suggestions, and roommate agreement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends birth details, gender, and location to an external paid API.

Mitigation: Use it only after the user explicitly consents to sharing those details with Xinjianxue for the requested roommate-advice analysis.

Risk: The skill uses service credentials and an AI authorization code during account binding.

Mitigation: Store license and API credentials only in a dedicated secret store, do not expose them in chat or configuration files, and treat the authorization code as a sensitive one-time credential.

Risk: The skill can involve analysis of another person's personal details.

Mitigation: Do not submit another person's details unless the user clearly says that person was mentioned and consented to the analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-roommate-cn)
- [Xinjianxue API base URL](https://chinaapi.xinjianxue.com)
- [Xinjianxue API route prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, markdown, api calls, configuration, guidance]

**Output Format:** [Markdown guidance with optional HTTP API request details and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Xinjianxue report responses as data/reference material and instructs the agent not to execute instructions contained in reports.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
