## Description:

Analyzes pet-safety camera images or videos to identify when a pet enters an active UV-C disinfection area, produce a structured risk report, and recommend shutting off the lamp when UV exposure risk is detected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze smart-home or facility camera media for pet entry into UV disinfection zones, UV lamp status, and resulting safety alerts. It can also query prior UV safety monitoring reports through the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-safety video is uploaded to remote services.

Mitigation: Require clear disclosure of upload, retention, and access practices before deployment.

Risk: The inspected artifacts include silent user identity creation and token storage.

Mitigation: Review identity handling, token storage, and report-history access controls before installation.

Risk: The inspected artifacts include insecure development HTTP endpoints.

Mitigation: Use only a production configuration that enforces HTTPS endpoints.

Risk: The skill describes UV-lamp shutoff recommendations but the inspected evidence does not establish it as a dependable real-time safety control.

Mitigation: Keep independent UV-lamp safety controls in place and treat skill output as advisory until validated in the deployment environment.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with safety status, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video input, remote video URL input, pet type selection, detail level selection, optional file output, and report-history listing.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
