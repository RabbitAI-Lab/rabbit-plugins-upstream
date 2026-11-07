## Description:

Analyzes video from a designated pet toilet area to detect a defecation event and provide a cleaning trigger after the pet leaves.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and home-automation developers use it to review video from a designated pet toilet area and generate an event signal for a downstream robot-vacuum integration. The signal must be connected through the user's smart-home gateway; the skill does not directly control a vacuum.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option can still upload video, and credential handling is not clearly explained.

Mitigation: Avoid private footage and valuable credentials until this is corrected; confirm retention and deletion arrangements first.

Risk: The configured API destination may not be changed by --api-url.

Mitigation: Do not rely on --api-url to change the destination.

Risk: Server-side detection accuracy and physical robot-trigger safety are unverified.

Mitigation: Validate results before connecting physical cleanup automation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, JSON, Markdown, guidance]

**Output Format:** [Structured analysis results, Markdown history report listings, and a cleaning event signal; may include a report link.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vision-based event detection only; no medical diagnosis. Robot actuation requires a separate smart-home integration.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
