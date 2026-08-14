## Description:

guaikei-viral helps agents retrieve and analyze public Xiaohongshu notes, comments, keyword results, and creator posts through Guaikei API-backed Node.js commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, marketers, analysts, and agents use this skill to search Xiaohongshu public content, inspect note details and comments, and monitor creator posts for trend research, competitive analysis, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu note URLs, profile URLs, and token-backed API requests are sent to the third-party Guaikei service.

Mitigation: Use the skill only for data you are allowed to share with guaikei.com, and avoid submitting confidential research targets or sensitive client information.

Risk: Command results are saved locally under logs/ and may contain competitive research, comments, URLs, or other sensitive analysis inputs.

Mitigation: Review, protect, or delete generated log files after use, especially in shared workspaces or regulated environments.

Risk: The skill is limited to public Xiaohongshu data and depends on a valid GUAIKEI_API_TOKEN and third-party API availability.

Mitigation: Confirm the token and network path before use, handle empty or failed API responses as non-results, and do not infer private or hidden platform data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-viral)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Markdown, Guidance, Configuration]

**Output Format:** [Markdown guidance with Node.js shell commands; successful CLI runs return structured JSON and save result files under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; requests are sent to guaikei.com.]

## Skill Version(s):

1.0.0 (source: artifact metadata, package.json, changelog, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
