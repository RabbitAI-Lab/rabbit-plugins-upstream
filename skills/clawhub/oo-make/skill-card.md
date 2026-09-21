## Description:

Make (make.com). Use this skill for Make requests involving reading, creating, updating, and deleting data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to inspect Make connector schemas, query Make account and scenario data, and run or change Make scenarios through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Make automations through write and destructive connector actions.

Mitigation: Confirm the exact scenario, payload, and expected effect with the user before approving write or destructive actions.

Risk: The first-time setup section includes remote installer commands.

Mitigation: Review the oo CLI installer through a safer path before running pipe-to-shell or PowerShell install commands.

Risk: Read actions may expose sensitive Make account, credential authorization, scenario, and usage metadata.

Mitigation: Treat retrieved Make data as sensitive and share or store it only when needed for the user's task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-make)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Make](https://www.make.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before executing Make actions and to confirm write or destructive operations before running them.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
