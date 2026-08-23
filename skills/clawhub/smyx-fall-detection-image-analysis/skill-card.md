## Description:

Detects whether anyone has fallen in a specified target area from an image or short video, with safety-monitoring use cases such as elder home care and nursing homes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, family members, and safety-monitoring teams use this skill to analyze uploaded images or short video clips for possible falls and to view structured reports and historical report links. Results are safety references and should be confirmed by a human before emergency decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home-care images or videos, report queries, and user identifiers may be sent to remote Lifeemergence services.

Mitigation: Use only when the service is trusted and authorized for the data being processed; review data handling requirements before deployment.

Risk: The security evidence flags default development HTTP endpoint configuration for sensitive media and report workflows.

Mitigation: Correct or verify endpoint configuration before installation or deployment, and prefer production HTTPS endpoints for sensitive workflows.

Risk: The security evidence notes local SQLite token and profile storage.

Mitigation: Treat local skill data directories as sensitive, restrict workspace access, and rotate or remove stored tokens when no longer needed.

Risk: Fall-detection results can be incorrect or incomplete and should not replace human confirmation.

Mitigation: Review suspected fall events manually and follow the organization’s emergency response procedure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Fall Detection API Documentation](artifact/references/api_doc.md)
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and historical report tables returned from remote API calls.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
