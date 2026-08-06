## Description: <br>
AI-powered UV disinfection safety monitor for pets that analyzes camera video or URLs to detect pet entry into active UV-C areas, issue high-risk alerts, recommend shutting off UV lamps, and log reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators of smart homes, pet households, or pet boarding facilities use this skill to analyze UV disinfection-area media for pet entry and UV-lamp risk signals. It returns structured safety findings, recommendations, report links, and optional history lookups from the publisher's remote service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet or home camera media and public URLs are sent to the publisher's remote analysis service. <br>
Mitigation: Use only approved media, avoid sensitive scenes, and confirm that the publisher's data handling is acceptable before installation. <br>
Risk: The skill may create or reuse a local/cloud-linked identity and persist tokens or user records locally. <br>
Mitigation: Run in an isolated workspace, review local token and database storage, and remove credentials when the skill is no longer needed. <br>
Risk: The security verdict is suspicious and the live monitoring or device-control path is not verified. <br>
Mitigation: Treat the output as advisory and require independently verified UV shutoff and monitoring controls for safety-critical use. <br>
Risk: Cloud history queries can expose prior analysis reports associated with the resolved identity. <br>
Mitigation: Limit use to trusted accounts and workspaces, and review access permissions before querying report history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Analysis API error-code documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with structured JSON-like analysis content, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Historical report queries return remote-service records; analysis supports local video files or public media URLs and may include export links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
