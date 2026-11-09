## Description:

Analyzes submitted video of window or balcony areas for child climbing or leaning behavior and returns a structured safety report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and safety operators can submit a local video or video URL of a window or balcony area for analysis, then review the returned risk report or query historical reports. The skill is intended to support adult supervision, not replace it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted recordings may contain sensitive images of children and are processed by an external service.

Mitigation: Obtain guardian consent and verify video processing, retention, and access practices before submitting recordings.

Risk: Account identity and report access depend on automatic identity handling whose enrollment and storage practices are not established by the available evidence.

Mitigation: Verify account enrollment, identity resolution, and token storage before using analysis or historical report features.

Risk: The security review reports that some advertised safeguards or alert functions may not work as claimed.

Mitigation: Test analysis and end-to-end alerts in the intended setup before relying on them, and maintain direct adult supervision.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured analysis results or text summaries; historical reports can be presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include detected behavior, confidence, event time, alert level, alert text, snapshot, or report link when returned by the service.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
