## Description:

Securely read a user's own XUNBEE email or SMS inbox, filter OTP messages, and extract verification codes with a scoped API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zeraswang](https://clawhub.ai/user/zeraswang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query their own authorized XUNBEE email or SMS inbox and retrieve the newest matching OTP or verification code. It is suited to authorized account access, support, and testing workflows where the agent should return only the requested message or code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive inbox messages, OTPs, or verification codes from the user's XUNBEE account.

Mitigation: Use it only for the user's own authorized inbox, request narrow filters, and return only the requested code or message.

Risk: A leaked XUNBEE API key could allow unauthorized read access to short-lived messages.

Mitigation: Use a read-only, expiring messages:read key and store it only in private skill settings or an environment variable.

Risk: Changing XUNBEE_BASE_URL could send requests and bearer tokens to an untrusted service.

Mitigation: Keep the default HTTPS endpoint unless the alternate server is controlled or explicitly trusted by the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zeraswang/skills/xunbee-message-inbox)
- [Server-Resolved GitHub Source](https://github.com/Zeraswang/xunbee-message-inbox)
- [XUNBEE Website](https://xunbee.akuwan.cn)
- [XUNBEE User Console](https://cc.akuwan.cn/admin/console/login)
- [XUNBEE API Key Management](https://cc.akuwan.cn/admin/console/notifications)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands; commands may return plain text verification codes or JSON message lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires XUNBEE_API_KEY; supports channel, source_ref, keyword, limit, wait, and trusted HTTPS base URL parameters.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
