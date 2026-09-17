## Description:

This skill preserves legacy Marriott hotel tool entry points and returns Chinese guidance directing users to general hotel search or price-comparison skills because Marriott-specific data is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users can invoke legacy Marriott hotel search, detail, or package tools to receive guidance on using general hotel search, price comparison, Tuniu, or Tongcheng travel skills for Marriott-family hotel queries. The skill does not perform Marriott-specific search, booking, persistence, or external data access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect this skill to perform Marriott-specific hotel search or booking.

Mitigation: Present it as a compatibility redirect and route live hotel lookup or booking needs to general hotel-search or price-comparison skills.

Risk: The skill output is Chinese-only and may be inconvenient for users who do not read Chinese.

Mitigation: Use it in Chinese-language workflows or pair it with translation when serving other audiences.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/marriott-hotel-booking)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Plain text Chinese service notice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The retained search, detail, and packages tools return the same compatibility guidance rather than live hotel data.]

## Skill Version(s):

1.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
