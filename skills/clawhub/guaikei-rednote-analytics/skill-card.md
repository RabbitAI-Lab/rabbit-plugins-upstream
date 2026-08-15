## Description:

Fetches public Xiaohongshu/RedNote search results, note details, creator posts, and comments through Guaikei command-line tools for downstream content, competitor, KOL, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, content operators, market analysts, and agent developers use this skill to collect structured public Xiaohongshu/RedNote data for trend research, competitor monitoring, creator screening, and comment review. It is not intended for private, hidden, or login-gated data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or links, requested result limits, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use the skill only when external API sharing is approved, avoid sensitive searches, and keep the API token scoped and rotated according to local policy.

Risk: Command results can be saved locally under logs/ and may contain public profile, post, or comment data tied to a research target.

Mitigation: Review local log retention, delete sensitive result files when no longer needed, and avoid storing investigations in shared workspaces unless authorized.

Risk: Returned public social data can be misused or interpreted outside platform rules and privacy expectations.

Mitigation: Use returned data for legitimate analysis only, avoid attempts to access private or login-gated content, and review conclusions before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-analytics)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful runs can save JSON results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
