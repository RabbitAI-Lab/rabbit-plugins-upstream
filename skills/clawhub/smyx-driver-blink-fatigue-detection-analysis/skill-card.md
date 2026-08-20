## Description:

Using an in-cabin DMS camera, the skill analyzes driver facial video, detects eye open or closed state, calculates blink rate and eye-closure duration, and reports fatigue-warning indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and fleet safety teams can use this skill to analyze driver-facing DMS video or video URLs for blink rate, long eye closure, PERCLOS, fatigue level, warning type, recommended action, and report links. The output is an assistive safety warning and not a medical or sleep-disorder diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-facing video or video URLs may be sent to the configured backend service.

Mitigation: Use only with explicit driver consent, minimize shared video content, and verify retention, deletion, and data-handling terms before deployment.

Risk: Reports may be associated with an automatically managed identity and local token data.

Mitigation: Run in an isolated workspace or account context and review token storage, access controls, and cleanup procedures before use.

Risk: Historical cloud report queries may expose prior analysis records without clear user control.

Mitigation: Verify authorization, account isolation, and report access boundaries before enabling history-list workflows.

Risk: Fatigue warnings can be unreliable when video quality is poor, the eyes are obscured, or lighting conditions are adverse.

Mitigation: Require adequate driver-face video quality, confirm both eyes are visible, and treat outputs as assistive safety signals rather than medical or operational determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis)
- [Driver fatigue detection API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured text from API-backed analysis results, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue metrics, warning messages, recommended actions, report links, and historical report tables.]

## Skill Version(s):

1.0.7 (source: release evidence; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
