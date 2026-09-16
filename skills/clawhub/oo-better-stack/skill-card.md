## Description:

Better Stack lets agents read, create, and update Better Stack data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Better Stack incidents and metadata from an agent session, including reading incident state and performing confirmed incident changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes direct installer commands for the oo CLI, including pipe-to-shell installation flows.

Mitigation: Review installation commands before use and prefer inspected or documented installation steps instead of running remote installer scripts directly.

Risk: Incident-management actions can create, acknowledge, or escalate Better Stack incidents.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any state-changing incident action.

## Reference(s):

- [Better Stack homepage](https://betterstack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue oo CLI commands that return JSON responses from Better Stack connector actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
