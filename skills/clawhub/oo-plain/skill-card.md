## Description:

Plain (plain.com). Use this skill for Plain requests that read, create, or update customer data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Plain action schemas, fetch or search customers, and create or update customer records through an OOMOL-connected Plain account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes unverified remote installer commands that could execute changing code on the user's machine.

Mitigation: Install the oo CLI through a verified, versioned method when possible, and do not let an agent run remote installer commands automatically.

Risk: The upsert_customer action can create or update Plain customer records.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before execution.

## Reference(s):

- [Plain homepage](https://www.plain.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-plain)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands for reading Plain data and confirmed write operations.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
