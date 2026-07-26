## Description: <br>
Manage OKX grid and DCA Martingale trading bots through the okx CLI, including creation, amendment, stopping, monitoring, P&L checks, TP/SL, margin adjustments, and AI-recommended parameters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill to guide an agent through authenticated OKX CLI workflows for creating, amending, stopping, and monitoring server-side grid and DCA bots in live or demo trading modes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through live OKX trading-bot actions that may affect real funds. <br>
Mitigation: Review every live-mode action before execution, prefer demo mode for testing, and confirm key write parameters with the user before create, amend, or stop commands. <br>
Risk: The skill requires sensitive OKX credentials or an OAuth session. <br>
Mitigation: Do not collect credentials in chat; use okx config init and delegate only API-key or OAuth permissions the user is comfortable granting. <br>
Risk: Incorrect bot identifiers, trading mode, or account funding assumptions can create, modify, or stop the wrong bot or fail after partial setup. <br>
Mitigation: Run credential and profile checks, list existing bots to obtain authoritative algo IDs, verify live or demo mode, and report balance shortfalls instead of transferring funds automatically. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/numpy0001/okx-cex-bot) <br>
- [OKX Homepage](https://www.okx.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and command tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the okx CLI, OAuth or API-key credentials, and explicit live or demo mode handling before authenticated trading actions.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
