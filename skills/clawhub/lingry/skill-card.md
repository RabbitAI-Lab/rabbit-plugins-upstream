## Description: <br>
Create, discover, and coin Lingry words with a local Sugarchain wallet, explicit terminal approval, and no wallet-passphrase exposure to OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[svetlyoh](https://clawhub.ai/user/svetlyoh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect Lingry status, browse public words, generate word candidates, prepare Lingry word drafts, and prepare wallet-backed coining or starter-grant requests while keeping signing and wallet secrets in a private terminal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet keys, passphrases, session tokens, or local keystore contents could be exposed if pasted into chat, logs, shell history, screenshots, or world-readable files. <br>
Mitigation: Keep wallet import, hidden passphrase entry, token refresh, signing, and broadcast in a private terminal; store local token files with restrictive permissions and never ask the user to paste secrets into chat. <br>
Risk: Prepared coining, starter-grant, tip, or payment requests could be mistaken for completed transactions. <br>
Mitigation: Treat agent-prepared requests as unsigned proposals until the user reviews them, explicitly approves broadcast in a private terminal, and the API or node response confirms success. <br>
Risk: Authenticated Lingry workflows can fail or expose stale state when the local session token, helper files, or runtime environment are missing or outdated. <br>
Mitigation: Verify installation and auth status before wallet workflows, refresh the browser-created Lingry session token privately, and restart the OpenClaw gateway when environment changes need to take effect. <br>


## Reference(s): <br>
- [ClawHub Lingry skill page](https://clawhub.ai/svetlyoh/skills/lingry) <br>
- [Server-resolved GitHub provenance](https://github.com/svetlyoh/web-wallet/tree/master/openclaw/skills/lingry) <br>
- [Lingry homepage and API](https://lingry.net) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and concise command-output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prepare non-secret local request metadata for wallet approval; signing and broadcast remain user-controlled in a private terminal.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
