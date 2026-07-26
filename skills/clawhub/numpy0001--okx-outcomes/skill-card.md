## Description: <br>
OKX Outcomes helps agents use the okx-outcomes CLI to browse YES/NO event-contract markets, guide setup and authentication, inspect account state, and prepare confirmed trading actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to research OKX Outcomes markets, complete OAuth and wallet binding, check balances and positions, and prepare CLI trading workflows with explicit confirmation before write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install path may encourage running an unpinned remote shell script. <br>
Mitigation: Review the install step first and prefer a verified release or official package-manager path for okx-outcomes instead of running curl piped to sh blindly. <br>
Risk: Trading write actions can place or cancel orders, lock points, merge positions, or redeem balances. <br>
Mitigation: Keep the dry-run preview and exact confirm flow, and verify the OKX account, wallet address, market, price, and size before any write action. <br>
Risk: OAuth sessions and signing keys are sensitive credentials for account access and on-chain authorization. <br>
Mitigation: Never paste private keys into chat; use the documented setup and keyring flow, mask secret values, and rotate credentials if exposure occurs. <br>


## Reference(s): <br>
- [OKX homepage](https://www.okx.com) <br>
- [OKX Outcomes CLI reference](https://github.com/okx/outcomes-cli/blob/main/docs/cli-reference.md) <br>
- [Setup & Authentication](references/setup-auth.md) <br>
- [Cross-Command Workflows](references/workflows.md) <br>
- [Account Commands](references/account-commands.md) <br>
- [CLOB Commands](references/clob-commands.md) <br>
- [CTF Commands](references/ctf-commands.md) <br>
- [Data Commands](references/data-commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses dry-run previews and exact user confirmation for write actions; command examples often use --json for structured output.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
