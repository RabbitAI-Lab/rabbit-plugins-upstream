## Description:

Searches public Xiaohongshu notes, retrieves note details and comments, and tracks public creator posts so agents can collect structured data for trend discovery, competitor analysis, KOL screening, and marketing research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, content creators, marketers, and analysts use this skill to collect public Xiaohongshu search results, note details, comments, and creator post lists for research, reporting, content planning, and competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and token-authenticated requests are sent to Guaikei's third-party API.

Mitigation: Use the skill only when this data sharing is acceptable, configure GUAIKEI_API_TOKEN through the environment, and avoid submitting sensitive or private targets.

Risk: CLI results are saved as local JSON logs under the artifact's logs directory by default.

Mitigation: Keep generated logs out of shared or synced directories when they contain collected social-media datasets, and delete logs when they are no longer needed.

Risk: The skill is limited to public Xiaohongshu data and does not support private, hidden, login-only, publishing, liking, commenting, or following actions.

Mitigation: Confirm that the user supplied a public keyword, note URL, or creator profile URL, and refuse or redirect requests for private data or account actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-search-and-track)
- [Guaikei API service](https://www.guaikei.com)
- [Options and CLI usage](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; executed CLIs return structured JSON and write JSON logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful CLI results include status, error_code, request metadata, skill metadata, and results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
