## Description:

Finds speaking opportunities and event organizer contacts on Twitter/X using apidojo's Twitter scraper, returning event names, organizer handles, topic focus, deadline signals, event size, and submission URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, startup founders, executives, coaches, and consultants use this skill to find and prioritize speaking, podcast guest, summit, panel, keynote, and workshop opportunities from Twitter/X posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends Twitter/X search terms and retrieved public-post data to Apify under the user's Apify account.

Mitigation: Use a scoped Apify token where possible, avoid confidential strategy terms in queries, and review Apify dataset retention and deletion settings.

Risk: Saved local outputs may contain public-post data, opportunity leads, or search strategy details.

Mitigation: Choose output filenames and storage locations carefully, and delete generated datasets when they are no longer needed.

Risk: Speaking opportunity deadlines and classifications can be time-sensitive or incomplete.

Mitigation: Review the generated results before outreach, verify deadlines and submission URLs, and flag expired opportunities.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/apidojo-io/skills/finding-speaking-opportunities-on-twitter)
- [Apify actor: apidojo/tweet-scraper](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, CSV, guidance]

**Output Format:** [Markdown tables and summaries with optional JSON or CSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include classification, relevance scoring, deadline handling, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
