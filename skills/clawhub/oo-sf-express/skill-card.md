## Description:

SF Express guides an agent to operate the SF Express connector through OOMOL's oo CLI for shipment, freight, cold chain, print, route, pricing, and station workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams with an OOMOL-connected SF Express account use this skill to inspect live connector schemas and run parcel, freight, cold chain, station, tracking, pricing, and waybill actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance recommends running remote installer scripts.

Mitigation: Prefer a verified package or manually inspect and verify any installer before running it.

Risk: The connector can make real changes to an SF Express account, including order creation, cancellation, address changes, uploads, and template deletion.

Mitigation: Confirm the exact payload and expected effect before any account-changing action.

Risk: Using the skill grants the OOMOL connector authority over the connected SF Express account.

Mitigation: Install only if the publisher is trusted and the account permissions are appropriate for the intended workflow.

## Reference(s):

- [SF Express Open Platform](https://open.sf-express.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub SF Express Skill Page](https://clawhub.ai/oomol/skills/oo-sf-express)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before actions; state-changing or destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
