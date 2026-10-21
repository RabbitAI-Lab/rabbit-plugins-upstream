## Description:

Retrieves public TikTok videos, creator posts, and comments to help agents prepare news briefs and analyze trends and audience reactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brands, and analysts use this skill to research TikTok topics, compare public creator posts, and summarize comment sentiment for briefs and market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The GUAIKEI service receives the API token and TikTok queries, profile URLs, video IDs, or comment targets.

Mitigation: Confirm that the user accepts sending these inputs to GUAIKEI before using the skill; keep the token private.

Risk: Saved result logs may expose usernames, comment text, and research keywords.

Mitigation: Protect local result logs and delete them when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-news-brief)
- [GUAIKEI service](https://www.guaikei.com)
- [Skill usage options](artifact/references/options.md)
- [Research workflow](artifact/references/demand-mining.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown briefs and structured JSON search, post, or comment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include public creator identifiers, comments, engagement metrics, source links, and query warnings.]

## Skill Version(s):

1.0.0 (source: skill frontmatter, package.json, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
