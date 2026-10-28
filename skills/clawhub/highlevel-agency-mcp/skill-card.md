## Description:

Automate GoHighLevel (GHL) funnel and website page layouts, client domain DNS & SSL onboarding, multi-step forms, workflow graphs, LeadShield contact form spam & B2B solicitation blockers, spam-shield IVRs, and sub-account snapshot diffs using HighLevel Agency & Builder MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

GoHighLevel agency teams and administrators use this skill to inspect, build, update, and verify client funnels, websites, domains, forms, workflows, phone settings, and sub-account configurations. It supports day-to-day account operations and pre-launch audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to live funnels, domains, workflows, staff access, or phone settings can affect production accounts.

Mitigation: Confirm the target sub-account and whether it is a sandbox or production account; start with read-only access, review previews, and verify changes after applying them.

Risk: Connecting the hosted MCP provider gives it access to operations on the connected GoHighLevel account.

Mitigation: Use narrowly scoped credentials and connect only accounts authorized for the requested work.

## Reference(s):

- [HighLevel Agency & Builder MCP](https://ghlagencymcp.com)
- [HighLevel Agency & Builder MCP endpoint](https://ghlagencymcp.com/mcp)
- [Public plugin repository](https://github.com/mooshee/highlevel-agency-mcp)
- [ClawHub skill page](https://clawhub.ai/mooshee/skills/highlevel-agency-mcp)

## Skill Output:

**Output Type(s):** [Analysis, Configuration, Guidance]

**Output Format:** [Natural-language status summaries, change previews, audit findings, and account configuration updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live account changes should be previewed and verified; the skill requires confirmation of the target sub-account and environment before mutation.]

## Skill Version(s):

1.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
