## Description:

Jumpseller (jumpseller.com). Use this skill for Jumpseller requests to read, create, and update store data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Jumpseller action schemas and run store, product, category, customer, and order actions through an authenticated OOMOL connector. It supports read workflows and confirmed write workflows for creating or updating Jumpseller records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation source and prefer a verified installer or documented release with integrity checks before installing.

Risk: Write actions can create or update products, categories, customers, and orders in Jumpseller.

Mitigation: Show the exact action payload and intended effect to the user and get confirmation before running any state-changing action.

## Reference(s):

- [Jumpseller homepage](https://jumpseller.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jumpseller)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect connector schemas and run Jumpseller actions; write actions require user confirmation of payload and effect.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
