## Description:

Analyzes Amazon review sentiment by theme, separating positive and negative patterns across product dimensions instead of returning only an overall score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to ask natural-language questions about Amazon review sentiment, recurring praise and complaints, topic trends, competitor comparisons, and listing or product improvement opportunities. It can read existing ARI data, generate reports, and guide billing-aware collection or analysis flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad natural-language requests may trigger paid ARI actions or account confirmation setting changes.

Mitigation: Review billing and confirmation settings before installing; ask for quote-only behavior or require confirmation before each credit-spending action when appropriate.

Risk: The skill requires an ARI API key and uses configured account data.

Mitigation: Use the browser authorization flow or local configuration paths, avoid sharing API keys in chat or reports, and install only if the ARI service is trusted for the account involved.

Risk: Automatic confirmation or monitoring can create future paid activity.

Mitigation: Avoid enabling autoconfirm or recurring monitoring unless intentionally desired, and verify cost notes before changing monitoring cadence.

Risk: Review analysis may be limited by sample size, collection window, site coverage, or variant coverage.

Mitigation: Report the sample range, collection window, and known coverage limits, and avoid treating incomplete or historical samples as current market trends.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [Usage Guide](artifact/使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-sentiment)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text responses, with shell command or JSON snippets for advanced setup, troubleshooting, and exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include sentiment summaries, review evidence, trend notes, report links, export guidance, and billing or confirmation prompts.]

## Skill Version(s):

1.4.7 (source: server release evidence, skill frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
