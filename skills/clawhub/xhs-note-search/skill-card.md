## Description:

xhs-note-search helps agents search public Xiaohongshu notes, retrieve note details and comments, and collect public posts from creator profiles for content research and marketing analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketing teams, analysts, and agents use this skill to gather public Xiaohongshu search results, note details, comments, and creator-post data for topic research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords, Xiaohongshu URLs, and the GUAIKEI_API_TOKEN are sent to the Guaikei service.

Mitigation: Confirm the user is comfortable with this data sharing before use and avoid submitting sensitive research topics or URLs.

Risk: Generated JSON logs can retain research topics, public comments, and collected public-note data on disk.

Mitigation: Protect or periodically delete generated logs when topics, comments, or analysis results are sensitive.

Risk: The skill is intended for public Xiaohongshu data and is not designed for private, hidden, or login-only content.

Mitigation: Use only publicly accessible Xiaohongshu keywords, note URLs, and creator profile URLs, and do not use results for unauthorized redistribution.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/engheng-art/skills/xhs-note-search)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Structured JSON on stdout with diagnostic text on stderr; successful runs may also write JSON result logs under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; requests are sent to the Guaikei service.]

## Skill Version(s):

1.0.0 (source: server release metadata, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
