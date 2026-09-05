## Description:

Analyzes fixed night-vision camera video from elder-care bedrooms or hallways to detect bed-exit events, total time out of bed, wandering patterns, and threshold-based alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, nursing-home operators, home-care teams, and developers use this skill to analyze night monitoring footage for bed-exit duration, wandering behavior, alert levels, report links, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Elder bedroom or hallway monitoring footage and video URLs may be sent to a configured cloud service.

Mitigation: Confirm consent from the monitored person or legal representative, verify the service destination and retention policy, and avoid sending footage that is not needed for the requested analysis.

Risk: The skill can silently create or reuse generated user identifiers and stores service tokens for report access.

Mitigation: Review account isolation, authorization, audit logging, and token storage controls before installation, especially in regulated care environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-night-bed-exit-wandering-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text with structured analysis results, alert messages, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output historical report lists from the configured cloud API; local file analysis supports mp4, avi, and mov inputs up to 10 MB.]

## Skill Version(s):

1.0.11 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
