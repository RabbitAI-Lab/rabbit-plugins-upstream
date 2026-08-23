## Description:

Retrieves public Xiaohongshu notes, note details, comments, and creator post lists through guaikei.com so agents can support content research, competitor analysis, KOL screening, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, analysts, and developers use this skill to collect and summarize public Xiaohongshu search results, note details, comments, and creator post lists for market research and content planning. It is not for login, posting, interaction, private data access, or unsupported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, note/profile URLs, and xsec_token query strings are sent to guaikei.com with the user's GUAIKEI_API_TOKEN.

Mitigation: Use the skill only with public Xiaohongshu inputs that the user is comfortable sending to the third-party API service, and manage GUAIKEI_API_TOKEN as a credential.

Risk: Successful runs save JSON result files in the skill's logs directory.

Mitigation: Avoid sensitive research terms on shared systems and clean up generated logs when retention is not needed.

Risk: API errors, invalid tokens, rate limits, or deleted/private content can produce empty or error responses.

Mitigation: Treat status-coded JSON responses as authoritative and do not fabricate data when the CLI reports empty or error results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-notes-and-comments)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful CLI runs emit a status-coded JSON object and save a JSON result file under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
