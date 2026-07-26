## Description: <br>
Analyzes fixed-camera walking videos of older adults to estimate gait metrics such as step length, gait speed, trunk sway, and cadence, then returns a low, medium, or high fall-risk level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, care organizations, rehabilitation teams, and health-platform developers use this skill to screen walking videos for gait instability indicators and generate structured fall-risk reports. The output is intended as auxiliary screening information, not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes elderly gait videos and report history through an external cloud service, which may involve sensitive health or caregiving footage. <br>
Mitigation: Use only with appropriate consent and review data retention, access control, and encryption practices before using real footage. <br>
Risk: The skill silently creates or reuses identity-linked local account tokens for analysis and history lookup. <br>
Mitigation: Review token storage, identity association, and who can access historical reports before installation or deployment. <br>
Risk: Gait metrics and fall-risk levels are auxiliary screening outputs and may be inaccurate or incomplete. <br>
Mitigation: Treat results as decision support and route concerning findings to qualified clinical or rehabilitation professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown tables or JSON structured analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes gait metrics, risk factors, fall-risk level, advisory text, and report links when available.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
