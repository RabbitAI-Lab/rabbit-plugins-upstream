## Description:

Tongcheng Chengxin (ly.com) lets agents search and read travel data for attractions, buses, flights, hotels, trains, multimodal transport, and travel products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill through an OOMOL-connected account to search Tongcheng Chengxin travel inventory and recommendations. It supports travel discovery workflows across attractions, buses, flights, hotels, trains, multimodal transport, and vacation products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to execute a remote oo CLI installer directly in the shell without built-in verification.

Mitigation: Review the oo CLI installation path before installing, prefer a signed or checksum-verified package, inspect the installer when practical, and avoid running it from an elevated shell.

Risk: Future or changed connector actions could have write or destructive effects if tagged that way by the live action catalog.

Mitigation: Inspect the live connector schema before building a payload and require explicit user confirmation for any action tagged write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chengxin)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Tongcheng Chengxin homepage](https://www.ly.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and search/read actions through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
