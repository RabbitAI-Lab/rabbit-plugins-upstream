## Description: <br>
27 tools for DeFi, DEX swaps, cross-chain bridges, Twitter/X, on-chain token data, crypto utilities, and LLM access via x402 micro-payments on Base. No API keys needed -- payment is the auth. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[foodaka](https://clawhub.ai/user/foodaka) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use Paytoll to access paid MCP tools for DeFi intelligence, transaction-data generation, cross-chain swap and bridge quotes, X/Twitter actions, crypto utilities, and LLM calls. The skill is suited to agents that can make explicit paid tool calls from a dedicated Base wallet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs an unpinned npm MCP server with wallet-signing access. <br>
Mitigation: Review the npm package before installation, pin or otherwise control the package version where possible, and use only a fresh dedicated Base wallet. <br>
Risk: Paid tool calls can automatically spend USDC from the configured wallet. <br>
Mitigation: Keep only funds you are willing to spend in the wallet and require explicit confirmation before paid calls. <br>
Risk: Twitter/X and LLM tools may handle raw OAuth tokens, secrets, private data, or other sensitive inputs. <br>
Mitigation: Avoid sending secrets or private data through these tools and do not provide long-lived X OAuth tokens. <br>
Risk: The MCP server discovers tools dynamically, so available behavior may change over time. <br>
Mitigation: Review the active tool list and costs before use, especially after package or server updates. <br>


## Reference(s): <br>
- [Paytoll ClawHub listing](https://clawhub.ai/foodaka/skills/paytoll) <br>
- [PayToll homepage](https://paytoll.io) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code, Text] <br>
**Output Format:** [Markdown guidance with MCP tool calls, JSON-like tool inputs, and unsigned transaction data where applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool calls may incur USDC micro-payments on Base and may require a dedicated wallet private key plus optional user-provided X OAuth token.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
