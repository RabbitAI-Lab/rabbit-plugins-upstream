## Description: <br>
AI-powered succulent special-state detection from HD images via plant cameras or smartphones that identifies black rot, etiolation/melting, and stretching, then returns anomaly type, severity, confidence, and report information for home care, greenhouses, and flower shops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and plant-care operators use this skill to analyze succulent images or videos for three special health states: black rot, etiolation/melting, and stretching. The skill is intended to produce structured findings, severity grading, confidence values, and links to cloud-hosted report details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Succulent images, videos, or supplied URLs may be sent to a remote service for analysis. <br>
Mitigation: Use only media and URLs that are appropriate for third-party processing; avoid private, internal, or sensitive inputs. <br>
Risk: The skill may create or reuse a local account identity and persist auth-like tokens in the workspace data directory. <br>
Mitigation: Review the local workspace data directory before and after use, and remove stored identity or token files when they are no longer needed. <br>
Risk: History queries may retrieve cloud report records automatically when the user asks for prior reports. <br>
Mitigation: Run history-list commands only when cloud report retrieval is intended, and review returned report links before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text containing structured JSON-like analysis results, severity and confidence fields, report-list output, and optional report export links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the same textual report to a user-supplied output file when requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
