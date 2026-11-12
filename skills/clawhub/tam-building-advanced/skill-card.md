## Description:

Build a total addressable market in Cargo by combining four company data sources, unifying and classifying accounts, and reporting CRM matches, net-new companies, and estimated market coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations teams, go-to-market engineers, and sales leaders use this skill to build a multi-source TAM in Cargo, compare it with CRM accounts, and assess net-new opportunities and market coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external CLI installation source is unpinned.

Mitigation: Review the package source and pin an approved version before installing.

Risk: Customer domains may be sent to external data sources.

Mitigation: Get approval for the domains and providers before sending customer data.

Risk: Source runs and sample queries may incur costs.

Mitigation: Approve source limits and spend before running samples or syncing data.

Risk: Security analysis was partial for two files and reported 91.7% coverage.

Mitigation: Account for the incomplete inspection and review the affected files before installation.

## Reference(s):

- [TAM Building Advanced on ClawHub](https://clawhub.ai/cargo-ai/skills/tam-building-advanced)
- [Skill source on GitHub](https://github.com/getcargohq/gtm-skills/tree/main/tam-building-advanced)
- [Project homepage](https://github.com/getcargohq/gtm-skills)
- [Configure the sources](references/configure.md)
- [Source comparison](references/sources.md)
- [Run and report](references/run.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, SQL queries]

**Output Format:** [Markdown guidance with TypeScript and Cargo configuration examples, shell commands, and SQL queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapted to the operator's ICP, CRM, Cargo workspace, source limits, and approval decisions]

## Skill Version(s):

0.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
