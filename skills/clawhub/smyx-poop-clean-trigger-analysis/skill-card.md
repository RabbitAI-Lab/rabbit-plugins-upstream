## Description:

Analyzes dog-toilet or pet defecation-zone video from a file or URL to detect a pet defecation event and output a cleaning trigger signal after the pet leaves the area.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home integrators use this skill to analyze pet defecation-area videos, generate structured event reports, and identify when a downstream robot-vacuum integration should clean the area. It is for vision-based event detection and does not provide medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-camera footage and report metadata are sent to the skill's cloud service for analysis and history retrieval.

Mitigation: Install only when cloud processing is acceptable, avoid sensitive footage, and confirm user consent and data-handling expectations before use.

Risk: The security evidence flags plaintext development endpoints and credential-handling concerns.

Mitigation: Use only production HTTPS endpoints, disable plaintext development configuration before deployment, and keep local workspace data and tokens protected.

Risk: The security evidence flags payment-related prompt behavior.

Mitigation: Review payment prompts and related install flows before enabling the skill for end users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and structured JSON-style analysis text, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a file; history queries return structured report records from the cloud service.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
