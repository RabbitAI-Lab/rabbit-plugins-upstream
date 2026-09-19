## Description:

Generates Amazon review analysis, VOC reports, trend summaries, competitor comparisons, and exportable report artifacts from ARI-collected review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to turn ASIN review data into concise issue summaries, VOC reports, trend analysis, competitor comparisons, listing suggestions, and archived reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI analysis or collection flows can spend credits, including automatic execution under account auto-confirm rules.

Mitigation: Use quote-only or ask-before-every-charge instructions before report generation, and review any auto-confirm settings.

Risk: Monitoring, watch, schedule, and auto-confirm changes can affect future account behavior and costs.

Mitigation: Confirm schedule, watch, and auto-confirm changes explicitly and review reported costs before enabling ongoing behavior.

Risk: Reports depend on ARI-collected Amazon review samples and may not cover every review, variant, or time window.

Mitigation: Treat conclusions as sample-based business analysis and verify important decisions with the stated data range and additional evidence when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-report)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Natural-language summaries and Markdown reports with optional links, HTML exports, and CSV exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some analysis and collection flows consume ARI credits and may auto-confirm under server-side account rules.]

## Skill Version(s):

1.4.13 (source: server evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
