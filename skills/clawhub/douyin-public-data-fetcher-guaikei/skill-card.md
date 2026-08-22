## Description:

Searches public Douyin keywords, creator posts, video comments, and real-time hot lists for content research, competitor analysis, comment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to run Node.js command-line tools that fetch public Douyin search results, creator posts, comments, and trending topics for internal content research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can bulk-collect public Douyin user, post, and comment data.

Mitigation: Run it only for explicit Douyin research requests and confirm the intended use complies with Douyin platform terms and applicable law.

Risk: The skill sends Douyin search terms, profile or video URLs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install and run it only when that data transfer is acceptable, and provide the token only through the documented environment variable.

Risk: Complete fetched results are saved under the skill's local logs directory by default.

Mitigation: Review or delete local logs after use and avoid sensitive research targets unless local retention is acceptable.

Risk: Server security evidence marked the release as suspicious and needing review.

Mitigation: Review and scan the skill before deployment, with particular attention to local logging, token handling, and data collection behavior.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/engheng-art/skills/douyin-public-data-fetcher-guaikei)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration]

**Output Format:** [JSON on stdout, logs and status messages on stderr, and saved JSON result logs under the local logs directory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN in the environment.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
