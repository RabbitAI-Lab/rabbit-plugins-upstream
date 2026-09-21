## Description:

Fluxguard helps agents operate Fluxguard monitoring through the OOMOL-connected oo CLI for reading, creating, updating, and deleting account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage Fluxguard monitoring workflows, including adding monitored pages, starting crawls, reading account and page data, managing categories, and maintaining webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Review or replace the remote installer step with a verified installation method before using the skill.

Risk: Fluxguard write and destructive actions can change or remove monitored pages, sites, categories, and webhooks.

Mitigation: Confirm the exact action, target, and payload with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fluxguard)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Fluxguard homepage](https://fluxguard.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use oo connector actions and may read, write, or delete Fluxguard resources depending on the selected action and user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
