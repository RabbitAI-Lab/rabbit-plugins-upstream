## Description:

A-Leads helps agents search and read A-Leads data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales operations teams, and developers use this skill to find or verify lead contact data through an OOMOL-connected A-Leads account. It supports business email lookup, personal email lookup, phone lookup, and email verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review and verify the OOMOL installer before running curl | bash or irm | iex; use an independently trusted installation method when required.

Risk: Lead enrichment actions may retrieve personal email addresses or phone numbers.

Mitigation: Run lookups only for user-approved tasks with an appropriate business purpose and handle returned contact data as sensitive.

## Reference(s):

- [ClawHub A-Leads skill page](https://clawhub.ai/oomol/skills/oo-a-leads)
- [A-Leads homepage](https://a-leads.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected A-Leads account; action schemas are inspected live before connector calls.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
