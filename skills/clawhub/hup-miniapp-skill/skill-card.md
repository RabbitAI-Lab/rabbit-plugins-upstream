## Description: <br>
Build, test, and list Hup mini apps - web apps that run inside Hup social posts and transact through the viewer's existing Hup wallet session via the Hup SDK bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[web3senior](https://clawhub.ai/user/web3senior) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold, port, debug, and prepare Hup mini apps that run inside Hup social posts and use the Hup SDK bridge for wallet interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated mini apps can request wallet confirmations through Hup. <br>
Mitigation: Review generated transaction and signing code before use, and keep wallet access scoped to the Hup SDK bridge. <br>
Risk: Unsupported wallet methods or mismatched transaction senders can fail at runtime. <br>
Mitigation: Use personal_sign or eth_signTypedData_v4 for signing, avoid eth_sign, eth_signTransaction, and wallet_addEthereumChain, and ensure transaction from values match the connected account. <br>
Risk: A mini app can render incorrectly or fail review if it self-connects wallets, blocks framing, or ignores Hup embed constraints. <br>
Mitigation: Do not bundle independent wallet connectors, allow Hup iframe embedding, design for the registered aspect ratio, and test standalone fallback behavior before listing. <br>


## Reference(s): <br>
- [Hup mini app live specification](https://hup.social/miniapp-skill.md) <br>
- [Hup mini app SDK](https://hup.social/miniapp-sdk.js) <br>
- [Hup apps directory](https://hup.social/apps) <br>
- [Miniapp guide snapshot](references/miniapp-guide.md) <br>
- [Demo app](references/demo-app.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML, JavaScript, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should use the Hup SDK bridge for wallet access and preserve Hup embed constraints.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
