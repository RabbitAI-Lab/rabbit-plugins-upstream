## Description:

Assesses ornamental-fish color from images or videos and reports vibrancy scores, trends, and aquarium care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, fish farms, and aquarium app developers use this skill to review fish color changes and receive husbandry suggestions from image or video assessments. It can also retrieve previous assessment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish images or videos and report requests are sent to a cloud service.

Mitigation: Use only media you are comfortable sending to the service; avoid sensitive media.

Risk: The skill silently creates or reuses an account identity and stores service tokens locally.

Mitigation: Review and manage the stored account context and local data before using the skill in a shared workspace.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [Assessment API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured assessment report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include vibrancy scores, color measurements, trends, care suggestions, and report links.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
