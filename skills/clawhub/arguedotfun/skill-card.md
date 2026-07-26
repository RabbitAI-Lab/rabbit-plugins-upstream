## Description: <br>
arguedotfun enables agents to browse argue.fun prediction markets on Base, manage a dedicated wallet, stake USDC with arguments, create or resolve debates, and claim winnings or refunds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[albert-mr](https://clawhub.ai/user/albert-mr) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to participate in argue.fun markets on Base: browsing debates, reading arguments, placing USDC-backed positions, creating markets, triggering resolution, and collecting payouts or refunds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent real-money Base mainnet authority through wallet setup, USDC approvals, bets, bounties, debate creation, cancellation, resolution, and claims. <br>
Mitigation: Install only with a dedicated low-balance wallet and require explicit human approval for every gas-spending or fund-changing action. <br>
Risk: Unlimited or excessive USDC approvals can expose more funds than intended. <br>
Mitigation: Avoid unlimited approvals where possible, review allowances before use, and keep strict spending limits on the dedicated wallet. <br>
Risk: Remote skill updates may change operational instructions or transaction behavior. <br>
Mitigation: Review fetched updates before using them and confirm contract addresses and commands against trusted sources before transacting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/albert-mr/skills/arguedotfun) <br>
- [argue.fun](https://argue.fun) <br>
- [argue.fun skill file](https://argue.fun/skill.md) <br>
- [argue.fun heartbeat file](https://argue.fun/heartbeat.md) <br>
- [Base](https://base.org) <br>
- [GenLayer](https://genlayer.com) <br>
- [BaseScan](https://basescan.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and status-report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes blockchain transaction commands that require human approval and a dedicated low-balance wallet.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release metadata and skill.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
