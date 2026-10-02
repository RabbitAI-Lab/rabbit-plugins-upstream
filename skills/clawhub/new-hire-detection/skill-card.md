## Description:

Guides teams to watch for new hires in their target market, qualify their companies against an ideal customer profile, and post matching alerts to Slack, with optional CRM integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales development teams use this skill to configure a recurring new-hire search, qualify the companies new hires join, and alert their team in Slack. CRM lookup or routing is an optional adaptation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qualification errors or misplaced alerts may expose lead details to the wrong Slack audience.

Mitigation: Review the qualification workflow with the channel owner, verify the channel ID, and start with a small pilot in a private, access-controlled channel.

Risk: Optional CRM routing can create or change records for the wrong account if matching is imprecise.

Mitigation: Keep the Slack-only default until CRM routing is approved; require exact, reviewed account matching and a reversible or dry-run-tested write path. Replace Salesforce contains-domain matching before scheduled use.

Risk: Recurring searches can incur repeated extraction costs.

Mitigation: Count and price the search before extraction, run the unscheduled pilot first, and obtain approval for the search limit and cadence.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/new-hire-detection)
- [Publisher-listed project homepage](https://github.com/getcargohq/gtm-skills)
- [Shape the search](references/search.md)
- [Run the pilot](references/run.md)
- [Add the CRM](references/crm-adaptation.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with TypeScript and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapt the example to the team's market and ICP; the default pilot ends with Slack alerts and makes no CRM changes.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
