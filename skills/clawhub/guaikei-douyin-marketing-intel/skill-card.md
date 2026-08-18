## Description:

Fetches public Douyin data for keyword search, creator post collection, video comment analysis, and real-time trending topic tracking for content research and competitive analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and content analysts use this skill to collect public Douyin search results, creator posts, comments, and trending topics for content research, competitor analysis, user-comment insight, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin research terms, target URLs, and GUAIKEI_API_TOKEN to the third-party guaikei.com API.

Mitigation: Use only approved tokens and workspaces, avoid sensitive search terms or target URLs, and review guaikei.com terms before installation.

Risk: Generated logs may retain comments, user identifiers, profile URLs, and search terms in the local logs directory.

Mitigation: Protect the workspace from unauthorized access and delete or archive logs according to the user's data-retention policy.

Risk: Ambiguous short-video research requests may lead the agent to run Douyin-specific data collection.

Mitigation: Confirm that Douyin is the intended platform before invoking the skill for ambiguous short-video requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-marketing-intel)
- [Guaikei API website](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [CLI request and response schemas](assets/*.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON stdout from CLI commands, stderr logs, and saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and GUAIKEI_API_TOKEN; fetched datasets are automatically written to logs/.]

## Skill Version(s):

1.0.0 (source: evidence release, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
