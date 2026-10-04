## Description:

Helps teams review closed CRM deals each month and propose evidence-backed updates to sales context through a pull request and Slack digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

RevOps, sales leaders, and GTM engineers use this skill to compare won and lost CRM deals, document dated findings and objections, and review proposed context changes before merging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository-controlled instructions may override the agent's safety rules.

Mitigation: Keep repository instructions lower priority than safety rules and review the skill before installing.

Risk: Hourly synchronization can copy broad CRM data, including contact fields, into the workspace.

Mitigation: Limit synchronized CRM fields, especially contacts, before enabling the monthly schedule in a sensitive workspace.

Risk: An unpinned CLI version may change behavior between installations.

Mitigation: Pin the Cargo CLI version and review the deployment plan before enabling the agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/win-loss-review)
- [Project homepage (listed in release metadata)](https://github.com/getcargohq/gtm-skills)
- [CRM audit reference](artifact/references/crm-audit.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown context files and run record, a pull request, and a five-line Slack digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include counts and denominators; a human reviews the pull request before merge.]

## Skill Version(s):

0.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
