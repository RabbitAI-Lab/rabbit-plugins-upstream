## Description:

This skill helps agents operate Credit Repair Cloud by reading, creating, updating, and deleting lead/client and affiliate records through the OOMOL credit_repair_cloud connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users with connected Credit Repair Cloud accounts use this skill to inspect live action schemas and run read, create, update, and delete operations for lead/client and affiliate records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote OOMOL installer scripts for the oo CLI.

Mitigation: Review the installer source and prefer signed or checksum-verified installation before approving setup.

Risk: The skill can create, update, and delete Credit Repair Cloud lead/client and affiliate records.

Mitigation: Confirm the exact target records, live schema, payload, and intended effect with the user before write or destructive actions.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Credit Repair Cloud homepage](https://www.creditrepaircloud.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live schema inspection before actions and returns connector responses with data plus execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
