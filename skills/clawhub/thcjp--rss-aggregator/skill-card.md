## Description:

Automatically reads configured RSS links, fetches and merges multi-source AI news reports, checks push history for duplicates, and generates high-density Markdown briefings without emoji.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent read configured RSS feeds, merge related AI news across sources, remove items already recorded in local history, and produce a concise Markdown briefing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch RSS feeds and article pages from the network.

Mitigation: Use trusted feed sources and run it only in environments where external web access is acceptable.

Risk: The skill may maintain a local pushed_history.log file despite the artifact declaring read-only tooling.

Mitigation: Review the history file location and agent write permissions before deployment.

Risk: Broad trigger keywords may route unrelated requests to this skill.

Mitigation: Review routing rules and narrow trigger terms if the deployment has many overlapping skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/rss-aggregator)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown briefing with article titles, summaries, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update a local pushed_history.log file to support deduplication across runs.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
