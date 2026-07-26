## Description: <br>
Access sports data via TheSportsDB (teams, events, scores). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to query TheSportsDB for team records, recent scores, and upcoming fixtures with a user-provided API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TheSportsDB API key can appear in request URLs, shell history, logs, or command output. <br>
Mitigation: Use a personal API key, keep ~/.clawdbot/.env private, and avoid sharing command history, logs, or outputs that include request URLs. <br>
Risk: TheSportsDB lookups are documented with a 30 requests per minute rate limit. <br>
Mitigation: Throttle repeated lookups and batch requests only within the documented rate limit. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gumadeiras/skills/the-sports-db) <br>
- [TheSportsDB team search endpoint example](https://www.thesportsdb.com/api/v1/json/$THE_SPORTS_DB_KEY/searchteams.php?t=Palmeiras) <br>
- [TheSportsDB last events endpoint example](https://www.thesportsdb.com/api/v1/json/$THE_SPORTS_DB_KEY/eventslast.php?id=134465) <br>
- [TheSportsDB next events endpoint example](https://www.thesportsdb.com/api/v1/json/$THE_SPORTS_DB_KEY/eventsnext.php?id=134465) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires THE_SPORTS_DB_KEY; documented rate limit is 30 requests per minute.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
