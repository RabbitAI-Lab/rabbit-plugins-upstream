## Description:

Turns a confirmed ideal customer profile into a sized company search and a deployed total addressable market model in Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, go-to-market engineering, and sales leadership teams use this skill to define their target market, estimate the matching company pool, and deploy a reusable company model in Cargo with approval before paid sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing unpinned Cargo CLI or CDK dependencies may introduce supply-chain changes.

Mitigation: Verify dependency sources and pin versions when required by your environment.

Risk: Research may process customer and LinkedIn-derived business data.

Mitigation: Obtain approval to use those data sources and apply your organization's data-handling rules.

Risk: Company sourcing incurs per-record credits, and an unintended deployment or repeat sync may increase spend.

Mitigation: Confirm the filter, result limit, and expected credit cost; review the deployment plan for only the intended connector, folder, and unscheduled model before approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/tam-building)
- [Skill homepage (metadata)](https://github.com/getcargohq/gtm-skills)
- [Source alternatives](references/sources.md)
- [Configuration guide](references/configure.md)
- [Run guide](references/run.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands, Markdown]

**Output Format:** [Markdown guidance and reports with code, configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deploys a reusable Cargo company model after operator approval; sourcing may incur per-record charges.]

## Skill Version(s):

0.5.1 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
