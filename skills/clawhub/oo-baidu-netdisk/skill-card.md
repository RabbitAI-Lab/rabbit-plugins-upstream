## Description:

This skill operates Baidu Netdisk (pan.baidu.com) through an OOMOL-connected account for reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to browse, search, download, upload, share, and reorganize files in a connected Baidu Netdisk account. It is intended for tasks that need Baidu Netdisk operations through the OOMOL oo CLI rather than direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer scripts for the oo CLI.

Mitigation: Prefer verified official releases or package-manager instructions, and run remote installer scripts only after deciding to trust OOMOL and the local code-execution risk.

Risk: Baidu Netdisk downloads and share links may pass through OOMOL connector transit storage or become externally accessible.

Mitigation: Confirm the content, destination, and sharing scope before download or share-link actions, and handle resulting links or files according to the user's data-handling requirements.

Risk: Write actions can create, copy, move, rename, share, or upload files in the connected Baidu Netdisk account.

Mitigation: Inspect the live connector schema, present the exact payload and expected effect, and obtain user confirmation before running state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baidu-netdisk)
- [Baidu Netdisk homepage](https://pan.baidu.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions inspect live connector schemas before execution; write actions require user confirmation before state changes.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
