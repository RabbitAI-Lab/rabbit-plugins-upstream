## Description:

Operates Razorpay through OOMOL's oo CLI connector for reading, creating, and updating Razorpay data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Razorpay action schemas, retrieve orders and payments, create orders, and issue refunds through an OOMOL-connected Razorpay account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Razorpay request and response data is routed through OOMOL's third-party connector.

Mitigation: Install only when that routing is acceptable and grant the connected Razorpay account only the permissions needed for the intended work.

Risk: The skill documents remote installer commands that execute downloaded code.

Mitigation: Use a verified and pinned installer, or review and verify the downloaded script before execution.

Risk: Order creation and refund actions can change Razorpay state.

Mitigation: Confirm exact amounts, currencies, payment IDs, refund details, and metadata with the user before running write actions.

## Reference(s):

- [ClawHub Razorpay skill page](https://clawhub.ai/oomol/skills/oo-razorpay)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Razorpay homepage](https://razorpay.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
