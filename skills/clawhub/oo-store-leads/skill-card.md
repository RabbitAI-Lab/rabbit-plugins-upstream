## Description:

Store Leads helps agents search and read Store Leads ecommerce app, domain, and technology data through the OOMOL Store Leads connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve Store Leads ecommerce app, domain, and technology records through an OOMOL-connected account without handling raw Store Leads credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback asks users to execute an unverified internet installer directly in a shell.

Mitigation: Install the oo CLI only through a trusted, verified, or pinned OOMOL release path, and avoid running installer commands from an elevated terminal.

Risk: Authentication, connection, credential, or billing failures can prevent Store Leads actions from running.

Mitigation: Use the first-time setup steps only after matching errors occur, then sign in, reconnect Store Leads, refresh credentials, or resolve billing before retrying.

Risk: Command payloads can become invalid if the live connector schema differs from examples in the skill text.

Mitigation: Fetch the action schema with the oo CLI before constructing payloads, and build requests from that live schema.

## Reference(s):

- [ClawHub Store Leads skill](https://clawhub.ai/oomol/skills/oo-store-leads)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Store Leads homepage](https://storeleads.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Store Leads get and list actions; live connector schema should be fetched before payload construction.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
