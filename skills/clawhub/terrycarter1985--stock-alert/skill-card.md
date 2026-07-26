## Description: <br>
Generates a daily stock price watchlist alert and sends it to a WhatsApp chat or group via the wacli (`wu`) CLI, using yfinance with a bundled CSV fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users who want scheduled or on-demand stock price notifications use this skill to generate a consolidated watchlist alert and optionally deliver it to a WhatsApp group. It is not intended for trading execution or real-time tick streaming. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags unresolved Feishu/Lark document-writing scope drift relative to the WhatsApp alert behavior. <br>
Mitigation: Treat Feishu/Lark publishing as out of scope unless the publisher documents and permission-scopes it; review docs/PERMISSIONS.md before enabling document writes. <br>
Risk: WhatsApp recipient limits are documented, but the security review states they are not enforced by the script. <br>
Mitigation: Verify the intended recipient before sending, run with --dry-run first, and use wacli only from an account approved for these notifications. <br>
Risk: Stock prices may come from yfinance or from a bundled local CSV fallback, so alerts can be delayed, unavailable, or stale. <br>
Mitigation: Use the output for notifications only and verify market data in an authoritative source before making financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/stock-alert) <br>
- [Publisher profile](https://clawhub.ai/user/terrycarter1985) <br>
- [Feishu/Lark permission configuration](docs/PERMISSIONS.md) <br>
- [wacli npm package](https://www.npmjs.com/package/@ibrahimwithi/wu-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text alert with command-line status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can run as a dry run without WhatsApp; actual sending requires a logged-in wacli (`wu`) CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
