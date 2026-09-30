## Description:

Produces quarter-organized research briefs on US stock earnings, combining reported results, management guidance, call summaries, filing changes, market context, and dated signals from SentiSense.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and researchers use this skill to review a company's earnings by fiscal quarter or survey recent and upcoming US earnings events. The output is research, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API credential is required to retrieve earnings research.

Mitigation: Provide a SentiSense API key only if comfortable with read-only SentiSense data calls; keep the key private.

Risk: Incomplete, delayed, or AI-generated financial summaries could mislead investment decisions.

Mitigation: Check fiscal periods, report dates, source citations, and coverage gaps; verify consequential decisions independently and do not treat the analysis as investment advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Dated Markdown earnings analysis and previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quarter- and report-date labels, source citations, coverage and data-availability notes, and a research-only disclaimer.]

## Skill Version(s):

1.4.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
