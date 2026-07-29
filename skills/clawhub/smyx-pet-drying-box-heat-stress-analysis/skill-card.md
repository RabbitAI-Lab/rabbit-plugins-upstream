## Description: <br>
Analyzes pet drying-box video from a local file or URL to identify early heat-stress signals such as panting intensity, tongue color, and movement frequency, then returns a structured risk report and intervention suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet grooming staff, pet hospitals, and developers use this skill to submit drying-box footage for cloud analysis and receive heat-stress risk levels, observations, report links, and safety-oriented intervention suggestions. It is for drying safety monitoring and does not provide disease diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet-environment footage or video URLs are sent to the LifeEmergence cloud service for analysis. <br>
Mitigation: Use only footage appropriate for that service, avoid uploading unrelated sensitive clinic or household content, and review privacy and retention terms before use. <br>
Risk: The skill can create or reuse a local identity, log in remotely, and cache access tokens in a workspace database. <br>
Mitigation: Run it in an isolated workspace without unrelated sensitive data, restrict workspace access, and clear local identity or token data when the skill is no longer needed. <br>
Risk: History queries retrieve cloud report records associated with the resolved identity. <br>
Mitigation: Use separate workspaces or identities for separate users or environments and review report history before sharing outputs. <br>
Risk: Heat-stress results may be mistaken for veterinary diagnosis or treatment direction. <br>
Mitigation: Present results as drying safety observations and intervention suggestions only, and escalate urgent or unclear animal-health concerns to a qualified professional. <br>


## Reference(s): <br>
- [Pet drying-box heat stress API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown text containing structured JSON-style report content and report links; optional file output writes the same textual report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return a history list from the cloud service, and supports basic, standard, or json detail modes.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
