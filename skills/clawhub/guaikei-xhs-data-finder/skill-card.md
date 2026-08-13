## Description:

Searches public Xiaohongshu notes by keyword, retrieves note details, comments, and creator posts, and returns structured engagement data for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content marketers, creators, and analysts use this skill to gather public Xiaohongshu notes, comments, and creator post data for trend research, competitor monitoring, KOL screening, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API-token-authenticated requests send Xiaohongshu keywords, note or profile URLs, limits, and fetched public results to Guaikei.

Mitigation: Use the skill only for public data the user is allowed to process, keep targets scoped, and confirm data-sharing policies before running commands.

Risk: The skill can bulk fetch public comments and profile/post data.

Mitigation: Prefer the smallest practical limit and avoid collecting more user or comment data than the task requires.

Risk: Fetched results can be saved under the skill logs directory without a per-run opt-out.

Mitigation: Protect or delete saved logs when they contain comments, user/profile data, or sensitive research interests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-data-finder)
- [Guaikei service page](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON data, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; results may be written to the skill logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
