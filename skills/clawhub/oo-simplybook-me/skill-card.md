## Description:

This skill helps agents operate SimplyBook.me through an OOMOL-connected account for reading, creating, and updating booking-related data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to inspect SimplyBook.me action schemas and run connector actions for company information, services, performers, and availability through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands.

Mitigation: Review the install path before use, prefer a verified package or checksum-verified installer, and do not let an agent run curl|bash or irm|iex installer commands automatically.

Risk: Connector actions can affect SimplyBook.me data when write-capable actions are requested.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions, and monitor requested SimplyBook.me actions.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SimplyBook.me homepage](https://simplybook.me/)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-simplybook-me)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata when actions run successfully.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
