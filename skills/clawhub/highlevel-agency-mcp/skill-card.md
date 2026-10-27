## Description:

Automates GoHighLevel funnel and website layouts, domain onboarding, forms, workflows, spam protection, IVRs, and sub-account snapshot diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

Agency operators and developers use this skill to inspect and manage GoHighLevel accounts, including pages, domains, forms, workflows, access roles, telephony, and snapshot audits. Confirm the target sub-account and environment before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account gives the hosted MCP operator the access granted to that connection.

Mitigation: Use a narrowly scoped account connection and restrictive write policy.

Risk: Changes to live account assets, domains, or staff access could have unintended effects.

Mitigation: Confirm the target sub-account and environment, then review the dry-run preview before applying changes.

## Reference(s):

- [HighLevel Agency & Builder MCP](https://ghlagencymcp.com/)
- [HighLevel Agency & Builder MCP endpoint](https://ghlagencymcp.com/mcp)
- [Public plugin repository](https://github.com/mooshee/highlevel-agency-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Configuration, Text]

**Output Format:** [Markdown and structured configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect or update connected GoHighLevel assets according to the selected account and write policy.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
