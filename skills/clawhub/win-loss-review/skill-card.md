## Description:

Reviews closed CRM deals each month to document win-loss patterns, update sales context through a pull request, and post a short Slack digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales leaders use this skill to compare won and lost CRM deals, document evidence-backed ICP insights and objections, and review monthly updates before merging them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full CRM records, including contacts and open deals, are stored in Cargo even though the review focuses on closed deals.

Mitigation: Confirm data handling is acceptable before installation and narrow extracted fields or records where possible.

Risk: Repository conventions can override the agent's instructions in a shared repository.

Mitigation: Remove the instruction giving repository conventions priority over the agent prompt before deployment.

Risk: A scheduled agent can open pull requests and post deal findings to Slack.

Mitigation: Review the deployment plan, lock Slack posting to an internal channel, and require human review before merging pull requests.

Risk: Installing the latest CLI version can introduce unreviewed changes.

Mitigation: Pin the Cargo CLI version used for installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/win-loss-review)
- [Project homepage](https://github.com/getcargohq/gtm-skills)
- [CRM audit reference](references/crm-audit.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown context files and run record, pull request, and five-line Slack digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include counts and denominators; repository changes require human review before merging.]

## Skill Version(s):

0.1.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
