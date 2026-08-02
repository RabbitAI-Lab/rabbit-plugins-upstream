## Description: <br>
Analyzes fixed-camera walking videos of older adults to estimate gait metrics such as step length, gait speed, trunk sway, and cadence, then reports gait stability and fall-risk level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, elder-care operators, rehabilitation staff, and developers use this skill to analyze straight-line walking videos, generate gait metrics, and review fall-risk screening reports or prior report history. The output is screening support only and does not replace professional medical or rehabilitation assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gait videos, report queries, identity values, and derived health reports may be sent to Life Emergence cloud services. <br>
Mitigation: Confirm consent, retention expectations, account ownership, and deletion controls before processing real elderly-person footage. <br>
Risk: The skill may silently create or reuse local identities and cached tokens for report access. <br>
Mitigation: Use an isolated workspace and review existing data/smyx-api-key.txt and data/smyx-common-claw.db state before installation or execution. <br>
Risk: Gait metrics and fall-risk levels are screening outputs and may be inaccurate without appropriate video quality, calibration, or clinical context. <br>
Mitigation: Treat results as decision support only and route concerning findings to qualified medical or rehabilitation professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown and text reports with structured JSON content, shell command examples, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include gait metrics, fall-risk level, risk factors, history-query results, and a cloud report export link.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and target metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
