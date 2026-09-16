## Description:

Feishu (feishu.cn). Use this skill for Feishu requests, including reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Feishu Drive, Docs, Wiki, Base, Sheets, Slides, Mail, Calendar, Chat, Tasks, OKRs, approvals, Minutes, and meetings through OOMOL's Feishu connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad write and delete operations across Feishu resources.

Mitigation: Confirm the exact target, payload, and expected effect before approving write or destructive connector actions.

Risk: The release security summary flags unsafe remote installer commands.

Mitigation: Avoid pipe-to-shell installer commands unless the installer source and integrity have been independently verified.

Risk: Connected Feishu account permissions determine the blast radius of actions.

Mitigation: Install only if the OOMOL publisher and connected account permissions are trusted and appropriately scoped.

## Reference(s):

- [ClawHub Feishu Skill](https://clawhub.ai/oomol/skills/oo-feishu)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Feishu](https://www.feishu.cn)
- [OOMOL Feishu Connection](https://console.oomol.com/app-connections?provider=feishu)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for invoking the oo CLI and Feishu connector actions; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
