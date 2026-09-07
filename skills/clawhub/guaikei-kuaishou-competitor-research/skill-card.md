## Description:

Searches public Kuaishou videos, creator posts, and video comments through the Guaikei API and returns structured JSON for competitor research, KOL screening, content planning, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operations teams, marketers, MCN analysts, and developers use this skill to collect public Kuaishou search results, creator post lists, and video comments. The outputs support competitor monitoring, topic discovery, KOL screening, comment insight, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Kuaishou URLs or IDs, and the configured API token are sent to guaikei.com.

Mitigation: Install and run the skill only when that third-party API data flow is acceptable for the workspace and task.

Risk: Successful fetches are saved locally as JSON logs that may contain public comments or competitor research data.

Mitigation: Use a controlled workspace for sensitive analysis and delete generated logs when retention is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-competitor-research)
- [Guaikei API Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Structured JSON from command-line API calls, with optional text or Markdown summaries prepared by the calling agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful fetches may be written to local JSON log files; requests require GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
