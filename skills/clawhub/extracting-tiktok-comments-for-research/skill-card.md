## Description:

Extracts and analyzes TikTok comments from public videos or creators using apidojo's TikTok Comments scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Market researchers, brand managers, content creators, and academic researchers use this skill to collect public TikTok comments and summarize audience sentiment, product feedback, top comments, questions, themes, and audience signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok video URLs and public comment datasets are sent to Apify for collection and processing.

Mitigation: Use only data the user is authorized to process, prefer direct video URLs, and disclose the Apify dependency before running the workflow.

Risk: Exported CSV or JSON comment datasets can retain user-generated content longer than necessary.

Mitigation: Store exports only where needed for the research task and delete them when analysis is complete.

Risk: A broad creator request can collect more public comment data than the user intended.

Mitigation: Clarify the research goal and target videos before execution, and use scoped direct video URLs when possible.

Risk: Apify access tokens may allow more actions than this workflow requires.

Mitigation: Use a least-privilege Apify token and keep it in environment configuration rather than embedding it in commands or reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/extracting-tiktok-comments-for-research)
- [Apify TikTok Comments Scraper](https://apify.com/apidojo/tiktok-comments-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research report with tables, plus optional CSV or JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cleaned comment fields such as username, comment text, likes, reply count, timestamp, sentiment, themes, and audience signals.]

## Skill Version(s):

1.0.0 (source: evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
