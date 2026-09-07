## Description:

Scrapes Twitter/X profile data for lists of usernames using apidojo's Twitter User scraper on Apify and returns account metadata such as bios, follower counts, verification status, and profile URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Data analysts, market researchers, and list-enrichment developers use this skill to bulk-fetch Twitter/X profile metadata for supplied usernames and export the resulting dataset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X targets and actor inputs are sent to Apify for third-party processing.

Mitigation: Use the skill only when that data sharing is acceptable for the intended workflow and dataset.

Risk: APIFY_TOKEN could be exposed through pasted commands, logs, or unsafe local configuration.

Mitigation: Store APIFY_TOKEN as a protected environment secret and avoid including tokens in shared command output or logs.

Risk: Exports may contain Twitter/X profile data, including profile metadata and account status details.

Mitigation: Choose output paths deliberately, restrict access to exported CSV or JSON files, and handle profile datasets according to applicable data policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-twitter-profiles)
- [Apify actor: apidojo/twitter-user-scraper](https://apify.com/apidojo/twitter-user-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands, JSON input examples, and tabular dataset output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CSV or JSON exports of Twitter/X profile datasets when the Apify actor is run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
