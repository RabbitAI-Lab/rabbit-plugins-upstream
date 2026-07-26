## Description: <br>
Fetches Withings health data for multiple family members, including weight, body composition, activity, and sleep metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use this skill to authenticate family members with Withings and retrieve health measurements such as weight, body composition, daily activity, and sleep data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill retrieves family health data and stores OAuth tokens locally. <br>
Mitigation: Treat token files as sensitive credentials, keep the skill directory private, and delete token files or revoke the Withings app when access is no longer needed. <br>
Risk: Adding a family member's Withings account without clear permission can expose private health history. <br>
Mitigation: Install and use the skill only for family members who have agreed to that access, and use explicit user IDs plus date or result limits when requesting history. <br>


## Reference(s): <br>
- [ClawHub Withings Family skill page](https://clawhub.ai/odrobnik/skills/withings-family) <br>
- [Withings Developer Portal](https://developer.withings.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, WITHINGS_CLIENT_ID, WITHINGS_CLIENT_SECRET, and per-user OAuth token files.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
