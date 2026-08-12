## Description:

Guaikei XHS Fetcher helps agents search public Xiaohongshu notes, fetch note details and comments, and retrieve creator posts as structured data for content research, competitor analysis, KOL screening, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, market analysts, and developers use this skill to collect public Xiaohongshu keyword, note, comment, and creator-post data through token-authenticated Guaikei API calls for downstream analysis and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, links, and token-authenticated requests to guaikei.com.

Mitigation: Use only with approved data and an authorized GUAIKEI_API_TOKEN; avoid submitting sensitive research terms or links unless that data transfer is acceptable.

Risk: Successful command results are saved locally and may contain fetched comments, URLs, creator information, or research terms.

Mitigation: Review, protect, or delete the logs directory after use according to the sensitivity of the collected data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-fetcher)
- [Guaikei service website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Files]

**Output Format:** [Markdown guidance with Node.js command examples and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results are written to stdout and successful task results are also saved under a local logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata and changelog report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
