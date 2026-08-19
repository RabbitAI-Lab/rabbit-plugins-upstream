## Description:

SamCart helps agents operate an OOMOL-connected SamCart account by inspecting live connector schemas and running supported customer, order, product, and subscription actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and business operators use this skill to retrieve and list SamCart customers, orders, products, and subscriptions from a connected marketplace through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive SamCart customer, order, and subscription data through a connected commerce account.

Mitigation: Install only if you trust OOMOL, connect only the intended SamCart account, and treat returned commerce records as sensitive business data.

Risk: Setup guidance includes remote installer commands that were not verified by server-resolved provenance.

Mitigation: Review the installer source or use a verified installation path before running setup commands.

Risk: Some actions are tagged as write or destructive and may change or remove SamCart data.

Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub SamCart skill page](https://clawhub.ai/oomol/skills/oo-samcart)
- [SamCart homepage](https://www.samcart.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May expose sensitive customer, order, product, and subscription data returned by the connected SamCart marketplace.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
