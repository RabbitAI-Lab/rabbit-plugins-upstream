## Description:

Analyzes snake mouth images or videos for visual signs associated with stomatitis risk, including mucosa color changes, pus points, ulcers, necrotic tissue, image quality, and relevant husbandry context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, reptile caretakers, breeding facilities, and reptile veterinary workflows can use this skill to generate structured visual risk reports from snake open-mouth media. The skill is intended to support observation and escalation decisions, not to provide a veterinary diagnosis or treatment prescription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snake images, videos, and history queries are sent to the configured LifeEmergence backend.

Mitigation: Use only media and report queries appropriate for remote processing, and confirm retention and handling expectations before using sensitive material.

Risk: The skill creates or reuses a local identity and stores backend tokens in a workspace SQLite database.

Mitigation: Run the skill only in a trusted workspace, restrict access to the workspace data directory, and remove local data when the identity or tokens should no longer persist.

Risk: Cloud history queries can return reports associated with the local identity.

Mitigation: Verify that the active workspace identity is appropriate before listing or sharing historical report links.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON structured analysis report with risk level, observed visual findings, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a caller-specified file path; history listings are formatted from cloud API results when requested.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
