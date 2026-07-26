## Description: <br>
Teneo Protocol CLI helps agents discover and query Teneo network agents, manage rooms, handle x402 USDC micropayments, and manage an auto-generated encrypted wallet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[teneoprotocoldev](https://clawhub.ai/user/teneoprotocoldev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to install and operate a Teneo CLI for discovering specialized agents, querying them for real-time data, managing rooms, and handling optional paid calls. It is intended for workflows that may need social media profile lookup, hotel search, crypto pricing, gas fee lookup, Amazon product search, news, or multi-agent orchestration through the Teneo network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically spend crypto through x402 USDC payments. <br>
Mitigation: Use a fresh low-balance wallet and prefer quote then confirm flows for paid actions. <br>
Risk: The CLI can sign transactions requested by remote agents. <br>
Mitigation: Review requested transactions before use and keep valuable accounts separate from TENEO_PRIVATE_KEY. <br>
Risk: The wallet-export-key command can print a live private key. <br>
Mitigation: Treat exported keys as secrets and keep them out of logs, chat transcripts, and shared terminals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/teneoprotocoldev/skills/teneo-agent-sdk) <br>
- [Teneo Protocol Homepage](https://teneo-protocol.ai) <br>
- [Teneo Protocol SDK on npm](https://www.npmjs.com/package/@teneo-protocol/sdk) <br>
- [x402 Protocol](https://x402.org) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash, TypeScript, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are designed to return JSON from the generated CLI where applicable.] <br>

## Skill Version(s): <br>
1.0.21 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
