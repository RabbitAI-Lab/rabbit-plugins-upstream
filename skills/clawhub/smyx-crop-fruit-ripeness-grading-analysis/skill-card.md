## Description:

Identifies fruit ripeness stages (green, turning, ripe, and over-ripe) from fruit image or video inputs using color, size, and gloss features, then returns a standardized ripeness grade.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, agricultural operators, and agents use this skill to grade tomato, pepper, and similar commercial crop fruit ripeness from images, videos, local files, or URLs. It can also retrieve account-linked historical ripeness reports from the configured backend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill sends crop images, videos, URLs, and account-linked report queries to a configured backend.

Mitigation: Review the backend destination and data handling expectations before installation, and use the skill only when sending those inputs to the configured service is acceptable.

Risk: The security review reports silent account identity management and local persistence of identity or token material.

Mitigation: Treat the local data directory as sensitive, document how account creation and token storage work, and avoid exposing identity values in user-facing output.

Risk: The security review reports development or private HTTP endpoints in configuration.

Mitigation: Switch to intended production HTTPS endpoints or validate the configured endpoints before deployment.

Risk: Historical report retrieval is account-linked and may expose prior analysis records for the resolved identity.

Mitigation: Add explicit confirmation before retrieving history and show only reports associated with the current resolved identity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text reports with optional JSON-oriented detail and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured ripeness grades, harvest-window guidance, analysis progress, saved result files, and historical report tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; SKILL.md frontmatter remains 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
