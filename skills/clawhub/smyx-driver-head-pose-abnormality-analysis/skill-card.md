## Description:

This skill analyzes in-cabin driver media to estimate head pose and report sustained head-down or side-view distraction events with warning context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, fleet operators, and vehicle-safety teams can use this skill to analyze driver-facing DMS camera videos or URLs for head-down and side-view distraction indicators. It supports structured reports, historical report lookup, warning messages, and recommended follow-up actions such as voice alerts or fleet uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver videos or media URLs are sent to the configured lifeemergence.com cloud service for analysis.

Mitigation: Use the skill only with explicit driver or employee consent and confirm that cloud processing and report retention meet the applicable privacy requirements.

Risk: The skill silently creates or reuses a local identity and persists tokens used for history and report access.

Mitigation: Review or clear local identity and token state between users, and avoid broad history queries unless retrieving prior cloud-stored reports is intended.

Risk: Head-pose estimates can be unreliable when the driver's face or head outline is not clearly visible, such as with hats, masks, sunglasses, strong backlight, or vehicle vibration.

Mitigation: Treat results as driver-assistance warnings rather than authoritative safety decisions, and use clear DMS media that meets the documented frame-rate and visibility constraints.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, head-pose angles, detected distraction events, warning type, and recommended action.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
