## Description:

Collects structured public Xiaohongshu (Rednote) data for topic discovery, competitor monitoring, KOL screening, and comment insight workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, content teams, and analysts use this skill to retrieve structured public Xiaohongshu data for content planning, competitor monitoring, KOL evaluation, trend research, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu URLs, API tokens, and fetched results are sent to the third-party guaikei.com API.

Mitigation: Use the skill only when third-party API processing is acceptable, confirm authorization for the target data, and avoid private, restricted, or unauthorized content.

Risk: Fetched social-media and business research data is saved locally in JSON log files.

Mitigation: Treat logs as sensitive, store them with appropriate access controls, and delete them when no longer needed.

Risk: The GUAIKEI_API_TOKEN is required for all data retrieval commands.

Mitigation: Provide the token through environment variables, avoid sharing it in prompts or logs, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-scout)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Structured JSON on stdout with optional human-readable summaries and JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands call guaikei.com and can request up to 10000 records per run.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
