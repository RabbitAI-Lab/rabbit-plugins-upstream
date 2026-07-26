## Description: <br>
Provides a Telegram Web App for Chia wallet verification via WalletConnect and Sage, enabling cryptographic proof of wallet ownership through MintGarden signature verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Telegram bot operators use this skill to add Chia wallet ownership verification to Telegram workflows such as NFT-gated groups, airdrop eligibility, Web3 authentication, DAO voting, and proof-of-holdings checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The verification flow links a Chia wallet address to a Telegram user. <br>
Mitigation: Provide a clear privacy notice and avoid retaining signatures, public keys, or address-to-user mappings longer than necessary. <br>
Risk: The bundled app includes a default WalletConnect project ID. <br>
Mitigation: Replace it with an operator-controlled WalletConnect project ID before production deployment. <br>
Risk: Open CORS, unauthenticated status checks, and missing rate limits can expose the verification service to abuse. <br>
Mitigation: Restrict CORS to the deployment domain, authenticate or remove status endpoints, and add rate limiting to verification requests. <br>
Risk: Console logs may expose wallet addresses, signatures, public keys, or verification details. <br>
Mitigation: Remove sensitive logs or redact wallet and signature data before operating the service with real users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/koba42corp/skills/chia-walletconnect) <br>
- [MintGarden API documentation](https://api.mintgarden.io/docs) <br>
- [WalletConnect documentation](https://docs.walletconnect.com/) <br>
- [Telegram Web Apps documentation](https://core.telegram.org/bots/webapps) <br>
- [Sage Wallet](https://www.sagewallet.io/) <br>
- [CHIP-0002](https://github.com/Chia-Network/chips/blob/main/CHIPs/chip-0002.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown documentation with JavaScript examples, shell commands, configuration snippets, and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a public HTTPS deployment for Telegram Web App use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
