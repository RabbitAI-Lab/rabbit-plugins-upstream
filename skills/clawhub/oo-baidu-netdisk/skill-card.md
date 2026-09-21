## Description:

Baidu Netdisk lets an agent operate a user's OOMOL-connected Baidu Netdisk account for reading, creating, updating, sharing, transferring, and managing files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage files and folders in a connected Baidu Netdisk account through OOMOL's connector and the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run an unverified remote installer script for the oo CLI.

Mitigation: Review the oo CLI installation path before installing, prefer a trusted package source, or manually verify the installer source and integrity.

Risk: Connected Baidu Netdisk access can list, search, download, share, create, move, and rename files in the user's account.

Mitigation: Connect Baidu Netdisk only when the user is comfortable granting OOMOL-mediated access, and confirm exact payloads before write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-baidu-netdisk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Baidu Netdisk](https://pan.baidu.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON responses from the oo CLI connector.]

## Skill Version(s):

1.0.5 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
