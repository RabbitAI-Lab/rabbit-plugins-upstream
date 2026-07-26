## Description: <br>
Unipile helps agents inspect live Unipile connector schemas and run OOMOL oo CLI actions to read Unipile accounts, chats, and messages through a connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to retrieve Unipile account, chat, and message data through an OOMOL-connected account. It is intended for read-oriented workflows that need live schema inspection before each connector action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Unipile account, chat, and message data through a connected account. <br>
Mitigation: Install and run it only when the user trusts OOMOL and intends to grant read access to the connected Unipile data. <br>
Risk: First-time setup may require a remote oo CLI installer, sign-in, account connection, or billing action. <br>
Mitigation: Run setup steps only after a matching command failure and only when the user intentionally needs that setup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-unipile) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Unipile Homepage](https://www.unipile.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads Unipile data through OOMOL; action payloads should be based on the live connector schema.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
