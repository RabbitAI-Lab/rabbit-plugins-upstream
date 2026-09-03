## Description:

Operate NoxInfluencer creator intelligence and marketing systems through the CLI, including search, analysis, contacts, monitoring, campaigns, CRM, outreach operations, products, affiliation, brand intelligence, exports, account setup, quota, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noxinfluencer](https://clawhub.ai/user/noxinfluencer)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, agencies, and their agents use this skill to operate NoxInfluencer workflows for creator discovery, due diligence, outreach operations, campaign and CRM management, monitoring, exports, and brand intelligence across supported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate NoxInfluencer account workflows that send messages, schedule email, change CRM or campaign data, unlock brand data, retrieve contacts, upload attachments, or create exports.

Mitigation: Review sensitive actions before execution and use approval or dry-run checks for writes, exports, contact retrieval, attachments, and quota-consuming operations.

Risk: Some actions may consume Skill quota, SaaS capability quota, membership entitlements, or email service quota.

Mitigation: Check quota and current tool pricing before broad searches, exports, contact retrieval, unlocks, or other paid operations.

Risk: Approved files or exported contact and campaign data may be exposed through NoxInfluencer workflows.

Mitigation: Confirm the intended recipient, task, file, and export scope before uploads, downloads, sends, schedules, or attachment changes.

## Reference(s):

- [NoxInfluencer Skill Homepage](https://www.noxinfluencer.com/skills)
- [Usage and Billing](https://www.noxinfluencer.com/skills/usage-billing)
- [Brand Monitor Workflows](references/brand-monitor.md)
- [CLI Response Format](references/cli-response-format.md)
- [Marketing Ops Workflows](references/marketing-ops.md)
- [Platform Support](references/platform-support.md)
- [Search Filter Semantics](references/search-filters.md)
- [Verdict Heuristics Reference](references/verdict-heuristics.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain-language responses with CLI-backed results, status summaries, identifiers, and next-step guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce approved file exports, downloaded reports, or JSON body files when a NoxInfluencer workflow requires them.]

## Skill Version(s):

0.1.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
