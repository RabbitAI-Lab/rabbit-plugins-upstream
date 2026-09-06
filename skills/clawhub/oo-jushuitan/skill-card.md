## Description:

Jushuitan ERP helps agents inspect live connector schemas and run OOMOL oo CLI actions to read, create, and update Jushuitan ERP data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Jushuitan ERP through an OOMOL-connected account for orders, after-sales, inventory, warehouses, products, purchasing, finance, logistics, WMS, and cross-border workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports unreliable safety labels for several high-impact ERP actions that can affect orders, inventory, shipping, warehouse workflows, finance data, or document status.

Mitigation: Confirm the exact action, payload, business effect, merchant, shop, warehouse, order, SKU, quantities, and current document state before running any action that changes ERP data.

Risk: The setup guidance includes remote script execution for installing the oo CLI.

Mitigation: Prefer a verified oo CLI installation path and review installation sources before piping downloaded scripts into a shell.

Risk: The skill operates through connected OOMOL and Jushuitan accounts and can access merchant ERP data.

Mitigation: Use an account with permissions scoped to the intended task and reconnect only when authentication or connection errors require it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jushuitan)
- [Jushuitan ERP homepage](https://www.jushuitan.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
