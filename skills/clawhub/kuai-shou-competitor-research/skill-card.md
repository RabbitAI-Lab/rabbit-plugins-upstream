## Description:

Kuaishou public-data retrieval and competitor-research skill for searching videos, listing creator posts, and fetching video comments as structured results for topic research, competitor monitoring, KOL screening, comment analysis, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operators, marketers, and analysts use this skill to retrieve public Kuaishou video, creator-post, and comment data for competitor research, content ideation, KOL screening, monitoring, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile URLs, video URLs, request limits, and GUAIKEI_API_TOKEN are sent to the disclosed third-party API service at guaikei.com.

Mitigation: Use the skill only when that data sharing is acceptable, provide only authorized public-data targets, and manage GUAIKEI_API_TOKEN as a sensitive credential.

Risk: Retrieved comments and creator data are saved locally in generated log files.

Mitigation: Protect the logs directory, limit access to collected platform/user data, and avoid redistributing results outside authorized analysis workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/kuai-shou-competitor-research)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Structured JSON results with concise text or Markdown guidance around command routing, required inputs, errors, and follow-up analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs include status, error_code, message, timestamp, request, skill_metadata, and results; outputs are also saved under a local logs directory.]

## Skill Version(s):

1.0.0 (source: server release evidence, skill frontmatter, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
