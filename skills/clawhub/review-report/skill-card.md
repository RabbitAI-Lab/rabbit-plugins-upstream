## Description:

Generates Amazon review analysis reports that collect available ARI review data, summarize VOC themes, trends, variants, competitors, and product-operation insights, and archive reports for later viewing or export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to ask for review summaries, VOC reports, trend analysis, competitor comparisons, negative-review triage, exports, and monitoring guidance from ARI-collected Amazon review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI credits may be spent automatically under server-side confirmation rules.

Mitigation: Use 'only quote, do not execute' for price checks, and set the ARI account to ask before every paid operation before running report workflows.

Risk: Review analysis can be incomplete when ARI has limited samples, stale collection windows, or unclear variant coverage.

Mitigation: Check the reported sample range and treat trend or variant conclusions as limited when the available data is sparse or ambiguous.

Risk: ARI API keys could be exposed if users paste credentials into chat or include them in shared outputs.

Mitigation: Use browser authorization or local configuration, keep keys out of prompts and reports, and stop on authentication errors instead of retrying with exposed credentials.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant Usage Guide](使用说明.md)
- [Account and Authorization Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [Credits and Billing](https://ari.funewa.com/zh/billing)
- [Online Reports](https://ari.funewa.com/zh/reports)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-report)
- [Publisher Profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise chat responses, with optional CSV, Markdown, and HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, report IDs, credit usage, data-scope notes, and confirmation prompts.]

## Skill Version(s):

1.4.11 (source: frontmatter, CHANGELOG, _meta.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
