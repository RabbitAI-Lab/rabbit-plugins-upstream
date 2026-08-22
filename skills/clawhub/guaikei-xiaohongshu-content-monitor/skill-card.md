## Description:

Search Xiaohongshu public notes, retrieve note details and comments, and monitor creator posts through command-line workflows that return structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, data analysts, and developers use this skill to collect Xiaohongshu public-content data for topic research, competitor monitoring, KOL screening, comment analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note links, profile links, and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use it only when that data sharing is acceptable and avoid submitting sensitive or unauthorized research targets.

Risk: Returned public-content results and query context can be saved locally under logs/.

Mitigation: Treat logs as retained research data and delete them manually when queries or results are sensitive.

Risk: Collected data is limited to public Xiaohongshu content but may still be subject to usage and redistribution constraints.

Mitigation: Confirm authorization and applicable platform or organizational rules before distributing outputs outside the personal or team workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xiaohongshu-content-monitor)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei support and token setup](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Files]

**Output Format:** [Structured JSON on stdout with optional JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a GUAIKEI_API_TOKEN and saves completed task results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata and package.json report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
