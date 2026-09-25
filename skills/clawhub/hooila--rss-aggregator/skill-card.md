## Description:

Aggregates configured RSS feeds, fetches article content, merges related reports, filters previously pushed items, and produces a concise daily AI news briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hooila](https://clawhub.ai/user/hooila)

### License/Terms of Use:


## Use Case:

Editors, operators, and agents use this skill to turn a configured RSS source list into a de-duplicated Markdown briefing for repeated daily AI news pushes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches RSS and article content from configured external sources, so briefing quality depends on source reliability and relevance.

Mitigation: Review and maintain rss_sources.txt before use, and verify important claims before redistribution.

Risk: The skill maintains a local pushed_history.log containing pushed titles and links for de-duplication.

Mitigation: Use an explicit storage path and retention limit when running the skill frequently.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hooila/skills/rss-aggregator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown briefing with title, summary, and source-link fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No emoji; hides RSS source names; records pushed titles and links for de-duplication.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
