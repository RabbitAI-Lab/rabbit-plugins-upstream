## Description: <br>
Creates Shieldz crypto payment links or reusable tip jars for explicitly confirmed user-provided wallets, and reads payment status from Shieldz. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[denizyanbollu](https://clawhub.ai/user/denizyanbollu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill through an agent to create confirmed Shieldz payment links or tip jars for their own wallet and to check payment status with a provided manage token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a payment link or tip jar sends wallet, chain, asset, amount, memo or title, and optional email data to Shieldz. <br>
Mitigation: Restate the exact data to be sent and proceed only after the user explicitly confirms the external call. <br>
Risk: A manage URL or manage token can expose payment totals and settings to anyone who holds it. <br>
Mitigation: Treat manage URLs and manage tokens as private credentials and do not share them publicly or write them to logs. <br>
Risk: An email address is personal data sent to a third-party service. <br>
Mitigation: Omit email by default and include it only when the user explicitly provides the address and agrees to send it. <br>


## Reference(s): <br>
- [Shieldz Payment Links API](https://shieldz.cash/api/v1/links) <br>
- [Shieldz Tip Jars API](https://shieldz.cash/api/v1/tip-jars) <br>
- [Shieldz MCP Server](https://shieldz.cash/mcp) <br>
- [Shieldz Skill Page](https://clawhub.ai/denizyanbollu/skills/shieldz) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown or plain text with Shieldz URLs, status summaries, and optional curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [External creation calls require explicit user confirmation; manage URLs and manage tokens are private capability credentials.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
