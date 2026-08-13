## Description:

Assesses hydroponic root and leaf images or videos to identify visual stress signs, judge whether nutrient concentration is likely too high or too low, and return qualitative adjustment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External hydroponic growers, plant factory operators, researchers, and developers use this skill to evaluate plant root and leaf media for signs that nutrient solution concentration is too concentrated, too dilute, or visually acceptable. It returns qualitative findings and adjustment guidance rather than EC or ppm measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or provided media URLs may be sent to a configured external service for analysis.

Mitigation: Use only media appropriate for external processing and avoid sensitive local files or private URLs.

Risk: The skill can silently create or reuse an identity and query cloud report history.

Mitigation: Confirm that automatic identity handling and cloud history lookup fit the workspace policy before installing or running the skill.

Risk: Local token persistence may leave service credentials or session state in the workspace.

Mitigation: Run in an approved workspace and clear persisted tokens or state according to local security policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [Hydroponic Nutrient Assessment API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis text, with optional shell commands and saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud history results returned by the configured external service.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
