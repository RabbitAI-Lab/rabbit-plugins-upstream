## Description: <br>
Helps agents extract structured business data from Google Maps search results through BrowserAct using user-provided search parameters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to collect business listings, addresses, ratings, review counts, and related place details from Google Maps search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Maps search terms and task parameters may be sent to BrowserAct. <br>
Mitigation: Confirm runs that could reveal sensitive business plans, lead lists, or customer targets before execution. <br>
Risk: The skill may ask users to provide a BrowserAct API key in chat. <br>
Mitigation: Set BROWSERACT_API_KEY through the environment or a secure secret store instead of pasting credentials into chat. <br>
Risk: The security scan verdict is suspicious due to proactive third-party API use and credential handling guidance. <br>
Mitigation: Review the skill before installing and only use it when BrowserAct data sharing is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phheng/skills/google-maps-search-api) <br>
- [BrowserAct integrations console](https://www.browseract.com/reception/integrations) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text business records printed from a Python command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BROWSERACT_API_KEY plus keywords, language, country, and result limit inputs; retries failed non-authorization runs once.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
