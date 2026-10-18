## Description:

Helps teams find decision-makers who recently joined companies in their target market, qualify those companies against their ideal customer profile, and alert a chosen Slack channel when there is a match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

RevOps, sales-development, and go-to-market engineering teams use this skill to adapt a new-hire monitoring workflow to their market and ICP. Once approved and deployed, it sends qualified job-change alerts to Slack; optional CRM routing requires separate approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unreviewed external dependency or incorrect Slack destination could affect deployment or disclose prospect details.

Mitigation: Review or pin the cargo-cdk dependency, verify the chosen Slack channel, and complete the documented pilot before enabling scheduled runs.

Risk: Large or frequent searches can incur unexpected extraction costs.

Mitigation: Confirm each search size, cadence, and estimated cost before approval.

Risk: Optional CRM routing can create incorrect records or act on untrusted LinkedIn data.

Mitigation: Keep CRM routing off until generated writes, deduplication policy, and prompt-injection protections have been reviewed.

## Reference(s):

- [New-hire detection skill homepage](https://github.com/getcargohq/gtm-skills/tree/main/new-hire-detection)
- [Cargo GTM skills documentation](https://github.com/getcargohq/gtm-skills)
- [Shape the search](references/search.md)
- [Run the pilot](references/run.md)
- [Optional CRM adaptation](references/crm-adaptation.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Text]

**Output Format:** [Markdown guidance and adapted TypeScript resources; Slack alert text after deployment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Alerts identify the new hire and company and include an ICP verdict and links; CRM writes are optional.]

## Skill Version(s):

0.1.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
