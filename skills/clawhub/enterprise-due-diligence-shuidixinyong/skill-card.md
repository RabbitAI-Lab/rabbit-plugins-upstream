## Description:

A company due-diligence skill that helps users evaluate prospective partners, suppliers, customers, or competitors using public bidding data, company profiles, partner relationships, competitor overlap, and public risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and analysts use this skill to run lightweight pre-cooperation due diligence on companies before contracting, credit, supplier, customer, or competitive decisions. It produces single-company reports and two-company comparisons grounded in bid records, company data, public links, and stated data gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional auto-registration sends a stable MAC-derived device hash.

Mitigation: Use a preconfigured ZLBX_API_KEY to skip auto-registration, or approve registration only when device-hash use for trial-account deduplication is acceptable.

Risk: Generated reports may preserve login-bypass links returned by the data service.

Mitigation: Treat generated Markdown and HTML reports as access-bearing artifacts and share them only with intended recipients.

Risk: The skill may store an API key in local configuration.

Mitigation: Restrict local config permissions and rotate or revoke the key if the configuration or generated reports are exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/enterprise-due-diligence-shuidixinyong)
- [Skill definition](artifact/SKILL.md)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report in chat with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; generated reports may include source links returned by the data service.]

## Skill Version(s):

1.0.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
