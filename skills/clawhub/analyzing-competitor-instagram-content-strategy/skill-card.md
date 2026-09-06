## Description:

Analyzes a competitor's Instagram content strategy and performance using apidojo's Instagram scraper on Apify, returning post frequency, content type mix, top-performing posts, hashtag strategy, and engagement benchmarks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams, social media managers, and brand strategists use this skill to benchmark a competitor's Instagram posting cadence, content mix, engagement patterns, hashtags, and top-performing posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires an APIFY_TOKEN for Apify access.

Mitigation: Store the token in environment variables or trusted MCP tooling and avoid pasting it into shared terminals.

Risk: Scraping competitor Instagram content may be inappropriate for some targets or use cases.

Mitigation: Verify that scraping the selected target content is appropriate before running the workflow.

Risk: Returned Instagram data may be limited, incomplete, or based on follower counts that differ from historical post dates.

Mitigation: Report the actual sample size, extend the analysis window when the sample is small, and verify follower counts before drawing conclusions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/apidojo-io/apidojo-skills/tree/main/skills/intent/analyzing-competitor-instagram-content-strategy)
- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/analyzing-competitor-instagram-content-strategy)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown strategy report with tables, metric summaries, optional shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce JSON or CSV data files when the Apify scraper output is saved before analysis.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
