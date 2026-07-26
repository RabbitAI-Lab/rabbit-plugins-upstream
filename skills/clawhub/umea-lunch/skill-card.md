## Description: <br>
Get today's lunch menus from restaurants in Umeå, using live data from umealunchguide.se. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simskii](https://clawhub.ai/user/simskii) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to retrieve and present current lunch menus for restaurants in Umeå, with optional date and restaurant filters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts umealunchguide.se to fetch live public lunch menu data. <br>
Mitigation: Deploy only where outbound access to umealunchguide.se is acceptable, and disclose that live lookup requires contacting that site. <br>
Risk: Live menu data may be unavailable, delayed, or different from restaurant offerings. <br>
Mitigation: Treat results as current third-party menu information and verify directly with the restaurant before relying on time-sensitive details. <br>


## Reference(s): <br>
- [Umeå Lunch on ClawHub](https://clawhub.ai/simskii/skills/umea-lunch) <br>
- [Umeå Lunch Guide](https://umealunchguide.se/) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON from the helper script, typically summarized as concise Markdown guidance for the user.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports date filtering, partial restaurant-name filtering, and restaurant listing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
