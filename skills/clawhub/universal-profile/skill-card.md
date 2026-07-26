## Description: <br>
Manage LUKSO Universal Profiles - identity, permissions, tokens, and blockchain operations with cross-chain support for Base and Ethereum. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frozeman](https://clawhub.ai/user/frozeman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure LUKSO Universal Profiles, inspect profile state, manage controller permissions, and prepare or submit profile and token transactions across supported chains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access a Universal Profile controller key and submit irreversible blockchain actions. <br>
Mitigation: Use a testnet or low-value controller first, keep key files locked down, and manually review every transfer, mint, relay, batch, permission, and authorization action before execution. <br>
Risk: Overbroad controller permissions can allow more profile or asset control than intended. <br>
Mitigation: Avoid full-access permissions, prefer least-privilege controller permissions, and review permission changes before authorizing them. <br>


## Reference(s): <br>
- [Universal Profile Skill on ClawHub](https://clawhub.ai/frozeman/skills/universal-profile) <br>
- [ERC725-JS Reference](references/ERC725-JS.md) <br>
- [LUKSO Docs](https://docs.lukso.tech/) <br>
- [LSP6 Key Manager](https://docs.lukso.tech/standards/access-control/lsp6-key-manager) <br>
- [Universal Everything](https://universaleverything.io/) <br>
- [ERC725.js](https://github.com/ERC725Alliance/erc725.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JavaScript snippets, and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include blockchain addresses, transaction payloads, relay requests, and command output; actions require user review before execution.] <br>

## Skill Version(s): <br>
0.9.0 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
