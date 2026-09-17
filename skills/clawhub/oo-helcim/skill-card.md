## Description:

Helcim (helcim.com) support for reading, creating, and updating customer data through an OOMOL-connected Helcim account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve, search, create, and update Helcim customer records through an OOMOL-connected account while avoiding direct handling of raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute scripts directly.

Mitigation: Review setup before installation; prefer installing the oo CLI from a verified release or package source instead of automatically running pipe-to-shell commands.

Risk: Customer create and update actions can change Helcim records.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, then run only the requested write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-helcim)
- [Helcim homepage](https://www.helcim.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload or response examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Customer create and update actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
