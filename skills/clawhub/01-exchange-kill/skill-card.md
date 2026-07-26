## Description: <br>
AI-powered 01.xyz exchange development skill for monitoring, trading strategies, and N1 blockchain integration. Covers REST API (FTX-inspired), Nord.ts SDK (@n1xyz/nord-ts), non-custodial trading patterns, and market making on Solana. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bouncyknighter](https://clawhub.ai/user/bouncyknighter) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and engineers use this skill to build 01.xyz and N1 blockchain monitoring, SDK integration, account tracking, risk analysis, and trading automation workflows. It provides implementation guidance, example commands, and safety checks for non-custodial perpetual futures integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example trading flows can affect real crypto funds when adapted for mainnet. <br>
Mitigation: Use devnet first, keep signing local, use a dedicated low-balance wallet, and require explicit confirmation before orders, withdrawals, deposits, or position-closing actions. <br>
Risk: Incorrect packages or endpoints could route development work to untrusted dependencies or services. <br>
Mitigation: Verify npm packages and 01.xyz/N1 endpoints against official sources before installing or connecting automation. <br>
Risk: Automated trading logic can create liquidation, stale-order, or wrong-market exposure. <br>
Mitigation: Apply the skill's account-health checks, market ID validation, devnet testing, and margin monitoring before using live funds. <br>


## Reference(s): <br>
- [01.xyz](https://01.xyz) <br>
- [01.xyz Developer Docs](https://docs.01.xyz) <br>
- [01.xyz API Reference](https://api.01.xyz) <br>
- [N1 Blockchain Docs](https://docs.n1.xyz) <br>
- [Nord TypeScript SDK](https://www.npmjs.com/package/@n1xyz/nord-ts) <br>
- [ClawHub Skill Page](https://clawhub.ai/bouncyknighter/skills/01-exchange-kill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline JavaScript, TypeScript, bash, curl, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; examples may call public market-data APIs or local trading APIs when applied by a user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
