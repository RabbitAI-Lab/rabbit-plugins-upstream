## Description: <br>
Browse, search, post, and moderate Reddit; read-only actions work without authentication, while posting and moderation require OAuth setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theglove44](https://clawhub.ai/user/theglove44) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent browse or search Reddit, inspect comments, submit posts or replies, and perform moderation actions after OAuth setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit posts, reply, and perform moderation actions against live Reddit communities. <br>
Mitigation: Require explicit human approval before submit, reply, remove, approve, sticky, lock, or unlock commands. <br>
Risk: OAuth access persists in ~/.reddit-token.json and can be reused until revoked or deleted. <br>
Mitigation: Use a dedicated low-privilege Reddit app and account, grant only needed scopes, protect the token file, and delete it when access is no longer needed. <br>
Risk: Environment variables may contain Reddit app credentials. <br>
Mitigation: Avoid placing Reddit passwords in shared environments or logs, and rotate credentials if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub Reddit Skill](https://clawhub.ai/theglove44/skills/reddit) <br>
- [Publisher Profile](https://clawhub.ai/user/theglove44) <br>
- [README](README.md) <br>
- [Reddit App Preferences](https://www.reddit.com/prefs/apps) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js; read-only commands can use Reddit public JSON endpoints, and write or moderation commands require OAuth credentials and a stored refresh token.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
