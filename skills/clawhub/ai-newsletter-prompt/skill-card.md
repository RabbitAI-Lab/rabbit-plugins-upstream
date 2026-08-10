## Description:

Generates a daily AI news digest from fresh web sources, with configurable article count, topic focus, inline Markdown delivery, optional file output, and JSON-style article data when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and AI practitioners use this skill to collect, verify, rank, and summarize recent AI and machine-learning news into a concise daily briefing or newsletter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill searches and fetches live web pages, so source availability, freshness, paywalls, and failed fetches can affect the digest.

Mitigation: Review the cited sources and warnings in the generated digest, and use the skill's verification and fallback behavior to skip weak or inaccessible articles.

Risk: Optional file output can save a generated newsletter to persistent output storage.

Mitigation: Choose inline output unless a saved Markdown file is needed, and review the generated file before sharing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/ai-newsletter-prompt)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [text, markdown, files, JSON, guidance]

**Output Format:** [Markdown digest, optional saved Markdown file, or JSON article list when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include article titles, source URLs, summaries, relevance scores, publication dates, source query, and warnings about skipped or failed fetches.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
