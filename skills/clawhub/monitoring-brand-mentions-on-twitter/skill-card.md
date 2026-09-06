## Description:

Monitors and aggregates brand mentions on Twitter/X using apidojo's Tweet and Search scrapers on Apify, returning tweet text, authors, engagement metrics, sentiment signals, and timestamps per mention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Brand managers, PR teams, community managers, and reputation analysts use this skill to collect public Twitter/X mentions for a brand, product, keyword, or competitor set and summarize sentiment, engagement, recurring themes, and high-priority mentions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand search terms and scraper requests are sent to Apify.

Mitigation: Use the skill only when sharing those terms with Apify is acceptable for the brand monitoring task.

Risk: APIFY_TOKEN can be exposed through shell history, logs, or shared command output.

Mitigation: Store the token securely and avoid placing it in logged commands, transcripts, or committed files.

Risk: Downloaded CSV or JSON outputs can contain sensitive operational data derived from public tweet content and metadata.

Mitigation: Limit distribution of exported datasets and handle them according to the organization's data handling policy.

Risk: Keyword-based sentiment labels can miss sarcasm or context in high-impact posts.

Mitigation: Manually review high-engagement positive and negative mentions before taking customer, PR, or escalation actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-brand-mentions-on-twitter)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown report with optional shell commands and CSV or JSON dataset files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sentiment summaries, engagement totals, tweet excerpts, author handles, timestamps, and links to public tweets.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
