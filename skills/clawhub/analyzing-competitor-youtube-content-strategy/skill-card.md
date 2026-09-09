## Description:

Analyzes a competitor's YouTube channel content strategy and performance using apidojo's YouTube scraper on Apify, returning cadence, content mix, top-performing topics, benchmarks, and engagement insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketing teams, YouTube strategists, and brand video teams use this skill to analyze competitor channels, identify high-performing topics, formats, and lengths, benchmark cadence and engagement, and produce a strategy report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify credentials can be exposed if APIFY_TOKEN is placed in URLs, shared transcripts, or checked-in files.

Mitigation: Keep APIFY_TOKEN in a secure environment or secret manager and avoid including it in URLs or shared outputs.

Risk: Broad YouTube scrape requests can consume Apify quota unexpectedly.

Mitigation: Set maxItems to a reasonable limit for the analysis and confirm the intended channel, playlist, search, or Shorts scope before running the scraper.

Risk: A customMapFunction can alter scraped output in ways that affect analysis quality or data handling.

Mitigation: Review any customMapFunction before use and keep transformations limited to the fields needed for the strategy report.

Risk: Small samples, outlier videos, dormant channels, or missing subscriber counts can make competitor benchmarks misleading.

Mitigation: Report the number of videos analyzed, use median alongside mean when outliers exist, flag limited samples, and state when subscriber-based ratios are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/analyzing-competitor-youtube-content-strategy)
- [Apify actor: apidojo/youtube-scraper](https://apify.com/apidojo/youtube-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown strategy report with tables and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save scrape results as JSON or CSV when requested; final analysis should include sample size, analysis date, and caveats for small samples, outliers, or missing subscriber data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
