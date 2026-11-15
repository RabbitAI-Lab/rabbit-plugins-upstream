## Description:

Analyzes nighttime monitoring footage for bed exits, prolonged wandering, and extended periods of stillness, producing structured monitoring results for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams and families can use the skill to review nighttime footage for possible bed exits, prolonged wandering, or extended stillness and receive structured monitoring reports. Results are for care reference and should be confirmed by a person on site.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags privacy concerns involving video uploads and identity data, and the destination and consent requirements are not established by the available evidence.

Mitigation: Before use, verify where footage and identity data are sent, obtain any required consent, and confirm the receiving host's access and data handling controls.

Risk: The security review flags account and credential handling concerns.

Mitigation: Review how credentials are stored and protected before connecting an account or providing credentials.

Risk: The security review was partial because a referenced item was missing, so it does not establish that every part of the artifact was assessed.

Mitigation: Review the missing referenced item and complete the assessment before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured monitoring report in JSON or Markdown, with findings, recommendations, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs; documented formats are MP4, AVI, and MOV, with a 10 MB maximum file size. Historical report listings are returned as Markdown tables.]

## Skill Version(s):

1.0.23 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
