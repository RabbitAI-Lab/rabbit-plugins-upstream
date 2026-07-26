## Description: <br>
Interact with the Sage Chia blockchain wallet via RPC for XCH transactions, CAT tokens, NFTs, DIDs, offers, options, coin management, and wallet configuration across Mac, Linux, and Windows setups with configurable RPC endpoints and SSL certificates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to operate a Sage Chia wallet through agent-guided RPC calls for balances, XCH and CAT transfers, NFTs, DIDs, offers, WalletConnect actions, and wallet configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority over a live Sage/Chia wallet, including transfers, signing, transaction submission, key management, and mnemonic-related operations. <br>
Mitigation: Use testnet or a test wallet first, require explicit human review of recipient, asset, amount, fee, network, and transaction summary before signing or submitting, and avoid enabling autonomous wallet actions. <br>
Risk: Connecting to an untrusted or remote RPC endpoint could expose wallet operations to an unexpected service. <br>
Mitigation: Keep the default RPC endpoint on localhost unless a trusted endpoint is intentionally configured, and verify certificate and key paths before use. <br>
Risk: Mnemonic, wallet key, certificate, and private key material can compromise funds if logged, shared, or mishandled. <br>
Mitigation: Do not log or transmit secrets, protect wallet key files and mnemonics, and review any request that retrieves or imports secret material. <br>


## Reference(s): <br>
- [Sage RPC Endpoints Quick Reference](references/endpoints.md) <br>
- [Sage Wallet GitHub](https://github.com/xch-dev/sage) <br>
- [Chia Developer Documentation](https://docs.chia.net/) <br>
- [ClawHub Skill Page](https://clawhub.ai/koba42corp/skills/sage-wallet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces RPC-oriented instructions and command examples; wallet responses depend on the user's Sage RPC endpoint and local wallet state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
