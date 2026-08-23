## Description:

Plan real-life events with the Chinese Tung Shing almanac by querying the 12Zodiacs.com API for auspicious dates, daily almanac details, zodiac clash, solar terms, hour pillars, and daily zodiac horoscopes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yonlandwu](https://clawhub.ai/user/yonlandwu)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and scheduling assistants use this skill to retrieve culturally contextual Chinese almanac guidance for events such as weddings, moving, launches, travel, contract signing, and daily zodiac readings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to 12Zodiacs.com and may reveal personal event timing or scheduling details.

Mitigation: Avoid entering sensitive personal events, medical scheduling details, or unnecessary API keys; install only when this third-party API use is acceptable.

Risk: Almanac results could be mistaken for professional medical, legal, or financial advice.

Mitigation: Use the output as cultural reference only and do not rely on it for clinical, legal, or financial decisions.

## Reference(s):

- [Tung Shing Almanac API Reference](references/api-reference.md)
- [Server-resolved GitHub Repository](https://github.com/yonlandwu/tung-shing-almanac-skill)
- [12Zodiacs Chinese Almanac API](https://www.12zodiacs.com/about-us/api/)
- [Tung Shing Web App](https://www.12zodiacs.com/tung-shing/)
- [Tung Shing Methodology](https://www.12zodiacs.com/tung-shing/methodology/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq; almanac data returned to users must include the required 12Zodiacs.com attribution.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
