## Description: <br>
A Cashu ecash wallet CLI for Bitcoin and Lightning payments. Use when managing Cashu tokens, sending or receiving payments via Lightning or ecash, handling HTTP 402 X-Cashu payment requests, or viewing wallet history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[egge21m](https://clawhub.ai/user/egge21m) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to manage a cocod Cashu wallet, receive or send Cashu and Lightning payments, handle HTTP 402 X-Cashu payment requests, and inspect wallet status or history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can spend real Cashu, Bitcoin, or Lightning funds. <br>
Mitigation: Require explicit user approval before any spend action and use preview or parse commands before execution when available. <br>
Risk: Wallet files, mnemonics, passphrases, and daemon state under ~/.cocod are sensitive. <br>
Mitigation: Keep ~/.cocod private and do not log, print, or expose wallet secrets unless the user explicitly requests a safe subset. <br>
Risk: Using an unexpected cocod package or version can change wallet behavior. <br>
Mitigation: Verify the cocod CLI package and exact 0.0.15 version before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/egge21m/skills/cocod) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires cocod CLI 0.0.15; spend actions require explicit user approval.] <br>

## Skill Version(s): <br>
0.0.15 (source: server release, skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
