## Description: <br>
WHOOP Central provides OAuth setup and Node.js scripts for fetching WHOOP sleep, recovery, strain, and workout data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[4xiomdev](https://clawhub.ai/user/4xiomdev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to connect a WHOOP account, inspect recent health metrics, and optionally export historical WHOOP records into local JSONL logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles WHOOP health data and stores OAuth credentials and tokens locally. <br>
Mitigation: Use a WHOOP developer app you control, keep ~/.clawdbot/whoop/credentials.json and token.json private, and revoke the WHOOP app or delete local token files when access is no longer needed. <br>
Risk: Bulk import can create a local archive of sensitive historical health records. <br>
Mitigation: Run historical import only when a local archive is intended, protect ~/clawd/health/logs/whoop, and delete those logs when they are no longer needed. <br>
Risk: OAuth scopes can grant broader read access than a task requires. <br>
Mitigation: Request only the WHOOP read scopes needed for the intended task and include offline access only when refresh tokens are required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/4xiomdev/skills/whoop-central) <br>
- [WHOOP Developer Portal](https://developer.whoop.com/) <br>
- [WHOOP API v2 base endpoint](https://api.prod.whoop.com/developer/v2) <br>
- [WHOOP OAuth authorization endpoint](https://api.prod.whoop.com/oauth/oauth2/auth) <br>
- [WHOOP OAuth token endpoint](https://api.prod.whoop.com/oauth/oauth2/token) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands; scripts emit terminal text, JSON, JSONL, and local JSONL log files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and, for the optional local HTTPS callback flow, openssl.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
