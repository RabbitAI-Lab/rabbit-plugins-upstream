## Description:

Provides structured Xiaohongshu public-data retrieval for note search, note details, creator posts, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, marketers, analysts, and agents use this skill to gather Xiaohongshu public data for trend research, competitor monitoring, KOL screening, and comment insight workflows. It retrieves data only; users remain responsible for analysis decisions and compliant use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and Xiaohongshu links are sent to the guaikei.com API service.

Mitigation: Use the skill only when third-party API processing is acceptable for the workflow and data policy.

Risk: Returned public-data results may be written to local JSON log files.

Mitigation: Run in workspaces where log retention is acceptable and clean up logs when they are no longer needed.

Risk: GUAIKEI_API_TOKEN is required for all commands.

Mitigation: Store the token as a secret environment variable and avoid exposing it in shared terminals, logs, or committed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-search-notes-get-comments)
- [Guaikei service site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON data outputs from the invoked commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and GUAIKEI_API_TOKEN for command execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
