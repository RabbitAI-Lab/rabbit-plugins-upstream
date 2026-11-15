## Description:

Pull podcast transcripts on demand and mine them for ideas, trends, and mechanics — without dumping raw transcript into context. Use when the user shares a podcast/episode URL, names a show, or asks what's worth taking from an episode/series. Handles Apple Podcasts, Spotify, YouTube, and RSS feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orensegal](https://clawhub.ai/user/orensegal)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to extract and compare findings, trends, mechanics, and predictions from podcast episodes relevant to a question or project. It records structured findings and produces a shareable report without placing the full transcript in the main conversation context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags undeclared analytics and publishing behavior and network access beyond the stated transcript research purpose; analysis is incomplete.

Mitigation: Address the analytics and publishing behavior, review network safeguards, and complete a behavior review before installation.

## Reference(s):

- [Project homepage](https://github.com/OrenSegal/signal-skills)
- [Recommended podcast sources](artifact/sources.md)
- [Analytics cross-check guide](artifact/analytics-check.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, JSON]

**Output Format:** [Structured findings with confidence tags and source details; HTML or Markdown report; JSON ledger records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include episode and date, confidence tag, topic, and optional speaker attribution.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
