## Description:

Non-contact detection of heart rate, respiration, blood oxygen, and heart rate variability from camera footage, with structured report output and history lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and care or wellness teams use this skill to analyze face video from a local file or URL for non-contact vital-sign estimates and to retrieve prior cloud reports. Results are for health reference and should not replace professional medical measurement or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends face/video health data to the Lifeemergence cloud service for analysis and report retrieval.

Mitigation: Use only with appropriate consent and confirm the publisher's retention, deletion, access-control, and data-handling terms before processing sensitive footage.

Risk: Reports are associated with an automatically managed identity and account tokens may be stored locally.

Mitigation: Review local token storage and identity behavior before installation, and avoid shared environments unless account isolation is understood.

Risk: Vital-sign analysis output is health-related and may be inaccurate or incomplete.

Mitigation: Treat results as health reference only and direct users to professional medical measurement or diagnosis for clinical decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](artifact/references/api_doc.md)
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with report links; Markdown table for history lookup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write results to a local output file when requested.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
