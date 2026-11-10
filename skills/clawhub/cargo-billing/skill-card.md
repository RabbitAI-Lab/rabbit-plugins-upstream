## Description:

Reports Cargo credit balances, usage by workflow, connector, or agent, subscription details, and invoices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace administrators use this skill to review Cargo credit balances, usage, plans, invoices, and payment methods, and to estimate workflow costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious: its summary says the estimate feature can launch a live workflow, and some reported capabilities do not clearly match the stated billing purpose. The scan is partial because some references could not be resolved.

Mitigation: Consider avoiding installation unless the skill is needed and its live workflow risks are acceptable. Prefer historical usage or a non-executing estimate; before any live estimate, confirm the exact workflow, inputs, possible charges, and external effects, and account for the scan's incomplete coverage.

## Reference(s):

- [Usage metrics examples](references/examples/usage-metrics.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/cargo-billing)
- [Project homepage (metadata)](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Text, Analysis, Shell commands, Guidance]

**Output Format:** [Natural-language billing summaries with shell command examples and JSON response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include usage breakdowns, credit estimates, and billing guidance.]

## Skill Version(s):

2.1.5 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
