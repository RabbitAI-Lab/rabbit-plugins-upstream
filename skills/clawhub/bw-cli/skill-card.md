## Description: <br>
Bitwarden CLI helps an agent interact with Bitwarden through the bw CLI for authentication, vault item management, password generation, organization workflows, and Send operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0x7466](https://clawhub.ai/user/0x7466) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill when they want an agent to propose or run Bitwarden CLI workflows for unlocking a vault, retrieving or managing vault entries, generating passwords, sharing Sends, and handling organization-related tasks. It is appropriate only where agent access to the Bitwarden vault is intentionally authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad authority over a Bitwarden password vault. <br>
Mitigation: Install only when the agent is intentionally allowed to operate the vault, and require explicit approval before retrieving secrets, exporting data, deleting items, creating Sends, approving devices, or changing organization resources. <br>
Risk: Persistent shell auto-sourcing can expose vault credentials or session material beyond the immediate task. <br>
Mitigation: Prefer interactive unlocks or short-lived environment variables, and avoid adding vault secret sourcing to persistent shell startup files. <br>
Risk: Raw command output can reveal passwords, TOTP codes, session keys, or exported vault contents. <br>
Mitigation: Review commands before execution, avoid logging sensitive output, and keep exports and raw output disabled unless explicitly needed. <br>
Risk: Starting bw serve can expose vault operations through a local REST API. <br>
Mitigation: Require explicit approval before starting bw serve, bind only to localhost, and stop the service immediately after the approved task. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/0x7466/skills/bw-cli) <br>
- [Bitwarden CLI documentation](https://bitwarden.com/help/cli/) <br>
- [Bitwarden CLI markdown documentation](https://bitwarden.com/help/cli.md) <br>
- [Bitwarden personal API key documentation](https://bitwarden.com/help/personal-api-key/) <br>
- [Bitwarden CLI Command Reference](references/commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that operate on sensitive vault data; outputs should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
