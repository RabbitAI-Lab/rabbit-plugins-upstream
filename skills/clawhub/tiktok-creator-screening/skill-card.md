## Description:

Helps agents find and assess TikTok creators using public video, creator-post, and comment data for evidence-based KOL shortlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Brand marketers, MCNs, creators, and analysts use this skill to research TikTok creators, compare their public posts and engagement, and review video comments before selecting collaboration candidates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The GUAIKEI API token and TikTok searches, profile URLs, or video IDs are sent to guaikei.com.

Mitigation: Use a scoped token and submit only queries and URLs your team permits the service to receive.

Risk: Locally saved temporary logs may contain sensitive searches or retrieved public comments.

Mitigation: Review and clear temporary logs when the queries or comments are sensitive for your team.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/tiktok-creator-screening)
- [GUAIKEI service](https://www.guaikei.com)
- [Skill options and usage](references/options.md)
- [Release notes](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON data, Analysis guidance]

**Output Format:** [Structured JSON for searches, creator posts, and comments; narrative guidance for reviewing results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON includes status, results, error codes, and warnings; a GUAIKEI API token is required.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
