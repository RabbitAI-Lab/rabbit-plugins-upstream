## Description:

Tongcheng Chengxin (ly.com) lets agents search and read Tongcheng Chengxin travel data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Tongcheng Chengxin for attractions, hotels, flights, trains, buses, multimodal transport, and travel products through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a reviewed official process, inspect or verify installer artifacts where possible, avoid elevated shells, and do not let an agent run installer one-liners automatically.

Risk: The connector performs account-backed network searches through OOMOL-brokered Tongcheng Chengxin access.

Mitigation: Connect only approved Tongcheng Chengxin accounts and use the skill only when you are comfortable with OOMOL brokering those requests.

## Reference(s):

- [Tongcheng Chengxin Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-chengxin)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Tongcheng Chengxin Homepage](https://www.ly.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
