## Description:

Operate Figma through an OOMOL-connected account to read, create, update, and delete Figma data via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design-automation agents use this skill to inspect Figma files, nodes, comments, projects, components, styles, and versions, and to perform user-approved write or destructive Figma actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute an unverified remote installer for the oo CLI.

Mitigation: Review or replace the installer with a verified, pinned installation method before installing the skill.

Risk: Write and destructive Figma actions can change or delete account data.

Mitigation: Approve exact targets and payloads before running write or destructive actions.

Risk: The skill relies on OOMOL as an intermediary for a connected Figma account.

Mitigation: Install only when use of OOMOL for the connected Figma account is acceptable.

## Reference(s):

- [ClawHub Figma Skill](https://clawhub.ai/oomol/skills/oo-figma)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Figma](https://www.figma.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return connector JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
