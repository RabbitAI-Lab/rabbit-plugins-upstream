## Description:

HighLevel enables agents to read, create, update, search, and delete HighLevel CRM contact records through an OOMOL-connected command-line connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage HighLevel CRM contacts without handling raw HighLevel credentials directly. It supports contact lookup, search, creation, update, and deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Use a verified package when available, or inspect and verify the installer before running it.

Risk: The skill can create, update, or delete HighLevel contact records.

Mitigation: Confirm the exact target, payload, and intended effect before running write or destructive actions.

Risk: Using the skill grants OOMOL bridge access to CRM contact data.

Mitigation: Install only when the user accepts OOMOL as the bridge to HighLevel and understands the data access involved.

## Reference(s):

- [ClawHub HighLevel skill page](https://clawhub.ai/oomol/skills/oo-high-level)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [HighLevel homepage](https://www.gohighlevel.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing request payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
