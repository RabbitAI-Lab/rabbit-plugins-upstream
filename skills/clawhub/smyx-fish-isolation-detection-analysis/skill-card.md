## Description:

Analyzes fixed aquarium camera video to track fish positions, compare each fish with the school centroid, and report prolonged isolation behavior with contextual cautions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, public aquarium teams, aquaculture operators, and developers use this skill to analyze uploaded or URL-based fish tank media for schooling, isolation, and alert-level reporting. It supports behavior monitoring and historical report lookup, while keeping diagnosis and treatment decisions with qualified aquatic professionals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media, video URLs, and history queries may be sent to the configured cloud service.

Mitigation: Use the skill only with media you are authorized to process, review the configured service endpoints before running it, and avoid sensitive or shared aquarium footage unless cloud processing is acceptable.

Risk: The skill can silently initialize an identity and persist identity or token data in the local workspace.

Mitigation: Review local workspace storage before and after use, avoid shared workspaces when token persistence is unacceptable, and clear stored identity data according to your environment's policy.

Risk: Fish isolation output may be mistaken for a veterinary diagnosis or treatment plan.

Mitigation: Treat results as behavior-monitoring guidance only; confirm health concerns, isolation decisions, medication, and treatment with a qualified aquatic professional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-isolation-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis reports with alerts, recommended actions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a file when requested; history lookup is formatted as a Markdown table.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
