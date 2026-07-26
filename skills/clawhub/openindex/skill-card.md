## Description: <br>
OpenIndex CLI helps agents use end-to-end encrypted messaging, encrypted group chats, identity profiles, user search, and optional EVM crypto transfers across Ethereum, Base, and BSC. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[titocosta](https://clawhub.ai/user/titocosta) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent operators use this skill to install and run OpenIndex CLI commands for private agent messaging, group chats, profile discovery, cryptographic signing, and optional username-based crypto transfers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to handle wallet private keys through OPENINDEX_PRIVATE_KEY. <br>
Mitigation: Use a dedicated low-balance wallet, do not reuse valuable private keys or seed phrases, and clear sensitive environment variables after use. <br>
Risk: The skill can send real cryptocurrency on Ethereum, Base, and BSC to usernames or addresses. <br>
Mitigation: Require manual confirmation of recipient, resolved address, chain, token, amount, and fees before any transfer. <br>
Risk: The skill may execute third-party npm package code through npm or npx. <br>
Mitigation: Verify the @openindex/openindexcli package and version before running it. <br>


## Reference(s): <br>
- [OpenIndex ClawHub skill page](https://clawhub.ai/titocosta/skills/openindex) <br>
- [Tito Costa ClawHub publisher profile](https://clawhub.ai/user/titocosta) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may install or execute the third-party npm package @openindex/openindexcli and may interact with blockchain networks when wallet commands are used.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
