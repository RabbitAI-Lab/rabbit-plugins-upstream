## Description:

Detrack lets agents read, create, update, and delete Detrack delivery and collection data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Detrack connector schemas and manage jobs and depots through an OOMOL-connected Detrack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-downloaded installer scripts.

Mitigation: Review the oo CLI installation path first, prefer a pinned, signed, or checksum-verified installer, and do not let the agent run setup automatically.

Risk: Create and update actions can change Detrack operational data.

Mitigation: Inspect the live action schema, confirm the exact payload and intended effect with the user, then run the action only after approval.

Risk: Delete actions can remove Detrack job records.

Mitigation: Confirm the target job and date with the user and require explicit approval before running destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-detrack)
- [Detrack homepage](https://www.detrack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Detrack connector schemas before constructing action payloads; connector responses are JSON when --json is used.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
