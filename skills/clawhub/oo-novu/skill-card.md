## Description:

Use this skill to read, create, and update Novu data through the OOMOL-connected oo CLI instead of calling the Novu API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Novu subscribers and trigger workflow events through an OOMOL-connected Novu account. It supports read, search, create, update, and event-triggering workflows while requiring confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute downloaded scripts directly.

Mitigation: Review or verify the installer through official, versioned installation steps before running it.

Risk: The connector can create or update subscribers and trigger workflow events in a Novu account.

Mitigation: Confirm each state-changing action and exact JSON payload with the user before execution.

Risk: Using the skill delegates Novu account operations to OOMOL's connected-service flow.

Mitigation: Install only when the operator accepts OOMOL connector access to the relevant Novu account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-novu)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Novu Homepage](https://novu.co)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Novu action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
