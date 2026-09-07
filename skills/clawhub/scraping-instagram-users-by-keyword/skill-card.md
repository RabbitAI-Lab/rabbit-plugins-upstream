## Description:

Extracts Instagram user profiles, followers, and following lists using apidojo's Instagram User Scraper on Apify, returning account metadata such as username, follower count, bio, post count, verification status, and available public contact fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, outreach teams, and competitive intelligence researchers use this skill to collect Instagram profile datasets by keyword, handle, profile URL, or user ID for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables bulk collection and export of Instagram profile data and public contact fields.

Mitigation: Use only for lawful, authorized research and avoid exporting email or phone fields unless necessary for the approved use case.

Risk: Large or broad scraping runs can increase cost, collect excessive data, and create privacy or platform-compliance exposure.

Mitigation: Keep maxItems narrowly scoped, prefer targeted handles or keywords, and account for Instagram rules and privacy obligations before outreach or dataset building.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/scraping-instagram-users-by-keyword)
- [Apify Instagram User Scraper API Endpoint](https://api.apify.com/v2/acts/apidojo~instagram-user-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON input examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide CSV or JSON exports from the Apify actor; output fields include profile metadata, follower and following counts, verification status, and public contact fields when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
