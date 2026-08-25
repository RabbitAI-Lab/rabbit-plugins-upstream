## Description:

AI-powered aquatic plant health monitoring from aquarium camera images, detecting visual leaf color and morphology issues and returning health assessments with care direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquascaping operators, aquarium shops, and developers use this skill to analyze aquarium plant images or videos for visible health symptoms, likely causes, care guidance, and account-linked history reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends aquarium media or media URLs to a configured remote analysis service.

Mitigation: Review the configured endpoints and only provide media that is appropriate for the remote service before running analysis.

Risk: The skill silently creates or reuses a local account identifier and stores service tokens or profile data in the workspace data directory.

Mitigation: Review local data retention expectations and clear workspace data when account-linked state should not persist.

Risk: The skill can query account-linked cloud history with limited user control.

Mitigation: Confirm that cloud history access is acceptable for the deployment context before enabling history report queries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with report links and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query account-linked cloud history and may send aquarium media or media URLs to the configured analysis service.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
