## Description:

Collects public Kuaishou data by searching videos, retrieving creator posts, and fetching video comments, returning structured JSON for content research, competitor monitoring, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to collect public Kuaishou video, creator, and comment data for topic research, competitor monitoring, KOL screening, and public-opinion analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou keywords, profile or video URLs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use the skill only when that data transfer is acceptable, keep the token in a trusted environment, and avoid submitting sensitive searches or links.

Risk: Retrieved public data is saved locally under the skill's logs directory.

Mitigation: Delete local log files after use when searches or results are sensitive, especially on shared machines.

Risk: The skill is limited to public Kuaishou data and does not support private, hidden, or login-only content.

Mitigation: Use it only for authorized public-data workflows and do not treat missing or empty results as evidence that private content does not exist.

## Reference(s):

- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and saves retrieved public-data results under the local logs directory.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, frontmatter, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
