## Description:

NeetoCal helps an agent search and read NeetoCal booking, scheduling link, and available-slot data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect NeetoCal connector schemas and retrieve bookings, scheduling links, and available slots from an OOMOL-connected NeetoCal account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote pipe-to-shell installer commands for the oo CLI.

Mitigation: Avoid running the installer blindly; use a trusted, verifiable package or review the installer before execution.

Risk: The skill accesses NeetoCal through OOMOL as an intermediary.

Mitigation: Install only when OOMOL intermediary access is acceptable for the user's organization and connected NeetoCal account.

Risk: Connector actions may expose booking, scheduling link, or availability information from the connected NeetoCal account.

Mitigation: Use the skill for the listed read-only actions, inspect the live schema before constructing payloads, and run only user-relevant queries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-neetocal)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [NeetoCal Homepage](https://www.neeto.com/neetocal)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides oo CLI schema inspection and read-only NeetoCal connector actions; command responses are JSON.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
