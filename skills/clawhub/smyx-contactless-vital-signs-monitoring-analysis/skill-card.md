## Description:

Analyzes camera footage to estimate heart rate, respiration, blood oxygen, and heart-rate variability without wearable sensors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to analyze a video or video URL for contactless vital-sign estimates and to review prior reports. Results are for health reference and do not replace medical measurement or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only setting still permits video analysis.

Mitigation: Do not rely on this setting as an export-only control until its behavior is fixed and verified.

Risk: The skill processes facial footage through a service, while retention and deletion practices are not established in the supplied evidence.

Mitigation: Before supplying footage, confirm the service destination and its retention and deletion practices.

Risk: Automatic account setup retains credentials without clear user controls, and account identifiers and stored tokens need careful handling.

Mitigation: Require separate handling for API secrets and account identifiers, with clear controls for stored tokens and automatic account enrollment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured vital-sign analysis and report information, including JSON results and Markdown summaries or report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated vital signs, risk prompts, recommendations, and links to reports; informational health reference only.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
