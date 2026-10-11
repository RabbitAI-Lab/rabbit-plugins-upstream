## Description:

Searches public Kuaishou videos, creator posts, and comments to support creator screening and marketing research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, analysts, and agencies use public Kuaishou video, creator, and comment data to shortlist collaborators, review engagement, and research content trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and Kuaishou URLs or IDs are sent to GUAIKEI's third-party API using a GUAIKEI_API_TOKEN.

Mitigation: Use only authorized inputs and a scoped token; confirm that third-party data sharing is acceptable before running commands.

Risk: Returned public video, profile, and comment data is saved locally under logs/.

Mitigation: Keep logs out of source control and shared folders, and delete them when retention is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-creator-screening)
- [GUAIKEI API and token information](https://www.guaikei.com)
- [Command options](references/options.md)
- [Release changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Structured data, Analysis]

**Output Format:** [JSON with optional text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns status and results for searches, public creator posts, or video comments; saves results under logs/.]

## Skill Version(s):

1.0.0 (source: release record, frontmatter, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
