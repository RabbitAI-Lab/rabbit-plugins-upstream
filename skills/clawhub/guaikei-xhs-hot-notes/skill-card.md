## Description:

Collects public Xiaohongshu keyword search results, note details, note comments, and creator posts as structured data for downstream analysis, comparison, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and content teams use this skill to retrieve public Xiaohongshu content data before summarizing trends, comparing notes, analyzing comments, monitoring creators, or preparing reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note URLs, profile URLs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install and run it only when that data sharing is acceptable, and scope the token to the intended use.

Risk: Generated logs may contain sensitive research records or collected public-content data.

Mitigation: Keep logs out of shared repositories and backups when needed, and delete them when they are no longer required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-hot-notes)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei service website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Structured JSON from Node.js CLI commands with human-facing status and error messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save retrieved results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
