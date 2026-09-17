## Description:

Bookingmood helps agents search and read Bookingmood bookings, products, and product availability through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect live Bookingmood action schemas, list bookings and products, and query product availability without handling raw Bookingmood credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that could run arbitrary code on the user's machine.

Mitigation: Install the OOMOL CLI only through a reviewed, trusted, version-pinned method and review installer scripts before execution.

Risk: The skill reads live Bookingmood booking, product, and availability data, which may include business-sensitive information.

Mitigation: Inspect the action schema first, request only needed fields, and avoid exposing returned booking or product data beyond the user's intended workflow.

## Reference(s):

- [ClawHub Bookingmood Skill](https://clawhub.ai/oomol/skills/oo-bookingmood)
- [Bookingmood Homepage](https://www.bookingmood.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before requests and can return connector JSON when actions run.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
