## Description:

Analyzes indoor pet videos for vomiting or regurgitation behavior and produces event summaries, observations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and veterinary care teams use this skill to review indoor camera footage for possible vomiting or regurgitation events, inspect event details, and retrieve prior reports. Results support observation rather than veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor pet footage or video URLs are sent to a cloud service and may expose household activity.

Mitigation: Use only footage you are authorized to share; confirm the service endpoint, retention period, and deletion process with the publisher before submitting real household video.

Risk: Analysis history is linked to an automatically managed identity, and user records and tokens are stored locally.

Mitigation: Review authentication and local storage practices with the publisher, restrict access to stored records, and use a trusted device.

Risk: Similar-looking behaviors can be misclassified, and results are not a medical diagnosis.

Mitigation: Confirm suspected events against the footage and consult a veterinarian for persistent symptoms or urgent concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [Pet analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis text or JSON with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event observations, risk prompts, history listings, and an optional saved result file.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
