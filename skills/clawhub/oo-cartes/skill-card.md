## Description:

Cartes.io helps agents read, create, update, delete, search, and list Cartes.io maps, markers, users, and categories through the OOMOL-connected cartes connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Cartes.io resources through an OOMOL-connected account, including map lifecycle operations, marker management, public search, and user or category reads. It is appropriate when an agent needs to inspect live action schemas, run Cartes.io connector actions, and confirm state-changing payloads before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts.

Mitigation: Use an official, verifiable oo CLI installation path and avoid running pasted installer pipelines blindly.

Risk: The skill can create, update, or delete Cartes.io maps and markers.

Mitigation: Review exact write or destructive payloads and obtain user confirmation before approving those actions.

Risk: The skill depends on OOMOL as the connector for the user's Cartes.io account.

Mitigation: Install only when use of OOMOL for Cartes.io access is acceptable for the deployment.

## Reference(s):

- [Cartes.io homepage](https://cartes.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Cartes.io skill](https://clawhub.ai/oomol/skills/oo-cartes)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
