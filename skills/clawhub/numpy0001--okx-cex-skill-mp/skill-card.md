## Description: <br>
Helps agents search, browse, install, update, remove, and verify AI trading skills from the OKX Skills Marketplace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-assistant users use this skill to discover and manage marketplace skill packages for trading workflows. It is for skill marketplace operations, not for placing orders, retrieving market data, or managing trading bots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing marketplace skills can place third-party instructions into local agent environments where they may run with the agent's local permissions. <br>
Mitigation: Use verified installs by default, review each downloaded SKILL.md before use, and install only skills from publishers the user trusts. <br>
Risk: Using force installation can bypass signature verification and install a package after verification failure. <br>
Mitigation: Avoid force installation unless the user has independently trusted the package and accepts the recorded bypass. <br>
Risk: Marketplace access requires API credentials, which can fail or expose sensitive configuration if mishandled. <br>
Mitigation: Configure credentials through the OKX CLI setup flow and resolve authentication errors before attempting marketplace operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/numpy0001/okx-cex-skill-mp) <br>
- [OKX homepage](https://www.okx.com) <br>
- [Publisher profile](https://clawhub.ai/user/numpy0001) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend OKX CLI or MCP marketplace operations and directs users to review third-party skill files before installation.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release metadata; artifact metadata reports 1.3.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
