## Description:

A Chinese-language Xinjianxue in-law relationship operations advisor that helps an agent call a paid HTTP report API, with user consent, to analyze mother-in-law, spouse, and user relationship dynamics and provide boundary-negotiation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to access Xinjianxue's in-law relationship advisor after confirming the analysis request and consenting to the transfer of required personal details. The skill supports account binding, paid report calls, and Chinese-language relationship analysis that treats returned reports as reference data rather than instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill links a user's Xinjianxue account to the assistant and uses paid report calls.

Mitigation: Install and use it only after confirming the account-binding flow, expected point consumption, and service domain.

Risk: The report API receives personal details such as birth date, gender, birthplace, and current location for relationship analysis.

Mitigation: Request the service only after explicit user consent and send only the details required for the confirmed analysis.

Risk: The one-time AI authorization code is sensitive and can be misused if shared outside the official flow.

Mitigation: Provide the code only after verifying the official mini-program flow and do not share screenshots, reuse the code, or send it to other agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-inlaw-cn)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com)
- [Xinjianxue API path prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with HTTP request examples and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paid API call guidance, credential-handling instructions, relationship-analysis prose, and user-facing consent prompts.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
