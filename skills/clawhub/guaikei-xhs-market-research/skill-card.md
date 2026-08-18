## Description:

Fetches public Xiaohongshu content, note details, creator post lists, and comments through Guaikei command-line tools for market research and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brand marketers, market researchers, and analysts use this skill to collect structured public Xiaohongshu search results, note details, creator post lists, and comments for trend discovery, competitor monitoring, KOL screening, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or links and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only approved inputs and tokens, and confirm that sending this data to Guaikei is acceptable for the user's organization or project.

Risk: Successful runs save fetched public post and comment data under local logs.

Mitigation: Treat log files as retained local records; review, protect, or delete them according to the user's data-retention requirements.

Risk: Large result limits can create bulk collections of public platform data.

Mitigation: Prefer the smallest useful limit and use bulk collection only when it is authorized and necessary for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-market-research)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Command guidance and structured JSON results saved as local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword, note URL, creator profile URL, filters, sorting, time range, and result limits.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact package and frontmatter report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
