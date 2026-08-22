## Description:

Retrieves translated Zhihuiya patent description or specification text in Chinese, English, or Japanese from patent IDs or publication numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve translated patent specification text for one or more known patent identifiers. It is intended for patent description translation lookup, not patent search, claims analysis, legal-status review, citation analysis, or portfolio analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent identifiers and returned patent descriptions are sent to LinkFox/Zhihuiya and full responses are retained in local LinkFox session data files.

Mitigation: Use the skill only for data that may be shared with LinkFox/Zhihuiya, review local response files for retention needs, and avoid inline output for very large or sensitive responses unless necessary.

Risk: The skill requires a LinkFox API key and can guide account registration through SMS-code login.

Mitigation: Obtain and store credentials through the first-party site or a secret manager, and avoid sharing SMS codes with an agent when possible.

Risk: Billing and payment flows may create paid orders or payment QR codes.

Mitigation: Require explicit user confirmation before listing paid plans, creating an order, or presenting a payment QR flow.

Risk: Feedback reporting could include sensitive task details if used carelessly.

Mitigation: Do not automatically report feedback containing patent text, credentials, billing details, or other sensitive context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data-translated)
- [linkfox-ai publisher profile](https://clawhub.ai/user/linkfox-ai)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to local LinkFox session data files; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
