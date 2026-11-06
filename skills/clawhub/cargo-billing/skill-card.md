## Description:

Reports Cargo credit balances, usage, subscription details, invoices, and payment-method status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to review credit balances, usage by workflow or resource, plan details, invoices, and payment-method status. It also provides guidance for estimating the cost of workflow runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A sample run used for cost estimation can trigger a real workflow, charges, or other external effects.

Mitigation: Require explicit approval for the workflow, record, expected costs, and effects; prefer historical usage or a sandbox.

Risk: Payment card details passed directly to a command may be exposed in shell history or process listings.

Mitigation: Use the hosted payment form instead of giving card details to the agent.

Risk: The external CLI and safeguards in sibling skills were not verified by the security review.

Mitigation: Pin a reviewed CLI version and review the relevant CLI and sibling safeguards before use.

## Reference(s):

- [Cargo Billing on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-billing)
- [Response shapes](artifact/references/response-shapes.md)
- [Usage metrics examples](artifact/references/examples/usage-metrics.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance, Shell commands]

**Output Format:** [Cargo CLI JSON responses summarized as concise text or Markdown, with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports depend on the selected workspace and date range; cost estimates may include a sample workflow run.]

## Skill Version(s):

2.1.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
