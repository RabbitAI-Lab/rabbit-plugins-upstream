## Description: <br>
Provides 2026 FIFA World Cup match schedules, results, standings, brackets, ELO-based match and champion predictions, team info, and team fortunes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pn1024](https://clawhub.ai/user/pn1024) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer World Cup 2026 schedule, results, standings, bracket, team information, match prediction, champion forecast, and team fortune questions through atomic APIs and card-based outputs. Predictions and fortunes are entertainment-oriented and should not be presented as guaranteed outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Predictions or team fortunes may be mistaken for reliable forecasts. <br>
Mitigation: Present prediction and fortune outputs as entertainment only, include the required disclaimer, and avoid guaranteeing accuracy. <br>
Risk: Routing and language behavior may be broader or more multilingual than some deployments expect. <br>
Mitigation: Review routing wording and locale expectations before deployment when strict sports scope or language behavior is required. <br>
Risk: World Cup results, team codes, or ELO ratings may become misleading if an agent fabricates or expands beyond the API data. <br>
Mitigation: Use the skill APIs as the source for results, team codes, and ELO values, and keep card data grounded in returned structured content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pn1024/skills/wc2026-prophet) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/pn1024) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration, guidance] <br>
**Output Format:** [Text responses with structured JSON content for card-based schedules, results, standings, brackets, team details, predictions, and fortunes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful API responses with bound components are intended to render as cards; prediction and fortune outputs require entertainment-only disclaimers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
