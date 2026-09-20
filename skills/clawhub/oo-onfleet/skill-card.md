## Description:

Onfleet (onfleet.com). Use this skill for ANY Onfleet request — reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to inspect schemas and run Onfleet task-management actions through an OOMOL-connected Onfleet account, including reading, creating, cloning, updating, completing, and deleting tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, complete, or delete Onfleet task data through the connected account.

Mitigation: Require explicit user confirmation for the exact payload and target before running write or destructive actions.

Risk: The setup guidance includes remote pipe-to-shell installation commands for the oo CLI.

Mitigation: Manually install or verify the oo CLI before use instead of allowing unattended pipe-to-shell setup.

Risk: The agent operates through credentials connected to the user's OOMOL account.

Mitigation: Install only when the publisher and connector provider are trusted, and review account connection scopes before running actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-onfleet)
- [Onfleet Homepage](https://onfleet.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Onfleet Connection Setup](https://console.oomol.com/app-connections?provider=onfleet)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo connector, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
