## Description: <br>
This skill uses computer vision to detect employee phone use in workplace video or images, count duration and frequency, and return structured monitoring reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Workplace administrators and authorized operations teams use this skill to analyze office monitoring images or video for phone-use events and retrieve structured reports for internal management review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sensitive workplace monitoring images, videos, and analysis data to cloud APIs. <br>
Mitigation: Use only where the operator is authorized to process workplace monitoring footage, with employee notice or consent, retention rules, and backend access controls confirmed before deployment. <br>
Risk: URL inputs may cause the backend service to fetch supplied media URLs. <br>
Mitigation: Restrict accepted URL sources and confirm backend fetch controls before allowing URL-based analysis. <br>
Risk: The skill silently creates or reuses an identity value and stores local identity/token data. <br>
Mitigation: Protect and periodically clear the workspace data directory, the SQLite token store, and data/smyx-api-key.txt; limit filesystem permissions to authorized users. <br>


## Reference(s): <br>
- [职场玩手机行为监测分析 API 文档](references/api_doc.md) <br>
- [API接口文档](skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files] <br>
**Output Format:** [Markdown or JSON analysis reports, with an optional saved output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and cloud-returned history records; output detail can be basic, standard, or json.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter states 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
