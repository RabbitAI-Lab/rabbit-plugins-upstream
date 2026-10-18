## Description:

Reviews closed CRM deals each month to propose evidence-backed ICP, insight, objection, and client updates in a pull request and share a brief Slack digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales teams use this skill to compare won and lost CRM deals, review proposed changes to their GTM context in a pull request, and receive a monthly Slack summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad CRM extraction copies deal, account, and contact records into Cargo storage.

Mitigation: Approve the data scope first and consider field allowlists or sanitized CRM views.

Risk: Repository write access and a recurring run can introduce unwanted context changes.

Mitigation: Review the repository binding, narrow repository-convention precedence, and require human pull-request review before merging.

Risk: The Slack digest could expose deal information in an unintended channel.

Mitigation: Verify the locked Slack channel before deployment and keep it out of customer-shared channels.

Risk: Unpinned CLI installation and hourly CRM sync can change behavior or data exposure over time.

Mitigation: Pin the CLI version and confirm that the hourly sync schedule is acceptable.

## Reference(s):

- [CRM audit and adaptation guide](references/crm-audit.md)
- [Project homepage (listed in ClawHub metadata)](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown context and audit files in a pull request, plus a five-line Slack digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Counts include denominators; a human reviews and merges proposed changes.]

## Skill Version(s):

0.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
