## Description: <br>
OKX Outcomes helps agents browse YES/NO event-contract markets, guide OAuth and wallet setup, inspect account state, and prepare confirmed CLOB or CTF trading commands through the okx-outcomes CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-support agents use this skill to operate OKX Outcomes workflows: discover event markets, review prices and positions, complete setup, and prepare order, cancellation, split, merge, or redeem actions with user confirmation. <br>

### Deployment Geography for Use: <br>
Global, subject to OKX Outcomes regional availability and the configured Global or US endpoint. <br>

## Known Risks and Mitigations: <br>
Risk: Install guidance includes an unverified remote shell installer in a high-impact financial workflow. <br>
Mitigation: Prefer a pinned release, checksum or signature verification, and manual review before executing any installer. <br>
Risk: The workflow can read account state and, after confirmation, place or cancel orders and run CTF actions. <br>
Mitigation: Use the documented dry-run preview, require an explicit confirmation before writes, and verify account orders or positions after execution. <br>
Risk: Private keys or signing material could be exposed if shared in chat or passed directly to commands. <br>
Mitigation: Never paste private keys into chat; rely on the local keyring and setup bind flow, and rotate credentials if a key is exposed. <br>


## Reference(s): <br>
- [OKX](https://www.okx.com) <br>
- [Setup & Authentication](references/setup-auth.md) <br>
- [Cross-Command Workflows](references/workflows.md) <br>
- [Account Commands](references/account-commands.md) <br>
- [Data Commands](references/data-commands.md) <br>
- [CLOB Commands](references/clob-commands.md) <br>
- [CTF Commands](references/ctf-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and JSON-oriented workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires okx and okx-outcomes binaries; write actions require a dry-run preview, explicit user confirmation, and post-action verification.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
