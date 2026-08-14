## Description:

Fetches structured Xiaohongshu/Rednote public-data results for keyword search, note details, creator posts, and note comments to support content research, competitive analysis, KOL screening, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, operators, marketers, analysts, and developers use this skill to collect structured public Xiaohongshu/Rednote data for topic research, competitor monitoring, creator screening, trend tracking, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The top-level description emphasizes comment fetching, while the docs and code expose broader keyword search, note-detail, and creator-post collection.

Mitigation: Install and invoke it only when the broader Xiaohongshu/Rednote public-data collection scope is intended, and choose the narrowest command that matches the user's task.

Risk: Keywords, note/profile URLs, and API tokens are sent to guaikei.com.

Mitigation: Use only approved public-data queries, confirm that third-party API use is acceptable for the workspace, and avoid sending sensitive or private inputs.

Risk: Returned results are saved locally under logs.

Mitigation: Review local log retention and cleanup practices before using the skill with operational or customer-related research data.

Risk: Bulk collection of public platform data may create policy, legal, or rate-limit concerns.

Mitigation: Review applicable platform and legal constraints, keep limits proportionate to the task, and avoid private, hidden, or unauthorized data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-ops)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [Structured JSON command output with optional locally saved JSON log files and concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include request metadata, status/error fields, runtime metadata, and public Xiaohongshu/Rednote content data returned by guaikei.com.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
