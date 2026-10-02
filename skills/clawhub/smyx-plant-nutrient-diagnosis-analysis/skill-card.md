## Description:

Analyzes plant leaf images or video for possible nutrient deficiencies and returns a structured diagnosis with guidance and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners and agricultural teams use plant images or video to investigate possible nutrient deficiencies, review suggested next steps, and retrieve prior diagnosis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or URLs are sent to an external cloud service during analysis.

Mitigation: Obtain consent before uploading and avoid sensitive media or private URLs.

Risk: Automatic identity handling and cloud report-history queries may expose records beyond the user's intended request.

Mitigation: Review identity and history access before use; request only reports the user is authorized to view.

Risk: A local database may retain service tokens.

Mitigation: Protect local storage and review token retention and access before installation.

## Reference(s):

- [Plant nutrient diagnosis API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Structured report or Markdown table with report links; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a proposed nutrient deficiency, confidence score, and fertilization direction; results are not a substitute for soil testing or agricultural advice.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
