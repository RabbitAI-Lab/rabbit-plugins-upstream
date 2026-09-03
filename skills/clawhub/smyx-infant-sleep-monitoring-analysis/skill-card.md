## Description:

Identifies infant sleep states such as deep sleep, light sleep, waking, and restlessness, then generates structured sleep reports and routine analysis for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and agents assisting caregivers use this skill to analyze infant sleep-monitoring videos or URLs, classify sleep states, summarize sleep timing and wake events, and retrieve prior cloud-hosted reports. Its outputs are for parenting reference and should not replace professional medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends baby-monitor videos or URLs and report-history requests to lifeemergence.com services.

Mitigation: Use only media and URLs intended for this service, and verify the publisher's privacy, retention, and data-handling practices before installation.

Risk: The skill creates or reuses a local identity and stores profile or token data in local files and SQLite-backed records.

Mitigation: Run it in an isolated workspace, protect the workspace data directory, and remove local identity or token stores when access is no longer needed.

Risk: Sleep-state analysis may be incomplete, incorrect, or unsuitable for clinical decisions.

Mitigation: Treat results as parenting reference only and consult a pediatric professional for abnormal sleep patterns or health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant sleep monitoring API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs for analysis, optional output file writing, and cloud report-list retrieval.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
