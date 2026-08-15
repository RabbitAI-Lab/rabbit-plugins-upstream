## Description:

Analyzes rehabilitation-session images or videos from fixed cameras to identify patient frustration or giving-up tendency signals, produce structured findings, and suggest motivation or escalation actions without making medical diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External care teams, rehabilitation centers, and home-rehab operators can use this skill to analyze authorized rehabilitation-session media for frustration, training interruption, low engagement, or lack-of-progress signals and to generate structured motivation recommendations, escalation guidance, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive patient video or audio, links activity to patient identity, retrieves history, and may trigger therapist or family notifications.

Mitigation: Use only with explicit patient or authorized guardian consent, confirm institutional disclosure and retention rules, and verify access controls before processing real patient media.

Risk: The server security summary flags cloud processing, automatic identity creation, history access, and local token storage as insufficiently disclosed or controlled.

Mitigation: Review the publisher's backend endpoints, retention policy, token storage protections, and authorization model before installation or deployment.

Risk: Frustration signals and progress comparisons could be mistaken for clinical conclusions or could motivate inappropriate changes to rehabilitation intensity.

Mitigation: Keep outputs limited to behavioral observations and motivation guidance, require clinician confirmation for therapy changes, and do not use the skill to diagnose medical or mental-health conditions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured analysis report with findings, recommendations, history rows, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud APIs for analysis and history retrieval; outputs should not expose internal identity values.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
