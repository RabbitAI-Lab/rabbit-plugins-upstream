## Description:

Searches English-language social platforms, including Reddit posts, Twitter/X tweets, and YouTube videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run targeted social search queries across Reddit, Twitter/X, and YouTube and return normalized JSON results for downstream analysis or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to external services including Reddit, TikHub, and Google/YouTube.

Mitigation: Use the skill only when external platform requests are acceptable for the query and environment.

Risk: Twitter/X and YouTube searches require API credentials that could be exposed through command history or logs.

Mitigation: Use limited-scope credentials where possible and pass secrets through environment variables instead of shared shell history or reports.

Risk: The dependency requirement allows httpx versions at or above 0.27 without an upper bound.

Mitigation: Pin and review httpx before operational deployment in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-social-en)
- [Publisher profile](https://clawhub.ai/user/sensenova-skills)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and shell commands; helper scripts emit JSON search results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results use a standard JSON shape with success, query, provider, items, and error fields.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
