## Description: <br>
Analyzes fixed-camera video from emergency shelters or temporary resettlement sites to detect visual acute-stress behavior signals and produce psychological-crisis alerts for authorized response teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External emergency-command teams and authorized psychological-rescue staff use this skill to analyze shelter video, locate visual behavior signals such as prolonged motionlessness, tremor, unresponsiveness, or hypervigilance, and review crisis alerts before dispatch. The skill is intended to support field triage and reporting, not to provide clinical diagnosis or medication guidance. <br>

### Deployment Geography for Use: <br>
China; reviewers should confirm jurisdictional fit before use elsewhere. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive shelter footage and mental-health-adjacent reports. <br>
Mitigation: Deploy only in an authorized emergency-response environment with a clear legal basis, operator approval, privacy controls, and role-based access to reports. <br>
Risk: Automatic identity creation, token persistence, and history access may create account-linkage and retention risk. <br>
Mitigation: Confirm where video and reports are sent, who can access historical reports, how long raw footage and derived records are retained, and whether automatic identity creation is acceptable before deployment. <br>
Risk: Behavioral alerts could be mistaken for clinical diagnoses or trigger unnecessary escalation. <br>
Mitigation: Require human review before high-risk dispatch, present results as visual behavior observations only, and keep clinical assessment and medication decisions with qualified responders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown text containing structured JSON-style analysis results, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include crisis level, zone or relative location, temporary tracking ID, responder dispatch suggestion, PFA quick reference, referral resources, and report export links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
