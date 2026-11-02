## Description:

Read-only access to public Douyin search, creator posts, comments, and trending lists, returning structured JSON for content planning, competitor monitoring, public-opinion analysis, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External users, social-media operators, brand marketers, analysts, and support teams use this skill to search public Douyin content, inspect creator posts and comments, retrieve trends, and produce structured data for planning and monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and links are sent to Guaikei, and retrieved public profile and comment data are saved locally.

Mitigation: Check the provider's pricing, protect the API token, send only intended search terms and links, and delete saved logs when no longer needed.

## Reference(s):

- [Guaikei service and token access](https://www.guaikei.com)
- [CLI options](references/options.md)

## Skill Output:

**Output Type(s):** [JSON data, Files]

**Output Format:** [Structured JSON in command output and saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Douyin search, creator-post, comment, and trending results are saved locally for later analysis.]

## Skill Version(s):

1.4.0 (source: SKILL.md frontmatter, package.json, changelog; released 2026-10-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
