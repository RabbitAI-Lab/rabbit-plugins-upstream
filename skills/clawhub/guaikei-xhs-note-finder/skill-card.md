## Description:

Searches public Xiaohongshu notes, note details, creator posts, and comments through the Guaikei API so agents can collect structured inputs for content, competitor, trend, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to collect public Xiaohongshu keyword results, note details, comments, and creator post lists for downstream summaries, comparisons, and reports. It is not intended for private, hidden, login-gated, or non-public data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords and public Xiaohongshu links are sent to the guaikei.com API with a GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when the user has approved this third-party API use and avoid submitting private, hidden, login-gated, or sensitive inputs.

Risk: Fetched result JSON is automatically saved locally and may contain sensitive business research.

Mitigation: Treat the logs directory as sensitive, restrict access where needed, and delete saved result files when they are no longer required.

Risk: API errors, empty results, rate limits, or invalid links can produce incomplete data.

Mitigation: Check returned status and error_code fields before analysis, retry only appropriate transient failures, and do not fabricate conclusions from empty or failed responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-note-finder)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI execution returns structured JSON and writes result JSON files under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched results are stored locally until removed.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
