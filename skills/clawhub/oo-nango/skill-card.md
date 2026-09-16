## Description:

Nango lets an agent inspect and manage Nango connections, integrations, and providers through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Nango connection, integration, and provider information and to perform approved connection tag, metadata, or deletion changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage Nango connections, including write and delete operations.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write or destructive action.

Risk: Credential retrieval may expose sensitive connection details when permitted.

Mitigation: Treat get_connection output as sensitive and avoid storing or displaying credentials unless needed for the task.

Risk: Remote installer commands can introduce supply-chain risk.

Mitigation: Use a trusted, verified oo CLI installation method before running connector actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nango)
- [Nango homepage](https://nango.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from Nango connector actions, including sensitive connection details when permitted.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
