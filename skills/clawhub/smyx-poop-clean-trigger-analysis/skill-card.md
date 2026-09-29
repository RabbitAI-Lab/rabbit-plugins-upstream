## Description:

Analyzes dog toilet or pet defecation-area video from a file or URL, detects a pet defecation event and feces presence, and returns a cleaning trigger signal after the pet leaves; it does not provide medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to submit fixed-camera pet toilet videos or URLs for cloud-backed defecation-event analysis, structured reporting, and robot-vacuum cleaning trigger generation. It is intended for indoor dog toilets, balcony defecation zones, and pet kennels where the user has already arranged any downstream smart-home integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet camera videos or URLs and user-linked identifiers are sent to lifeemergence cloud services.

Mitigation: Use the skill only with appropriate consent and non-sensitive footage, and review the cloud provider's data handling before deployment.

Risk: The skill can create or reuse an identity and persist local account or token records for history lookup.

Mitigation: Run it in an isolated workspace, restrict access to the workspace data directory, and remove or rotate local tokens when the integration is no longer needed.

Risk: The cleaning trigger is an event flag, not a direct robot-vacuum control integration.

Mitigation: Require a separately reviewed smart-home gateway or robot-vacuum OpenAPI integration before allowing automated cleaning actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output a cloud report list or report export link; cleaning trigger is an event signal, not direct robot-vacuum control.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
