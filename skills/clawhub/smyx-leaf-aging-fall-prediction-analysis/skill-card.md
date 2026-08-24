## Description:

Uses fixed-angle indoor plant images or video to analyze leaf color, gloss, and petiole angle changes, then predicts likely leaf-fall risk windows and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and plant-care operators use this skill to evaluate continuous indoor plant media, distinguish normal leaf aging from possible stress, and receive structured predictions for leaves likely to fall within the next 3-7 days.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media, report history, and internal identifiers may be sent to the publisher's remote service.

Mitigation: Install only where that data transfer is acceptable, and confirm the service endpoints and data-handling expectations before use.

Risk: The skill may silently create or reuse an identity and store authentication tokens locally.

Mitigation: Review local identity and token storage before deployment, restrict workspace access, and define a process to delete or reset stored identity data.

Risk: Security evidence flags broad network behavior and possible dev/private HTTP endpoint configuration.

Mitigation: Confirm production endpoints, block unintended private or test hosts, and monitor outbound network access during execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the generated report text to a caller-specified output file.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter declares 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
