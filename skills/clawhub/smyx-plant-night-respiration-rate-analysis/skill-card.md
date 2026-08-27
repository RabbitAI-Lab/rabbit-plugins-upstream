## Description:

Estimates relative plant night respiration intensity from plant-factory canopy thermal imagery and optional ambient CO2 data, then returns structured analysis, risk prompts, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze nighttime plant canopy thermal images or videos, optionally with CO2 context, to estimate relative respiration intensity for plant factories, artificial climate chambers, and closed greenhouses. It can also return historical analysis reports from the configured remote service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and report metadata may be sent to lifeemergence.com services.

Mitigation: Use only with plant imagery and metadata that are approved for that remote service, and review data-handling expectations before installation.

Risk: The skill can automatically associate an internal identity and create or reuse remote/local account records.

Mitigation: Confirm the identity flow is acceptable in the deployment environment and avoid using the skill where silent account association is not permitted.

Risk: Service tokens may be stored in a local SQLite database under the workspace data directory.

Mitigation: Restrict access to the workspace data directory, inspect stored credentials during review, and rotate or remove tokens when retiring the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Plant night respiration API documentation](artifact/references/api_doc.md)
- [Analysis API error-code reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text containing structured analysis results, risk prompts, recommendations, report links, or historical report lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local file paths or URLs for plant thermal imagery/video; supports basic, standard, and JSON detail modes plus optional file output.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
