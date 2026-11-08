## Description:

Analyzes submitted infant sleep videos for posture and possible face covering, then returns a structured risk report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers can submit an infant sleep video for an on-demand review of sleep position and possible mouth, nose, or head covering. Use the result as supplemental information alongside adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private infant footage or reports may be uploaded or associated with another user's data.

Mitigation: Submit only footage intended for remote analysis, and use the skill only after sender isolation and export-only fixes are confirmed; avoid shared-agent use with private reports.

Risk: The service's processing, retention, deletion, account handling, credential protection, and costs are not verified.

Mitigation: Before use, confirm who processes the videos, how accounts are created, retention and deletion options, credential protection, and costs.

Risk: The bundled code does not establish continuous monitoring or dependable real-time alarms, and detection performance is unverified.

Mitigation: Treat results as on-demand supplemental analysis; maintain adult supervision and do not rely on the skill for alarms or SIDS prevention.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in JSON or text, with Markdown report lists when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [On-demand results may include risk factors, suggestions, and a report link.]

## Skill Version(s):

1.0.18 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
