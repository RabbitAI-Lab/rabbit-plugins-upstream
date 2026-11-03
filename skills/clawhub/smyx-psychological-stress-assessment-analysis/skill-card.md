## Description:

Analyzes facial blood-flow and emotional cues in images or videos to produce structured reports on stress levels and anxiety and depression tendencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People using mental-health monitoring workflows can submit an image or video for a structured stress assessment, or retrieve prior assessment reports. The reports are for reference and do not replace professional psychological or clinical evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive facial media may be uploaded even when analysis is meant to be disabled, and reports may be mixed across users.

Mitigation: Avoid sensitive media and shared agents until account isolation and the no-analysis control are fixed; confirm upload processing, report deletion, and token protection.

Risk: Assessment results may be mistaken for clinical diagnoses.

Mitigation: Treat reports as informational only; seek professional psychological or clinical evaluation for concerns.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured assessment text or JSON; Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include stress scores, anxiety and depression tendency labels, suggestions, and report links.]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
