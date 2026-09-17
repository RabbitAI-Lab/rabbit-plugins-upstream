## Description:

FireHydrant helps agents use an OOMOL-connected FireHydrant account to list and retrieve incidents, services, and environments, and to create incidents through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to inspect FireHydrant incidents, services, and environments and to create incidents after confirming the write payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer execution.

Mitigation: Prefer a verified package, pinned release, checksum, or official manual install path instead of running curl-to-bash or Invoke-Expression commands blindly.

Risk: The skill can read FireHydrant data and create incidents through OOMOL.

Mitigation: Use an authorized connected account, treat incident and service details as sensitive, and confirm exact payloads before any write action.

Risk: Broad routing language may cause use beyond the documented connector actions.

Mitigation: Limit operation to the listed actions and inspect the live action schema before constructing command payloads.

## Reference(s):

- [ClawHub FireHydrant Skill](https://clawhub.ai/oomol/skills/oo-firehydrant)
- [FireHydrant Homepage](https://firehydrant.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live schemas before running connector actions; write actions require payload confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
