## Description:

This skill retrieves public TikTok videos, creator posts, and video comments as structured JSON for read-only analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

Creators, marketers, and researchers use it to search public TikTok videos, review creators’ posts, and inspect video comments for topic research, competitor monitoring, and audience sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and submitted TikTok links are sent to the third-party Guaikei service, and API usage may incur charges.

Mitigation: Use a dedicated API token and review the service’s data handling and pricing before submitting sensitive terms or links.

Risk: When local logging is enabled, queries and results may be retained in temporary-directory log files.

Mitigation: Keep logging disabled unless local copies are needed, and protect any logs that are created.

## Reference(s):

- [Guaikei service and support](https://www.guaikei.com)
- [TikTok data skill options](references/options.md)
- [TikTok data skill changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON data, Analysis]

**Output Format:** [Structured JSON envelope containing TikTok video, creator-post, or comment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result counts and available fields depend on public data and API plan limits; empty result arrays are valid.]

## Skill Version(s):

1.1.1 (source: frontmatter, package.json, changelog, released 2026-11-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
