## Description:

Operate Mojo Helpdesk through an OOMOL-connected account to read, create, update, search, and comment on helpdesk tickets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents and developers use this skill to operate Mojo Helpdesk from an agent workflow, including ticket creation, retrieval, search, comments, queue and tag listing, and approved updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute unverified code on the user's machine.

Mitigation: Install the oo CLI manually from a trusted source or verify the installer before running setup commands.

Risk: Write and destructive Mojo Helpdesk actions can create comments, create tickets, or overwrite ticket data.

Mitigation: Confirm the exact payload, target ticket, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [Mojo Helpdesk homepage](https://www.mojohelpdesk.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mojo-helpdesk)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas before issuing Mojo Helpdesk actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
