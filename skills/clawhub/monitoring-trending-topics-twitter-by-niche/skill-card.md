## Description:

Monitors niche-specific trending topics and conversations on Twitter/X using apidojo's Twitter Search scraper, returning tweet velocity, engagement signals, trend classifications, scores, and top voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External social media managers, PR teams, and content strategists use this skill to monitor emerging Twitter/X conversations in a defined niche and summarize trend strength, relevance, and notable voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires access to an Apify account token and sends selected Twitter/X search terms to Apify.

Mitigation: Keep APIFY_TOKEN in an environment variable or secret manager, prefer the MCP or client-based path, and avoid sharing token-bearing commands or logs.

Risk: Trend monitoring results can be sparse or noisy when search terms are too narrow, filters are restrictive, or returned records are missing key fields.

Mitigation: Broaden search terms, remove secondary filters when needed, apply quality thresholds, and note any records removed for missing fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-trending-topics-twitter-by-niche)
- [ClawHub publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown report with optional JSON or CSV result files and inline shell/API commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes trend classifications, trend velocity scores, engagement signals, summary findings, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
