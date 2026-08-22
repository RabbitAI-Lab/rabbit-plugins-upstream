## Description:

Searches Xiaohongshu public content, retrieves note details, comments, and creator posts, and returns engagement data for content research and social media analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketing teams, analysts, and agent operators use this skill to research public Xiaohongshu notes, compare engagement signals, inspect comments, and monitor creator or competitor posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords and supplied Xiaohongshu URLs are sent to the Guaikei API.

Mitigation: Use the skill only for authorized public Xiaohongshu research and confirm that third-party API data handling is acceptable before execution.

Risk: Local logs can retain full fetched results and xsec_token-bearing URLs.

Mitigation: Run in a controlled workspace, treat logs as sensitive, and delete or redact logs after use.

Risk: Installing on shared or managed machines may expose retained results or the required API token.

Mitigation: Review the artifact before installation, store GUAIKEI_API_TOKEN in a managed environment variable, and rotate the token if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-public-content-intel)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON objects with status, request metadata, skill metadata, and results; guidance may include Markdown with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; command executions write result logs under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
