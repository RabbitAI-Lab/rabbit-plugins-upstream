## Description: <br>
Kingdoc helps agents create, edit, manage, convert, recover, and resolve conflicts in Kingsoft/WPS online documents using local document tools and Kingsoft/WPS APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external collaborators, and developers use Kingdoc to operate Kingsoft/WPS documents through an agent, including document creation, spreadsheet and multidimensional table editing, file management, OCR, format conversion, sharing, version recovery, and collaborative conflict resolution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Kingsoft/WPS documents and selected local files. <br>
Mitigation: Use a dedicated working folder, grant only needed document permissions, and review selected files before upload or download. <br>
Risk: Document deletion, sharing, upload, overwrite, and webhook actions can affect user data or expose content. <br>
Mitigation: Require explicit user confirmation for delete, share, upload, overwrite, permission, batch, and webhook operations before execution. <br>
Risk: Credential and token handling can expose account access if configuration or logs are mishandled. <br>
Mitigation: Protect config.json, avoid running auth token tests in logged terminals, and keep credentials out of shared logs or prompts. <br>
Risk: The security verdict is suspicious due to powerful capabilities and weaker runtime guardrails than the safety text claims. <br>
Mitigation: Review and scan the skill before deployment, then enforce operational approvals and file-scope restrictions in the host agent. <br>


## Reference(s): <br>
- [Kingdoc ClawHub page](https://clawhub.ai/fyniujin/skills/kingdoc) <br>
- [Kingsoft Developer Platform](https://developer.kdocs.cn) <br>
- [WPS Open Platform](https://open.wps.cn) <br>
- [Authentication reference](references/auth.md) <br>
- [Security design](references/security.md) <br>
- [Workflow reference](references/workflows.md) <br>
- [Spreadsheet API reference](references/et_references.md) <br>
- [Office conversion and extraction reference](references/office_references.md) <br>
- [Rate limit and hardware adaptation reference](references/rate_limit.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with configuration snippets, shell commands, API-oriented guidance, and generated document content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local document artifacts and cloud document operations when configured with user credentials and explicit action approval.] <br>

## Skill Version(s): <br>
3.3.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
