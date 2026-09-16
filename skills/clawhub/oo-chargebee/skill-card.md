## Description:

Chargebee (chargebee.com). Use this skill for Chargebee requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Chargebee action schemas and run Chargebee customer, invoice, item price, and subscription actions through the oo CLI. It supports read workflows and confirmed customer creation against an OOMOL-connected Chargebee account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes online installer commands that execute downloaded content in a shell.

Mitigation: Do not let an agent run first-time installer commands automatically; install the oo CLI through a verified, pinned, or inspected method.

Risk: Chargebee write actions can create or modify billing data.

Mitigation: Confirm the exact JSON payload and expected effect with the user before running any write action.

## Reference(s):

- [Chargebee homepage](https://www.chargebee.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Chargebee skill page](https://clawhub.ai/oomol/skills/oo-chargebee)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Chargebee account.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
