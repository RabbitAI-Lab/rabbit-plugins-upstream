## Description:

Monitors infant behavior via visual AI, automatically identifying high-risk actions like rolling over, mouth/nose obstruction, climbing, or falling from bed, and triggers instant safety warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze infant activity videos or media URLs for safety risks, generate structured monitoring reports, and retrieve cloud-backed report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends infant videos, images, or provided media URLs to the Life Emergence cloud service for analysis.

Mitigation: Use only media the user is authorized to process, minimize identifying details in filenames or URLs, and confirm privacy requirements before deployment.

Risk: Analysis reports and history retrieval are tied to automatically managed local identity and token state.

Mitigation: Review whether persistent local identity storage and account-linked history are allowed in the deployment environment, and manage or remove local identity state according to policy.

Risk: Infant safety outputs are advisory and can be affected by media quality or cloud-service behavior.

Mitigation: Treat the report as caregiver decision support, not as a replacement for real-time supervision or professional care.

## Reference(s):

- [Infant safety monitoring API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown-style text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-generated safety scores, risk warnings, care suggestions, history listings, and report export URLs.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
