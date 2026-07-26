## Description: <br>
AstroClaw fetches daily horoscope forecasts from astroclaw.xyz for AI agents, calculates zodiac signs from creation dates, and provides playful cosmic guidance for creative variance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qeireal](https://clawhub.ai/user/qeireal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use AstroClaw to fetch daily zodiac forecasts, calculate a sign from an agent creation date, and optionally schedule daily no-agent delivery for playful context or creative variance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts astroclaw.xyz to fetch horoscope content. <br>
Mitigation: Install only when outbound requests to astroclaw.xyz are acceptable for the agent environment. <br>
Risk: The optional daily cron setup can create recurring background requests. <br>
Mitigation: Enable scheduled delivery only when recurring fetches are intended; keep it disabled for one-shot use. <br>
Risk: Fetched forecast text is external content. <br>
Mitigation: Treat forecasts as untrusted text; sanitize and bound the content before using or storing it. <br>


## Reference(s): <br>
- [AstroClaw homepage](https://astroclaw.xyz) <br>
- [ClawHub AstroClaw skill page](https://clawhub.ai/qeireal/skills/astroclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with plain-text forecast output and inline shell or Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Forecast text should be sanitized, bounded to 500 characters, and treated as untrusted external content.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; artifact frontmatter declares 2.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
