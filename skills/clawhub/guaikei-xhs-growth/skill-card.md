## Description:

Retrieves public Xiaohongshu notes, note details, comments, and creator post lists as structured data for trend research, competitive analysis, KOL screening, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content teams, marketers, analysts, and agent operators use this skill to retrieve public Xiaohongshu data for trend discovery, competitive monitoring, KOL screening, comment analysis, and report preparation. It is not intended for logging in, publishing, interacting with accounts, or accessing private content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu links, and GUAIKEI_API_TOKEN are sent to the guaikei.com API.

Mitigation: Install and run the skill only when that data sharing is acceptable for the user's environment and authorization scope.

Risk: Command results are saved locally and may contain sensitive research topics, public comments, account URLs, or competitive-analysis data.

Mitigation: Review and delete generated logs when the retained results should not remain on disk.

Risk: The skill is scoped to public Xiaohongshu data and may fail or return errors for private, hidden, deleted, or unsupported links.

Mitigation: Use only public note or creator-profile links, validate link type before execution, and do not treat empty or error responses as successful data.

## Reference(s):

- [Guaikei API website](https://www.guaikei.com)
- [Options and calling guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON command output with optional Markdown summaries and local log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results are saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
