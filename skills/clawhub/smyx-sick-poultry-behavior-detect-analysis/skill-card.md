## Description: <br>
Detects morbid behavioral cues in poultry and pigs from continuous barn videos, including difficulty standing, ruffled feathers or piloerection, isolation, drowsiness, and appetite loss, and returns behavior type and risk level for early screening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, animal-health teams, and developers use this skill to screen poultry or swine barn images and videos for abnormal behavior, produce structured risk reports, and retrieve prior cloud analysis reports. The output is for early behavior screening and does not provide disease diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports under-disclosed identity, token, account, history, and local persistence behavior. <br>
Mitigation: Review the publisher's documentation for identity creation, token storage, account reuse, and history retrieval before installation or execution. <br>
Risk: The skill may upload barn media or submit media URLs to cloud-backed Lifeemergence endpoints. <br>
Mitigation: Confirm endpoint ownership, media retention, deletion controls, and authorization requirements before processing sensitive farm footage. <br>
Risk: The skill can query prior reports associated with a local or internal identity. <br>
Mitigation: Limit use to trusted workspaces and verify that report history access is scoped to the intended user or farm identity. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-sick-poultry-behavior-detect-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports and tables with JSON-backed analysis results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include behavior categories, abnormal subject locations, group morbidity ratio, risk level, analysis time, and cloud report URLs.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
