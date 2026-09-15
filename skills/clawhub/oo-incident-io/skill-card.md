## Description:

incident.io helps agents search and read incident.io data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to inspect incident.io incidents, actions, statuses, and severities from a connected incident.io account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes one-line remote installer commands, which evidence.security flags as a supply-chain risk.

Mitigation: Use a verified or pinned oo CLI installation path, inspect installers before execution, and avoid running remote installer commands directly in a shell.

Risk: The skill mediates incident.io access through OOMOL-connected credentials.

Mitigation: Install only if OOMOL-mediated access is acceptable, connect a least-privilege incident.io credential, and keep usage to the listed read-only actions unless a future version clearly discloses and gates writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-incident-io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [incident.io](https://incident.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill calls listed read-only incident.io connector actions and returns connector data with execution metadata when commands are run.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
