## Description:

Operate TaxJar through the OOMOL oo CLI for reading, creating, updating, and deleting TaxJar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live TaxJar action schemas and run TaxJar connector actions for sales tax calculation, rates, VAT validation, tax categories, nexus regions, customers, orders, and refunds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl and PowerShell installer commands that could execute unverified remote code.

Mitigation: Use a verified manual install path, inspect what will run, and do not allow an agent to run the installer commands automatically.

Risk: TaxJar write and destructive actions can create, update, or delete business records.

Mitigation: Confirm the exact payload, target record, and intended effect with the user before running write or destructive actions.

Risk: The skill depends on the oo CLI and OOMOL-managed TaxJar credentials.

Mitigation: Install only when the OOMOL publisher and credential handling model are trusted for the intended TaxJar account.

## Reference(s):

- [ClawHub TaxJar skill page](https://clawhub.ai/oomol/skills/oo-taxjar)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [TaxJar homepage](https://www.taxjar.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before building payloads and to confirm write or destructive TaxJar actions before execution.]

## Skill Version(s):

1.0.3 (source: evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
