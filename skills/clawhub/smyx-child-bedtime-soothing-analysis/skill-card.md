## Description:

Analyzes nighttime bedroom audio and video for signs of child distress and returns soothing guidance and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to review nighttime audio and video for signs such as crying, fear of the dark, or waking after a nightmare, and receive soothing guidance and a structured report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private child reports may be associated with the wrong account, and recordings may still be processed when a no-analysis option is selected.

Mitigation: Avoid bedroom recordings and shared-workspace use until account isolation and the no-analysis option are fixed. Confirm provider retention and deletion controls, and explicitly authorize uploads and account enrollment.

Risk: The skill may not reliably detect distress or provide safe automatic soothing for continuous monitoring.

Mitigation: Do not rely on this version for continuous child monitoring or automatic soothing.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis results with soothing guidance and report links, presented as text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected events, suggested soothing actions, a history listing, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
