## Description: <br>
Analyzes pet defecation-area videos or URLs to detect a pet entering, defecating, and leaving, then returns a cleanup trigger signal and structured report for robot-vacuum integration; it does not provide medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and smart-home developers can use this skill to analyze indoor dog-toilet or pet-area footage and decide when a separate robot-vacuum integration should be triggered for cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Household pet-area media or URLs are sent to cloud services for analysis. <br>
Mitigation: Use only when users accept cloud processing; avoid sensitive private footage unless retention, deletion, and access terms are documented. <br>
Risk: The skill silently creates or reuses an internal identity and stores API tokens locally. <br>
Mitigation: Review token storage and account-linking behavior before deployment; restrict workspace access and rotate or delete stored credentials when no longer needed. <br>
Risk: Historical reports and exports may expose prior household media analysis results. <br>
Mitigation: Limit access to report-list and export functions to authorized users and verify report deletion and retention controls. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis) <br>
- [Pet Poop Trigger API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports and tables with optional JSON detail and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cleanup trigger event flags, event timestamps, pet type, recommendations, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
