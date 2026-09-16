## Description:

Printify (printify.com). Use this skill for ANY Printify request: reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Printify shop data through an authenticated OOMOL connection. It supports retrieving orders and products, listing shops, listing orders with filters, and listing products with pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installation commands for the oo CLI.

Mitigation: Review the CLI source and installation method first, prefer a signed or checksummed installer, and avoid running the pipe-to-shell installer unless independently verified.

Risk: Some Printify actions may change account data.

Mitigation: Use the skill only for explicit Printify account tasks and confirm the exact payload and effect before executing any action marked as write.

## Reference(s):

- [Printify homepage](https://printify.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-printify)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads/responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return connector data with meta.executionId when actions run.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
