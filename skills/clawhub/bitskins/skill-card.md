## Description: <br>
Interacts with the BitSkins REST API V2 and WebSocket API for CS2/Dota 2 skin trading, including account management, market search, buying, selling, wallet operations, Steam trades, and real-time subscriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluesyparty-src](https://clawhub.ai/user/bluesyparty-src) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to search CS2/Dota 2 skins, check prices, and manage BitSkins account, marketplace, wallet, Steam inventory, and WebSocket workflows through authenticated API interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform real financial and account-security actions through BitSkins APIs. <br>
Mitigation: Use the narrowest available API key and require explicit confirmation with endpoint, item, amount, destination, and account-security impact before buy, sell, deposit, withdrawal, API-key, 2FA, trade-link, card, or account-status changes. <br>


## Reference(s): <br>
- [BitSkins API V2 Endpoint Reference](references/api-endpoints.md) <br>
- [BitSkins WebSocket API](references/websocket.md) <br>
- [BitSkins API Base URL](https://api.bitskins.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call BitSkins REST or WebSocket endpoints when the user provides an API key and confirms sensitive actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
