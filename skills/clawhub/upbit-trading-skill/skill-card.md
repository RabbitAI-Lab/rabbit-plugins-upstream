## Description: <br>
Upbit real-time trading bot for GLM AI analysis, technical indicators, and automated trading signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smeuse-dev](https://clawhub.ai/user/smeuse-dev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and crypto traders use this skill to monitor Upbit positions, calculate common technical indicators, request GLM-based market analysis, and generate trading-related events or signals. It requires careful credential handling and should be reviewed before live exchange use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests Upbit exchange credentials for account access and trading-related monitoring. <br>
Mitigation: Use a dedicated least-privilege Upbit API key, prefer read-only permissions unless live trading is intended, and never grant withdrawal permission. <br>
Risk: The runtime invokes an external ../zai/ask.sh script for GLM analysis. <br>
Mitigation: Inspect, pin, replace, or remove that dependency before running the skill in any trusted environment. <br>
Risk: Security evidence flags under-disclosed behavior around actual order execution and Telegram behavior. <br>
Mitigation: Treat the release as a monitoring and signal-generation tool until the publisher documents and ships confirmed order execution and notification behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smeuse-dev/skills/upbit-trading-skill) <br>
- [Publisher profile](https://clawhub.ai/user/smeuse-dev) <br>
- [Upbit Open API management](https://upbit.com/mypage/open_api_management) <br>
- [Upbit accounts API endpoint](https://api.upbit.com/v1/accounts) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript scripts, shell commands, console text, and JSON event files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local JSON files for positions and events; runtime behavior depends on Upbit credentials and the external GLM shell-script dependency.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
