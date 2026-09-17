## Description:

Ortto (ortto.com). Use this skill for Ortto requests involving reading, creating, and updating data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to retrieve Ortto contacts, list people, and create or update Ortto people through an OOMOL-connected Ortto account. The skill is intended for Ortto customer data workflows where the agent should inspect live connector schemas before running actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unpinned remote installer scripts executed directly in a shell.

Mitigation: Use a verified installer or package with checksum or signature validation, and run the installer only after trusting the OOMOL source.

Risk: The merge_people action can create or update Ortto people.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, then run the write action only after approval.

Risk: The skill operates through an OOMOL-connected Ortto account.

Mitigation: Confirm the intended OOMOL account and Ortto connection are active before use, and resolve authentication or connection errors through the documented setup flow.

## Reference(s):

- [Ortto ClawHub Skill](https://clawhub.ai/oomol/skills/oo-ortto)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Ortto](https://ortto.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI commands and payload guidance; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: skill metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
