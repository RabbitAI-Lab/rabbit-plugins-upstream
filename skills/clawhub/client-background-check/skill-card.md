## Description:

Helps sales and BD users produce procurement-focused customer background reports from Zhiliaobiaoxun tender data, including customer profiles, purchasing history, supplier relationships, bid strength, competitors, public-risk checks, and optional two-company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, BD, procurement, and bidding teams use this skill before customer meetings, supplier reviews, or competitive analysis to understand an organization's public tender history, budgets, suppliers, customers, competitors, and disclosed risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives company names and query parameters submitted for background checks.

Mitigation: Use the skill only for queries suitable for the vendor service and avoid submitting sensitive internal strategy or confidential customer context.

Risk: Auto-registration may send a hashed device identifier and creates local credential state.

Mitigation: Preconfigure ZLBX_API_KEY to skip auto-registration, require explicit user consent before registration, and treat ~/.zlbx/config.json as sensitive.

Risk: Generated reports and raw API links may contain signed login-bypass parameters.

Mitigation: Share reports and links only with intended recipients and preserve the skill's warnings about signed links.

Risk: Procurement intelligence and public-risk sections can be incomplete or misread as definitive claims about real organizations.

Mitigation: State data boundaries, cite sources for public-risk statements, separate facts from inference, and avoid unsupported allegations or legal conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/client-background-check)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](references/api-quick.md)
- [Seven-step workflow guide](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown report with optional generated HTML report path and concise account or API-key guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or explicit user consent for auto-registration; reports can include API-returned signed links and should preserve stated data boundaries.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
