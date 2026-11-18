## Description:

Meta Ads MCP is a production-grade operational guide for creating, managing, optimizing, and documenting Meta (Facebook/Instagram) ad campaigns via the Facebook Ads MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benkalsky](https://clawhub.ai/user/benkalsky)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, agencies, and developers use this skill to plan, create, pause, monitor, and document Meta ad campaigns through MCP-guided workflows while preserving approval, privacy, and account-health controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real advertising operations where wrong account selection, missing spending limits, or premature activation could spend budget or affect live campaigns.

Mitigation: Confirm the ad account, page, pixel, spending limits, and final approval before creating or activating campaigns; create campaign entities in paused status first.

Risk: Custom Audiences, Pixel, and CAPI workflows can involve customer data or regulated personal information.

Mitigation: Use the skill only after confirming customer-data consent, lawful basis, privacy-policy coverage, hashing requirements, opt-out handling, and applicable data-residency obligations.

Risk: Campaign assets and documentation may cross trust boundaries when stored in Google Drive or passed to related copy and image-generation skills.

Mitigation: Use organization-approved storage, verify Drive folder permissions, and apply internal data-handling rules before sharing campaign details with external systems or other skills.

## Reference(s):

- [Meta Ads MCP Skill Page](https://clawhub.ai/benkalsky/skills/meta-ads-mcp)
- [benkalsky Publisher Profile](https://clawhub.ai/user/benkalsky)
- [Account, Architecture & Naming](references/campaign-architecture.md)
- [Budget Strategy & Audience Targeting](references/budget-and-audience.md)
- [Campaign Creation, KPIs & Documentation](references/campaign-operations.md)
- [Ad Formats, Copy & Asset Generation](references/creative-and-copy.md)
- [Pixel/CAPI Tracking & Retargeting](references/tracking-and-retargeting.md)
- [Pre-Campaign Intake Questions](references/intake-questions.md)
- [Safety Guardrails](references/safety-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with checklists, campaign plans, documentation templates, and MCP operation names.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is designed to propose operational steps and campaign documentation; live account actions require user approval and account verification.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
