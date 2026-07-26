## Description: <br>
Verify AI agent identity and reputation via ERC-8004 on-chain registries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sumeetchougule](https://clawhub.ai/user/sumeetchougule) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to check whether an AI agent has an ERC-8004 on-chain identity and to review its reputation before deciding whether to trust it. The default commands are read-only lookups, while registration is an optional on-chain action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional registration command can sign and broadcast an on-chain transaction when CHAOSCHAIN_PRIVATE_KEY is configured. <br>
Mitigation: Use verify and reputation lookups for normal read-only operation; configure a dedicated low-balance wallet only when intentionally registering. <br>
Risk: Mainnet registration handling is reported as misleading by the security evidence. <br>
Mitigation: Explicitly choose a testnet for testing and review the selected network before running registration. <br>
Risk: Private-key configuration increases exposure if the same wallet is reused elsewhere. <br>
Mitigation: Avoid casual CHAOSCHAIN_PRIVATE_KEY configuration and keep registration credentials limited to a purpose-specific wallet. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sumeetchougule/skills/chaoschain) <br>
- [ChaosChain Homepage](https://chaoscha.in) <br>
- [ChaosChain Documentation](https://docs.chaoscha.in) <br>
- [ERC-8004 Specification](https://eips.ethereum.org/EIPS/eip-8004) <br>
- [8004scan Agent Explorer](https://8004scan.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown-style command examples and plain-text CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read commands can query public blockchain RPC endpoints; the optional register command can submit a signed transaction when a private key is configured.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
