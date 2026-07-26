## Description: <br>
Automates live football odds analysis and value-betting workflows for Asian Handicap and Over/Under markets using The Odds API and Singbet-related betting portals. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[hga030888-blip](https://clawhub.ai/user/hga030888-blip) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and betting-system evaluators can use this skill to inspect an agent workflow that fetches live football odds, evaluates betting opportunities, and records or simulates wager execution. Because the artifact targets gambling workflows, any real-money use requires separate legal, account, credential, and per-bet approval controls. <br>

### Deployment Geography for Use: <br>
Global, subject to local gambling laws and platform availability <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed for automated gambling decisions and may place or simulate wagers without explicit per-bet approval. <br>
Mitigation: Require explicit human confirmation before every wager and use the skill only where gambling activity is lawful and authorized. <br>
Risk: The betting function can report a successful bet even though the artifact contains placeholder execution logic. <br>
Mitigation: Treat any success message as an internal log entry unless independently confirmed by the betting platform. <br>
Risk: The artifact includes a hard-coded API key and expects betting credentials in configuration. <br>
Mitigation: Replace or remove bundled secrets, store credentials outside plain configuration, and rotate exposed keys before use. <br>


## Reference(s): <br>
- [The Odds API](https://the-odds-api.com/) <br>
- [ClawHub skill page](https://clawhub.ai/hga030888-blip/skills/football-automated-value-betting) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python tool functions and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes live-odds retrieval, betting-action text responses, betting statistics, fixed-stake configuration, and daily bet-limit settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact configuration) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
