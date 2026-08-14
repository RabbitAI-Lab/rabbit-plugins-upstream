## Description:

Analyzes A-share and Hong Kong-listed companies from a company name or ticker, then produces a structured company research report and investment briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pm2-567](https://clawhub.ai/user/pm2-567)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users, investors, research analysts, and investment teams use this skill to perform initial A-share and Hong Kong equity research, including company profiling, industry structure, moat analysis, financial review, and relative valuation. It can run a full six-step workflow or narrower company-profile and financial-analysis modes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, tickers, and lookup terms may be sent to public finance and search providers.

Mitigation: Use the skill only for data that can be shared with those providers, or run it in an environment with approved network controls and provider allow lists.

Risk: Generated reports and temporary JSON files may be written locally and retained by the host environment.

Mitigation: Apply the organization's retention policy to report outputs and clear temporary data after use, especially in managed or confidential research workflows.

Risk: Dependency and browser asset hygiene may matter in controlled environments.

Mitigation: Update dependency minimums during deployment review and prefer a local copy of html2canvas instead of loading it from a public CDN.

## Reference(s):

- [Skill README](README.md)
- [Financial Analysis Guide](references/financial-analysis-guide.md)
- [Moat Analysis Framework](references/moat-analysis-framework.md)
- [Porter Five Forces Template](references/porter-five-forces-template.md)
- [Relative Valuation Methods](references/valuation-methods.md)
- [Company Profile Template](templates/company-profile-template.md)
- [Deep Analysis Report Template](templates/deep-analysis-report-template.md)
- [Financial Analysis Template](templates/financial-analysis-template.md)
- [Briefing Card Template](templates/briefing-card-template.html)
- [ClawHub Skill Page](https://clawhub.ai/pm2-567/skills/company-deep-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, html, json, shell commands, guidance]

**Output Format:** [Markdown reports, HTML briefing cards, local JSON data files, and inline command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full mode emits a Markdown deep analysis report and an HTML investment briefing; single-step modes emit one focused Markdown report.]

## Skill Version(s):

1.0.12 (source: frontmatter, changelog, server release; changelog released 2026-08-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
