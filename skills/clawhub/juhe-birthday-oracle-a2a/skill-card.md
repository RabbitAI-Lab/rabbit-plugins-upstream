## Description:

This third-party paid ClawHub skill queries Juhe's birthday-oracle service for a specified date and returns birthday book, birthday code, birthday flower, personality, fortune, career, health, tarot, and related entertainment readings after Alipay confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and consumer agents use this skill to request entertainment-oriented birthday readings for a specific date through a disclosed paid Alipay flow. It is intended for birthday-book, birthday-code, birthday-flower, and date-specific reading requests, not general horoscope or life-decision guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may not realize the lookup is paid entertainment content.

Mitigation: Ask for explicit confirmation, show actual payment details through Alipay, and present results as entertainment rather than decision guidance.

Risk: The query sends the selected date to Juhe's service.

Mitigation: Send only the date chosen for the lookup and stop if unrelated personal information or payment outside the documented Alipay flow is requested.

Risk: Payment handling could be confusing if order details are incomplete.

Mitigation: Display the item name, amount, transaction number, user order number, and available Alipay payment channels before payment completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-birthday-oracle-a2a)
- [Juhe A2A birthday query endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Structured Markdown with payment-confirmation guidance and an HTTP POST command template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-supplied date and Alipay payment confirmation; returned readings are entertainment content and should not be treated as factual predictions.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
