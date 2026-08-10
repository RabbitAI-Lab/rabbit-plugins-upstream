## Description: <br>
Research, size, and route user-signed Hyperliquid perpetual futures with funding analysis, drawdown guards, EIP-712, and zero custody. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to research Hyperliquid perpetual futures, inspect account risk, size candidate trades, and route user-approved EIP-712 signed orders or cancellations. It is intended for zero-custody workflows where every state-changing action requires fresh manual confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help place real perpetual futures trades or cancel active orders, which can change market exposure and cause financial loss. <br>
Mitigation: Review every proposed trade or cancellation, including asset, side, size, leverage, stop, order type, signature details, and builder fee, before giving fresh manual confirmation. <br>
Risk: Wallet secrets or raw private key material would create custody and account-compromise risk if shared with an agent. <br>
Mitigation: Use only public account addresses, optional FarmDash bearer access, and user-signed EIP-712 payloads; never provide private keys, seed phrases, wallet exports, or raw wallet secrets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-futures-strategist) <br>
- [FarmDash Agents Homepage](https://www.farmdash.one/agents) <br>
- [Bundled OpenAPI Contract](artifact/openapi.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON from agent tool workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include market analysis, position sizing, account-risk summaries, execution or cancellation request parameters, and confirmation prompts.] <br>

## Skill Version(s): <br>
1.0.21 (source: ClawHub release evidence; artifact frontmatter reports 3.2.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
