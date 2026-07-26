## Description: <br>
Poseidon OTC lets agents create Solana P2P trade rooms, negotiate token offers, lock tokens with escrow, and execute atomic swaps through the Poseidon OTC protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[romovow](https://clawhub.ai/user/romovow) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use this skill to coordinate P2P SPL token swaps on Solana, including room creation, offer negotiation, optional lockups, confirmations, cancellations, and execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous mode can give an agent hot-wallet authority to move funds through Poseidon services. <br>
Mitigation: Use only a dedicated, low-balance burner wallet and do not configure a primary wallet key. <br>
Risk: Incorrect token mints, amounts, room IDs, counterparties, recipient wallets, lockups, claims, cancellations, or executions can move funds unexpectedly. <br>
Mitigation: Require manual approval for each funds-moving or receive-wallet action and verify trade details outside the Poseidon API before signing or executing. <br>


## Reference(s): <br>
- [Poseidon Website](https://poseidon.cash) <br>
- [Poseidon Documentation](https://docs.poseidon.cash) <br>
- [ClawHub Skill Page](https://clawhub.ai/romovow/skills/poseidon-otc) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [JSON-like action results and Markdown documentation with TypeScript and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Solana room IDs, trade links, wallet addresses, balances, and transaction signatures.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
