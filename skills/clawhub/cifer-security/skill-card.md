## Description: <br>
Implement quantum-resistant encryption using the CIFER SDK (cifer-sdk npm package), including SDK initialization, wallet setup, secret creation, text encryption/decryption, and file encryption/decryption on Ethereum, Sepolia, and Ternoa. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tip-citron](https://clawhub.ai/user/tip-citron) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to integrate CIFER SDK encryption into blockchain applications, including wallet signing, on-chain secret creation, payload encryption/decryption, and file encryption/decryption workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet setup and blockchain examples can expose private keys or spend funds if copied into unsafe environments. <br>
Mitigation: Use testnets or low-balance wallets for examples, confirm chain IDs and fees before sending transactions, and keep private keys out of chat, source control, logs, and frontend bundles. <br>
Risk: File encryption and decryption examples use a configured remote blackbox service and may process sensitive files. <br>
Mitigation: Avoid uploading highly confidential files unless you trust the remote service, and choose output paths that do not overwrite important local data. <br>


## Reference(s): <br>
- [CIFER SDK Full API Reference](reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JavaScript and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes SDK setup steps, wallet guidance, blockchain transaction examples, error-handling notes, and file-handling examples.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
