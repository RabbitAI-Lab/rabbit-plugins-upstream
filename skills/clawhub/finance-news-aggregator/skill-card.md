## Description:

AI and technology news aggregation guidance for collecting, scoring, deduplicating, verifying, and reporting news from 100+ RSS-style sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to structure AI, technology, research, GitHub trend, and finance news summaries with source labels, recency windows, deduplication, and verification checks. Outputs should be reviewed by a human before real-world use, especially for finance-related analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Separately obtained scripts may behave differently from the markdown-only artifact.

Mitigation: Review and scan any Python scripts before running them, and execute only code from trusted sources.

Risk: Finance-related summaries or sentiment analysis may be mistaken for investment, legal, or insurance advice.

Mitigation: Label finance outputs as informational, avoid recommendations, and require human review before any real-world decision.

Risk: News summaries can amplify stale, incorrect, single-source, or unverified claims.

Mitigation: Require source labels, timestamps, recency windows, and cross-verification before treating items as reliable.

Risk: User-deployed RSS or API collection can send queries, IP addresses, and timestamps to third-party services.

Mitigation: Use public sources only, avoid collecting login-gated or authorized content, and follow applicable terms of service and robots.txt rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/finance-news-aggregator)
- [Declared project homepage](https://github.com/lanyasheng/ai-news-aggregator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional command examples and structured report templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference-only guidance; artifact contains no executable scripts and requires human review for outputs.]

## Skill Version(s):

5.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
