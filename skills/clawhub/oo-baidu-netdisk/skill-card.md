## Description:

Baidu Netdisk (pan.baidu.com) helps an agent read, create, and update Baidu Netdisk data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to browse, search, inspect quota and account details, download, upload, share, and modify files in a user's Baidu Netdisk account through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to run remote installer scripts directly in a shell.

Mitigation: Review the installer or use a signed, versioned installation path before running it.

Risk: The connector can access a user's Baidu Netdisk account and perform write, share-link, upload, move, copy, and rename actions.

Mitigation: Use a trusted OOMOL-connected account and confirm the exact payload and effect before each state-changing action.

Risk: Connector access may remain available after setup.

Mitigation: Review connected-account permissions periodically and revoke access when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baidu-netdisk)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Baidu Netdisk homepage](https://pan.baidu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, JSON, and text snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON from the oo connector; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
