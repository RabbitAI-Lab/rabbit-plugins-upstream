## Description:

Scrapes Instagram profile statistics and optional recent post metrics for account lists using Apify's apidojo Instagram scraper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to collect Instagram profile statistics and optional recent post metrics for influencer vetting, brand research, and list enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested Instagram targets and retrieved profile or post data are sent to Apify/Apidojo.

Mitigation: Use the skill only when third-party processing is permitted for the requested targets and resulting data.

Risk: Broad URL inputs may collect more Instagram data than intended.

Mitigation: Prefer profile handles or profile URLs unless broader scraping is deliberate.

Risk: APIFY_TOKEN can be exposed through command history, logs, or shared output.

Mitigation: Keep APIFY_TOKEN out of logs where possible and avoid sharing commands or files that contain the token.

Risk: Saved CSV or JSON exports may contain profile and post data that needs controlled handling.

Mitigation: Store, share, or delete exported files according to the user's data-handling rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-instagram-profile-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command, JSON request, table, CSV, and JSON export examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces structured Instagram profile datasets with account statistics, profile metadata, and optional recent post metrics.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
