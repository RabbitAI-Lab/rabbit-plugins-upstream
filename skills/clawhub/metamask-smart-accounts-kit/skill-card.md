## Description: <br>
Web3 development using MetaMask Smart Accounts Kit for building dApps with ERC-4337 smart accounts, user operations, batch transactions, signers, paymasters, delegations, and ERC-7715 advanced permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ayushbherwani1998](https://clawhub.ai/user/ayushbherwani1998) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to get implementation guidance and code examples for MetaMask smart accounts, delegation flows, gas abstraction, and advanced permission requests in Web3 applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Copied smart-account or delegation code can move real assets if chain IDs, recipients, token addresses, amounts, expiries, or caveats are wrong. <br>
Mitigation: Use testnets first and verify chain IDs, recipients, token addresses, amounts, expiries, and caveats before any mainnet use. <br>
Risk: Private keys or wallet secrets can be exposed through source code, prompts, logs, or client-side applications. <br>
Mitigation: Use secure wallet and key-management practices, and never paste or persist real private keys in code, prompts, logs, or browser-delivered apps. <br>
Risk: Incorrect bundler, paymaster, or delegation settings can authorize unintended operations. <br>
Mitigation: Verify bundler and paymaster URLs, review generated calldata, and apply restrictive caveats and time limits before redeeming delegations. <br>


## Reference(s): <br>
- [MetaMask Smart Accounts Kit Documentation](https://docs.metamask.io/smart-accounts-kit) <br>
- [Smart Accounts Reference](references/smart-accounts.md) <br>
- [Delegations Reference](references/delegations.md) <br>
- [Advanced Permissions Reference](references/advanced-permissions.md) <br>
- [MetaMask Flask](https://metamask.io/flask) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with TypeScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; copied code should be reviewed before use with real wallets or assets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
