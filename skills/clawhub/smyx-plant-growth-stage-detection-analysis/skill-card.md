## Description:

Detects plant growth stages from plant images or videos and returns phenological observations, stage classification, confidence, general care guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, and developers use this skill to analyze plant media from smart pots, home grow boxes, greenhouses, and plant factories and identify the current growth stage. It is intended for reference-level stage assessment, confidence reporting, and general care direction rather than detailed agricultural operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or provided URLs are processed by an external cloud service.

Mitigation: Use only media approved for external processing and avoid sensitive camera footage unless that data handling is acceptable.

Risk: The skill can create or reuse an internal account identifier and query cloud report history.

Mitigation: Review account and report association behavior before use, and run it only in workspaces where cloud history access is intended.

Risk: Service tokens may be stored in the workspace data database.

Mitigation: Protect workspace storage and follow local token rotation, removal, and access-control practices.

## Reference(s):

- [Plant Growth Stage Detection API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown or JSON analysis report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stage name, confidence, observations, general care guidance, history tables, and report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
