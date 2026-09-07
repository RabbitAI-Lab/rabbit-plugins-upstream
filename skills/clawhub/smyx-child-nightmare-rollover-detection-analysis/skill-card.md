## Description:

This skill analyzes fixed-camera child nighttime sleep audio and video to detect rollovers, crying, sleep talk, and body-jerk events, then returns sleep-quality reports and possible restless-sleep or nightmare alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers building child sleep-monitoring workflows use this skill to analyze night-vision sleep recordings, generate structured sleep-behavior reports, and surface non-diagnostic prompts to check on a child when restlessness or possible nightmare signals are detected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive children's bedroom audio and video.

Mitigation: Use only with guardian consent, isolate the workspace, and confirm retention and deletion controls before deployment.

Risk: The skill sends recordings and analysis requests to cloud APIs.

Mitigation: Confirm approved production endpoints, access controls, and data-handling terms before allowing real child recordings.

Risk: The security evidence reports unsafe defaults, including apparent plaintext HTTP development services and local identity state.

Mitigation: Force HTTPS production services, protect or remove stored tokens and identity state, and review configuration before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured sleep-behavior report text, Markdown tables for history listings, and JSON-compatible analysis fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sleep-quality scores, event counts, alert text, recommendations, and report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact SKILL.md frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
