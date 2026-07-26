## Description: <br>
WHOOP Tracker helps agents access WHOOP fitness tracker data via API, including recovery scores, sleep metrics, workout stats, daily strain, and body measurements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ijaack](https://clawhub.ai/user/ijaack) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to set up OAuth access to their WHOOP account and retrieve recovery, sleep, workout, daily strain, profile, and body measurement data for fitness tracking and trend analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive WHOOP fitness, sleep, recovery, body measurement, name, and email data after OAuth authorization. <br>
Mitigation: Install and authorize it only when that data access is acceptable, and grant only the WHOOP scopes needed for the intended use. <br>
Risk: WHOOP OAuth credentials and tokens are stored locally under ~/.whoop. <br>
Mitigation: Keep credentials.json and token.json private, avoid shared machines, retain restrictive file permissions, and revoke the WHOOP OAuth grant when access is no longer needed. <br>
Risk: CLI output may include personal health and profile details. <br>
Mitigation: Review command output before sharing, logging, or pasting it into other tools. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ijaack/skills/whoop-tracker) <br>
- [WHOOP OAuth setup](references/oauth.md) <br>
- [WHOOP API reference](references/api-reference.md) <br>
- [WHOOP developer portal](https://developer.whoop.com) <br>
- [WHOOP API base URL](https://api.prod.whoop.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text or JSON from Python CLI scripts, with Markdown setup guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided WHOOP OAuth credentials and tokens stored under ~/.whoop, plus network access to the WHOOP API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
