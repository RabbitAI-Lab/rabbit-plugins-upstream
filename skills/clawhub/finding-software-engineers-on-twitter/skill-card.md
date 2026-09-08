## Description:

Finds software engineers and developers to recruit using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Technical recruiters, startup hiring managers, and engineering talent acquisition teams use this skill to discover and qualify software engineering candidates from public Twitter/X activity by tech stack, role signals, and open-to-work indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses an Apify API credential.

Mitigation: Store APIFY_TOKEN securely and avoid exposing it in command history, logs, shared terminals, or exported artifacts.

Risk: The workflow processes public profile data for recruiting.

Mitigation: Use it only when approved for recruiting searches, limit result volumes and exports, and protect or delete candidate files according to privacy and recruiting policies.

Risk: Local helper scripts or generated commands may be run during collection.

Mitigation: Review any local helper script or command before execution and scan outputs before deployment or sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-software-engineers-on-twitter)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor: apidojo/twitter-user-scraper](https://apify.com/apidojo/twitter-user-scraper)
- [Apify actor: apidojo/tweet-scraper](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown candidate summaries and tables with inline shell/API examples; optional CSV or JSON result files when saved by the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include candidate handles, names, inferred tech stack, follower counts, activity signals, scores, and open-to-work indicators.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
