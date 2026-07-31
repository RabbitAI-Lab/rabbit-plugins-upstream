## Description: <br>
通过可配置的锤子便签 API 查询、新增、分类、星标、置顶便签，生成公众号富文本，并将 Markdown 或本地 .md 文件导出为 PNG 长图。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaoolee](https://clawhub.ai/user/zhaoolee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and note-management users use this skill to manage an authenticated Smartisan Notes workspace through a configured API, including note lookup, creation, folder classification, starring, pinning, WeChat-ready HTML generation, and PNG long-image export. It is best used with a self-hosted local service; the public fallback is only a no-SLA option when local deployment is not available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private notes, local images, or credentials may be sent to the public fallback service when a local endpoint is unavailable or not configured. <br>
Mitigation: Prefer a self-hosted local service and explicitly set NOTES_API_BASE_URL and NOTES_EXPORT_API_BASE_URL to that local endpoint before using the scripts. <br>
Risk: The note-management script can reuse broad project-level SUPERADMIN credentials if account-scoped credentials are not supplied. <br>
Mitigation: Use NOTES_API_USERNAME and NOTES_API_PASSWORD for the intended account instead of SUPERADMIN and SUPERADMINPASSWORD whenever possible. <br>


## Reference(s): <br>
- [Workspace API and command reference](references/workspace-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/zhaoolee/skills/notes-export-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write HTML, Markdown, or PNG files through the bundled scripts when the user requests exports.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
