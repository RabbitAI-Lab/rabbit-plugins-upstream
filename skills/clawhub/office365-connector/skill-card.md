## Description: <br>
Office 365 / Outlook connector for email, calendar, and contacts using resilient OAuth authentication, with multi-account support for managing multiple Microsoft 365 identities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tirandagan](https://clawhub.ai/user/tirandagan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent read, search, send, and manage Microsoft 365 email, calendar, and contact data across one or more user accounts. It is suited to workflows that need Microsoft Graph access with OAuth device-code authentication and per-account token isolation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad Microsoft 365 access, including email, calendar, contacts, send-mail capability, and offline token refresh. <br>
Mitigation: Use the smallest Azure delegated permission set that supports the intended workflow, review consent before use, and revoke Microsoft app consent when the skill is no longer needed. <br>
Risk: The skill stores client secrets and per-account OAuth tokens on disk, and token-printing commands can expose credentials if used carelessly. <br>
Mitigation: Protect ~/.openclaw/auth as a password store, avoid running token-printing commands in shared terminals, keep file permissions restricted, and rotate or remove secrets for unused accounts. <br>


## Reference(s): <br>
- [Multi-account usage guide](MULTI-ACCOUNT.md) <br>
- [Azure App Registration setup guide](references/setup-guide.md) <br>
- [Microsoft Graph permissions reference](references/permissions.md) <br>
- [Microsoft Graph API documentation](https://learn.microsoft.com/en-us/graph/api/overview) <br>
- [Microsoft Graph authentication concepts](https://learn.microsoft.com/en-us/graph/auth/auth-concepts) <br>
- [Microsoft Graph throttling guidance](https://learn.microsoft.com/en-us/graph/throttling) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, shell commands, and text or JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include Microsoft 365 mailbox, calendar, and contact data for the selected account; write operations can send email or modify calendar items when the configured permissions allow it.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and CHANGELOG.md, released 2026-02-09) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
