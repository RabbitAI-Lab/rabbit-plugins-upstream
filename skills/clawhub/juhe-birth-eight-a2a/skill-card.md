## Description:

Provides a paid Juhe-powered birth-date astrology lookup that returns eight-character, five-element, lunar calendar, zodiac, stem-branch, and constellation information from a confirmed Gregorian birth date and hour.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to purchase and retrieve entertainment-oriented birth-date astrology details, including BaZi, five-element, lunar calendar, zodiac, stem-branch, and constellation information. The skill is intended for queries where the user provides a specific Gregorian birth date and birth hour.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's birth date and birth hour to an external Juhe API for each paid lookup.

Mitigation: Require explicit user confirmation before payment and transmit only the year, month, day, and hour needed for the query.

Risk: Users may over-rely on entertainment astrology output for consequential decisions.

Mitigation: Present results as entertainment reference material and avoid medical, financial, legal, career, or relationship determinations.

Risk: The paid flow can create unintended charges if the user does not understand the Alipay payment prompt.

Mitigation: Show the product, amount, order information, payment channels, and QR payment step before completing payment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-birth-eight-a2a)
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns structured tables after payment; uses only the confirmed year, month, day, and hour for each query.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
