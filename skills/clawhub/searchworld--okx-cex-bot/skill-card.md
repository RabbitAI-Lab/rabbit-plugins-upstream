## Description: <br>
Manage Grid bots (spot/contract/coin-margined) and DCA Martingale bots (Spot DCA / Contract DCA) on OKX, including create, stop, amend, P&L monitoring, TP/SL, margin or investment adjustment, and AI-recommended parameters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill to guide an agent through OKX grid and DCA bot workflows, including credential checks, live versus demo mode selection, bot creation, updates, monitoring, and stop procedures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write commands can create, amend, stop, or close OKX bots and may move real funds. <br>
Mitigation: Confirm live versus demo mode and review all write-command parameters before execution. <br>
Risk: Contract grid or DCA actions can leave leveraged positions open or expose the user to liquidation risk. <br>
Mitigation: Use demo mode first, review liquidation and margin inputs, and verify bot state after create, amend, stop, or close-position commands. <br>
Risk: Credential misuse could expose OKX account access. <br>
Mitigation: Do not collect credentials in chat; guide users through the OKX CLI configuration flow and verify credential status locally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-bot) <br>
- [OKX homepage](https://www.okx.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live or demo mode annotations and JSON-output command variants.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
