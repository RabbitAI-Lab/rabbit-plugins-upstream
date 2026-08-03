## Description: <br>
Analyzes user-provided pet toilet or defecation-zone video files or URLs to detect defecation events, emit a cleanup trigger signal for downstream robot-vacuum integration, and return structured reports without providing medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and home-automation builders use this skill to analyze pet toilet or fixed defecation-area footage, identify the pet entering, defecating, and leaving, and produce a cleanup trigger signal. Actual robot-vacuum dispatch requires a separate user-side smart-home gateway or vendor OpenAPI integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provided videos or URLs are sent to LifeEmergence cloud services for analysis and may include sensitive home footage. <br>
Mitigation: Use only footage you are comfortable uploading to that service, and confirm the publisher's retention and deletion terms before using sensitive recordings. <br>
Risk: The skill may create or reuse a persistent local identity and store account tokens or profile data in a workspace SQLite database. <br>
Mitigation: Install in a controlled workspace, review local storage and token handling before deployment, and clear local identity or token data when the skill is no longer needed. <br>
Risk: Cloud report-history queries can expose reports linked to the persistent identity. <br>
Mitigation: Limit use to identities and environments where cloud report linkage is acceptable, and review who can access generated report links. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API reference](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports, JSON or text command output, and cloud report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a local file when requested; cloud report history is queried through the LifeEmergence service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
