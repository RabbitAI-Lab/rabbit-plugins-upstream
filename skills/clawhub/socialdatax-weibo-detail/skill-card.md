## Description:

Retrieves and organizes details and engagement metrics for a Weibo post.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts can retrieve a Weibo post's content, author, publishing time, media details, and interaction counts for research or content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External package behavior may change between uses.

Mitigation: Use a reviewed, fixed package version and limit CLI access to unrelated files and secrets.

Risk: Requested post identifiers or URLs and usage attribution are sent to SocialDataX, and data calls may consume service credits.

Mitigation: Provide only intended post references and confirm service-credit use before making a lookup.

Risk: Media downloads write files to a local destination.

Mitigation: Choose the output path explicitly; media downloads do not require the API key.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [Structured JSON post details with concise Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post content, author, media, interaction counts, publish time, and post URL when available.]

## Skill Version(s):

0.1.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
