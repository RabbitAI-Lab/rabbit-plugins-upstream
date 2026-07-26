## Description: <br>
Analyze Twitter Spaces and voice conversations to extract market intelligence, crypto alpha, sentiment analysis, and speaker-attributed insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benschiller](https://clawhub.ai/user/benschiller) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agents use Clawdio to browse a catalog of Twitter Spaces reports, purchase selected reports through x402, and receive market intelligence, speaker-attributed transcripts, and machine-readable metadata from long-form voice conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/benschiller/skills/clawdio-twitter) <br>
- [Clawdio API](https://clawdio.vail.report) <br>
- [API Reference](references/API-REFERENCE.md) <br>
- [Integration Guide](references/INTEGRATION.md) <br>
- [x402 Protocol](https://www.x402.org/) <br>
- [Coinbase AgentKit](https://docs.cdp.coinbase.com/agentkit) <br>
- [Coinbase CDP SDK](https://docs.cdp.coinbase.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown guidance with curl and JavaScript examples; purchased reports return JSON metadata plus Markdown report and transcript artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and an x402-compatible wallet funded with USDC on Base Mainnet. Security evidence recommends using a dedicated low-balance wallet, requiring explicit approval before each purchase, browsing the free catalog first, verifying report ID and price, and handling speaker-attributed transcripts carefully.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
