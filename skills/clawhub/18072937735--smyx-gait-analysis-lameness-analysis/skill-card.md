## Description:

Analyzes pet side-view walking videos or URLs with AI pose-estimation-based gait metrics to surface stride, stance and swing phase, symmetry, lameness, and restricted-mobility findings without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary clinic staff, and rehabilitation teams use this skill to submit side-view walking media for gait analysis and retrieve structured historical reports for mobility monitoring. The output is intended as a visual gait-analysis aid, not a substitute for veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, report history, and identity-linked activity may be sent to Life Emergence cloud services.

Mitigation: Install and run the skill only where this cloud processing is acceptable, and review organizational consent and data-handling requirements before use.

Risk: The skill can silently create or reuse service identities and persist authentication tokens locally.

Mitigation: Use a workspace with appropriate file permissions, restrict access to shared data directories, and review token storage and credential routing before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-gait-analysis-lameness-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with structured analysis results, history tables, report links, and optional JSON detail]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Life Emergence cloud services to analyze media and retrieve identity-linked report history.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
