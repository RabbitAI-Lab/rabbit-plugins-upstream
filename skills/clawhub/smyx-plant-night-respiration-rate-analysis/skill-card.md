## Description:

Analyzes nighttime plant canopy thermal imagery, optionally with ambient CO2 data, to estimate a relative plant respiration intensity index and provide structured monitoring guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, growers, and precision-agriculture operators use this skill to submit plant-factory or greenhouse nighttime thermal images or videos, estimate relative respiration intensity, review health and environment-control guidance, and query prior cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it wraps cloud media analysis with silent identity creation, persistent tokens, and active plaintext development endpoints.

Mitigation: Install only after the publisher fixes the release configuration to use HTTPS production endpoints, documents identity and account creation, avoids storing bearer tokens in plain SQLite, and corrects the dependency name.

Risk: Uploaded images, videos, and report history may be cloud-submitted and account-linked.

Mitigation: Treat submitted plant imagery, videos, and report history as cloud data and review consent, retention, and account-linking expectations before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)
- [Plant Night Respiration API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured JSON-style analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiration intensity estimates, level assessment, abnormality prompts, recommendations, report links, or cloud report history tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
