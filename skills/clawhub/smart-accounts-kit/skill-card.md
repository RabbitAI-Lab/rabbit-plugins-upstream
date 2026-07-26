## Description: <br>
This skill helps developers build dApps with MetaMask Smart Accounts Kit for ERC-4337 smart accounts, user operations, signer configuration, gas abstraction, delegations, and ERC-7715 advanced permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ayushbherwani1998](https://clawhub.ai/user/ayushbherwani1998) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to integrate MetaMask smart accounts, configure account implementations and signers, send user operations, implement gasless flows, and create or redeem constrained delegations. It is aimed at Web3 dApp work involving ERC-4337, ERC-7710, ERC-7715, Viem, paymasters, and the MetaMask Delegation Framework. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet automation examples may involve private keys, session accounts, or delegated authority. <br>
Mitigation: Use testnets first, never commit or log real private keys, and prefer managed signing, KMS, or HSM-backed custody for production session accounts. <br>
Risk: Delegations and advanced permissions can authorize transactions on a user's behalf. <br>
Mitigation: Limit delegations by amount, target, redeemer, call count, and expiry, and require clear user consent and revocation controls. <br>
Risk: Incorrect caveats or smart account state can cause failed or overbroad delegation behavior. <br>
Mitigation: Validate caveat parameters, confirm smart account deployment and status, and test permission flows on testnets before mainnet use. <br>


## Reference(s): <br>
- [Smart Accounts Reference](references/smart-accounts.md) <br>
- [Delegations Reference](references/delegations.md) <br>
- [Advanced Permissions Reference](references/advanced-permissions.md) <br>
- [MetaMask Smart Accounts Kit Documentation](https://docs.metamask.io/smart-accounts-kit) <br>
- [MetaMask Flask](https://metamask.io/flask) <br>
- [ERC-7710 Specification](https://eips.ethereum.org/EIPS/eip-7710) <br>
- [ERC-7715 Specification](https://eips.ethereum.org/EIPS/eip-7715) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TypeScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; developers should review generated wallet, delegation, and transaction guidance before execution.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; toolkit reference 0.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
