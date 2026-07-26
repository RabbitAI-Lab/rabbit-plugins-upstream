## Description: <br>
Access Web3 email via EtherMail using WalletConnect for messages tied to an Ethereum wallet address. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Ethermail to access EtherMail through Telegram or browser automation, connect an Ethereum wallet with WalletConnect, and read or send wallet-addressed email. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead users to use a raw Ethereum private key with automatic WalletConnect signing. <br>
Mitigation: Use a dedicated low-value wallet, prefer manual or hardware-backed signing where possible, and never use a primary or funded wallet key. <br>
Risk: WalletConnect signing depends on a separate connector skill or setup that affects login security. <br>
Mitigation: Inspect the separate walletconnect-agent or connector implementation before use and install it only from a trusted source. <br>
Risk: Browser automation can expose session state or wallet-connection data during the EtherMail login flow. <br>
Mitigation: Run the browser automation in an isolated environment and review the generated WalletConnect URI handling before connecting a wallet. <br>


## Reference(s): <br>
- [ClawHub Ethermail skill page](https://clawhub.ai/daaab/skills/ethermail) <br>
- [EtherMail website](https://ethermail.io) <br>
- [EtherMail Telegram Mini App](https://t.me/ethermailappbot/app?startapp=afid_6986e9a5c5a97b905a78c390) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with bash and JavaScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes WalletConnect URI extraction steps and browser automation guidance; the bundled script prints a wc: URI to stdout.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
