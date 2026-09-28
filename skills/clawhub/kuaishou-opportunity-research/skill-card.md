## Description:

Research Kuaishou search results, creator posts, and video comments to identify content, growth, and market opportunities worth further validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, content teams, marketers, and analysts use this skill to collect public Kuaishou keyword search results, creator post lists, and video comments for trend research, competitor monitoring, creator screening, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile links, video links, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Confirm the third-party API and data-sharing terms are acceptable before installing or running the skill.

Risk: Generated local logs may retain sensitive research targets or comment datasets.

Mitigation: Delete, restrict, or protect log files when they contain sensitive business research or user-comment data.

Risk: The skill is limited to public Kuaishou data and can return empty or error results when inputs are invalid, private, removed, or rate-limited.

Mitigation: Check status and error_code before using results in analysis, and do not infer conclusions from failed or empty responses.

## Reference(s):

- [Kuaishou Opportunity Research on ClawHub](https://clawhub.ai/why20261/skills/kuaishou-opportunity-research)
- [Guaikei API access](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results include status, error_code, request metadata, skill metadata, and results; successful runs are also saved to local log files.]

## Skill Version(s):

1.0.0 (source: release evidence, frontmatter, package.json, changelog released 2026-09-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
