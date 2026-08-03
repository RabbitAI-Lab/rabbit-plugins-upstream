## Description: <br>
Analyzes frontal facial images or short videos of elderly people to estimate facial asymmetry, mouth-corner deviation, and related landmark-based risk indicators for auxiliary screening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, elder-care operators, and health-monitoring developers use this skill to submit frontal face media, receive a structured asymmetry report, and review cloud-stored historical reports. The output is intended as an auxiliary screening signal, not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elderly face images, videos, and health-screening results are uploaded to cloud services. <br>
Mitigation: Use only with informed consent, send the minimum necessary media, and confirm the publisher's retention, deletion, and access-control practices before deployment. <br>
Risk: The skill automatically creates or reuses identity records and tokens with limited user-facing control. <br>
Mitigation: Review authentication, token storage, and account-association behavior with the publisher before installation in managed environments. <br>
Risk: Facial asymmetry output could be mistaken for a clinical diagnosis. <br>
Mitigation: Present results as auxiliary screening only and require professional medical review for suspected stroke, facial paralysis, or other urgent symptoms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis, risk labels, report links, and example command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export links and historical report listings returned from the configured API service.] <br>

## Skill Version(s): <br>
1.0.5 (source: server-resolved release metadata; artifact SKILL.md frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
