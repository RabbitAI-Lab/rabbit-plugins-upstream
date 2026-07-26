## Description: <br>
Minecraft Custom Mod Builder helps agents generate, validate, and runtime-check structured Minecraft Bedrock add-ons, Bedrock skin packs, and Fabric or NeoForge projects through AgentPMT-hosted build and verification tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to create Minecraft mods and skin packs from structured specifications, review visual proof, and iterate on generated or agent-edited source until install-readiness checks pass. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mod specifications, textures, generated artifacts, and uploaded source archives may be sent to AgentPMT or File Manager for remote processing. <br>
Mitigation: Upload only intended assets and source; avoid private or proprietary code unless the user has approved remote processing. <br>
Risk: Generated client utilities or prank and chaos mechanics could be misused on public or unauthorized servers. <br>
Mitigation: Use these outputs only in single-player, private, or explicitly authorized servers, and keep the install-readiness and visual-review gates before delivery. <br>
Risk: Account, wallet, or payment secrets could be exposed through prompts or logs during setup. <br>
Mitigation: Keep account secrets, wallet private keys, mnemonics, signatures, and payment headers out of prompts and logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/minecraft-custom-mod-builder) <br>
- [AgentPMT Marketplace Page](https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder) <br>
- [Icon Generator Skill](https://clawhub.ai/agentpmt/product-icon-generator) <br>
- [File Management Skill](https://clawhub.ai/agentpmt/file-management) <br>
- [AgentPMT Main MCP Server](https://api.agentpmt.com/mcp/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON action parameters and generated source or installable artifact references.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote AgentPMT tool calls may return task ids, runtime verification results, visual proof file ids or signed URLs, generated source archives, and installable artifacts.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
