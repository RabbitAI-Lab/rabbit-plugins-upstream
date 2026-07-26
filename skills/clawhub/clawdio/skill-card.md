## Description: <br>
Auditory intelligence for AI agents that transforms human audio into structured data, semantic reports, and machine-readable markdown for market intelligence, crypto alpha, speaker-attributed quotes, and sentiment analysis from voice conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benschiller](https://clawhub.ai/user/benschiller) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents, developers, and market-research workflows use this skill to browse Clawdio's catalog and purchase voice-discussion reports that include metadata, structured markdown analysis, and speaker-attributed transcripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent with access to a funded wallet can spend real USDC through the automatic x402 purchase flow. <br>
Mitigation: Use a dedicated low-balance wallet, verify the Clawdio domain, report ID, and 1.49 USDC price, and require manual approval or a strict spending policy before any /catalog/purchase request. <br>


## Reference(s): <br>
- [Clawdio API](https://clawdio.vail.report) <br>
- [ClawHub skill page](https://clawhub.ai/benschiller/skills/clawdio) <br>
- [Coinbase AgentKit documentation](https://docs.cdp.coinbase.com/agentkit) <br>
- [Coinbase CDP SDK documentation](https://docs.cdp.coinbase.com/) <br>
- [x402 protocol](https://www.x402.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell and JavaScript examples; purchased reports are JSON containing metadata plus markdown report and transcript content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and an x402-compatible wallet funded with USDC on Base Mainnet for paid report purchases.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
