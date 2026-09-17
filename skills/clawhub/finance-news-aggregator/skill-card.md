## Description:

AI/technical news aggregation skill for concurrent RSS collection, interest scoring, cross-day deduplication, and unified prefetching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to gather, rank, deduplicate, summarize, and template AI, technical, paper, GitHub trend, and finance-news updates. Outputs are advisory and require human review before operational or market-facing use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-impact or sentiment-risk summaries may be mistaken for financial advice.

Mitigation: Treat outputs as informational only, verify sources manually, and do not use the skill as the basis for investment decisions.

Risk: News aggregation and summarization can surface stale, inaccurate, duplicated, or low-confidence source material.

Mitigation: Apply the skill's source grading, time-window rules, deduplication guidance, and human review before publishing or acting on summaries.

Risk: If users independently deploy the referenced RSS or API scripts, third-party services may receive request metadata such as queries, IP addresses, or timestamps.

Mitigation: Use only public sources, follow source terms and robots.txt rules, and avoid sending credentials, private data, or unnecessary personal information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/finance-news-aggregator)
- [Declared project homepage](https://github.com/lanyasheng/ai-news-aggregator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, report templates, and optional JSON output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include source labels, time windows, recency constraints, and human-review caveats.]

## Skill Version(s):

5.0.4 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
