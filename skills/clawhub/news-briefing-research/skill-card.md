## Description:

Builds source-aware news briefings from GDELT, BBC, CNN, The Guardian, and Yahoo News using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, editors, and other users gather recent public news, compare coverage across sources, and prepare dated briefings with original links and uncertainty clearly identified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and article URLs are sent to Crawlora's external API.

Mitigation: Avoid sending private, confidential, or sensitive queries or URLs unless permitted by your privacy requirements.

Risk: Different news indexes and update schedules can leave briefings incomplete or misleading.

Mitigation: State the collection window and coverage limits, link original articles, and label unverified claims and corrections.

## Reference(s):

- [News Briefing Research on ClawHub](https://clawhub.ai/crawlora-org/skills/news-briefing-research)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Dated Markdown briefing with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes publication dates, source comparisons, coverage limits, and uncertainty labels.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
