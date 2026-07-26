## Description: <br>
Helps agents browse, install, update, remove, and verify AI trading skills from the OKX Skills Marketplace using the OKX CLI or related MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-assistant users use this skill to discover, install, update, remove, and verify AI trading skills from the OKX Skills Marketplace. It is for skill marketplace management, not order placement, market data, portfolio review, or bot management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide installation or changes of third-party trading skills across multiple detected agent environments. <br>
Mitigation: Review each target skill before installing and confirm that multi-agent installation is intended before running the default add flow. <br>
Risk: Installed marketplace skills run locally with the agent's permissions. <br>
Mitigation: Install only skills from trusted publishers, use signature verification, and avoid bypassing verification unless the source and risk are explicitly accepted. <br>
Risk: Marketplace access and install flows require local OKX CLI setup and credentials. <br>
Mitigation: Configure credentials only for intended marketplace access and use download-only or MCP alternatives when full CLI installation is unavailable or too broad. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-skill-mp) <br>
- [Publisher profile](https://clawhub.ai/user/searchworld) <br>
- [OKX homepage](https://www.okx.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown with inline shell commands and command-output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CLI commands, MCP tool alternatives, installation guidance, update checks, removal steps, and signature-verification guidance.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
