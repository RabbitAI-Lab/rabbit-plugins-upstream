## Description:

Monitors Instagram for brand mentions and tagged posts using apidojo's Instagram scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External brand managers, social listening teams, PR agencies, and community managers use this skill to collect public Instagram posts that mention a brand, classify mention type and sentiment, and prepare a brand health report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram monitoring keywords, hashtags, URLs, and scraped post data may be sent to Apify or stored locally.

Mitigation: Collect only what is needed, keep CSV and JSON exports in access-controlled locations, and follow applicable platform, privacy, and business policies.

Risk: Sentiment and mention-type classification can be wrong for complex, mixed, ambiguous, or non-English posts.

Mitigation: Review mixed, high-reach, complaint, and non-English posts before using the report for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-instagram-brand-mentions)
- [Apify Instagram scraper run endpoint](https://api.apify.com/v2/acts/apidojo~instagram-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands, tables, JSON examples, and reporting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CSV or JSON export instructions for collected Instagram post data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
