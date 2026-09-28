## Description:

Guides use of a local credential vault for organizing secrets, controlling access, and recovering access to stored credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and methodology all rights reserved

## Use Case:

Developers and other users can organize credentials in a local vault and use the supplied command-line tools to manage access, backups, and recovery. Keep an agent away from real secrets unless its access is explicitly intended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Master passwords, recovery keys, or secret values may become visible to an agent or in command arguments and output.

Mitigation: Keep the agent away from real secrets unless explicitly intended; use interactive prompts rather than command-line secret arguments and avoid sharing secret-bearing output.

Risk: Reading, removing, or deleting vault entries may disclose or destroy sensitive credentials.

Mitigation: Treat get, remove, and delete operations as sensitive manual actions and keep vault files in a controlled local path.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/credential-vault-design)
- [Vault CLI source](artifact/tools/vault_cli.py)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vault commands may reveal secrets in their output; review sensitive operations before execution.]

## Skill Version(s):

2.0.2 (source: server-resolved ClawHub release; bundled skill frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
