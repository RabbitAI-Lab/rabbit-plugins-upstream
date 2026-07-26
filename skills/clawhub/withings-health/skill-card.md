## Description: <br>
Fetches health data from the Withings API including weight, body composition (fat, muscle, bone, water), activity, and sleep. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hisxo](https://clawhub.ai/user/hisxo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to retrieve Withings account health measurements, including weight history, body composition, activity, and sleep data. It is useful when a user asks to inspect or summarize health data from Withings devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads personal Withings health data. <br>
Mitigation: Install only when the user is comfortable granting Withings health-data access and revoke the Withings app authorization when access is no longer needed. <br>
Risk: OAuth client secrets, .env files, and local tokens can expose account access if shared. <br>
Mitigation: Keep WITHINGS_CLIENT_SECRET, any .env file, and tokens.json private; do not commit or share the authenticated skill directory, and delete tokens.json when deauthorizing the skill. <br>


## Reference(s): <br>
- [Withings Developer Portal](https://developer.withings.com/) <br>
- [ClawHub skill page](https://clawhub.ai/hisxo/skills/withings-health) <br>
- [Publisher profile](https://clawhub.ai/user/hisxo) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; wrapper commands return JSON arrays or status text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js plus WITHINGS_CLIENT_ID and WITHINGS_CLIENT_SECRET; authenticated use stores local OAuth tokens.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
