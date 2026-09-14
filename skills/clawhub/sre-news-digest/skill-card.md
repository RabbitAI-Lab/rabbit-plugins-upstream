## Description:

Generate categorized and rated SRE, DevOps, and Solution Architecture news digests from sre.news with expert scoring and Markdown output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[imzye](https://clawhub.ai/user/imzye)

### License/Terms of Use:

MIT-0

## Use Case:

SRE, DevOps, and solution architecture practitioners use this skill to collect recent sre.news items, read linked articles, rate relevance, categorize topics, and generate an English Markdown digest for daily or periodic review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The digest depends on a disclosed RSS mirror, so feed availability or mirror completeness can affect article selection.

Mitigation: For important digests, compare feed results with sre.news or the original article sources before relying on the output.

Risk: The workflow asks the agent to open external article links supplied by the feed.

Mitigation: Use an isolated browsing environment without sensitive sessions, avoid unrelated embedded resources, and review generated links before sharing externally.

## Reference(s):

- [Server-resolved GitHub source repository](https://github.com/imzye/sre-news-digest)
- [ClawHub skill page](https://clawhub.ai/imzye/skills/sre-news-digest)
- [SRE News](https://sre.news)
- [SRE News RSS mirror](https://news.imzye.com/rss.xml)
- [SRE/DevOps News Scoring Rubric](references/scoring-rubric.md)
- [Digest Template](templates/digest_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown digest with article links, source names, ratings, category sections, and short expert summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper script can also emit a JSON article list before the agent reads, rates, categorizes, and formats the digest.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
