## Description: <br>
供应商信息结构化整理与 Markdown 档案生成；根据用户提供的资料（Word、PDF、Excel）提取供应商关键信息，按模板汇总生成质量管理档案，支持 Python 生成 SVG 组织结构图。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, sourcing, and supplier-management teams use this skill to turn user-provided supplier documents into structured supplier profiles and quality-management records. It is intended for organizing supplied information, not for automatically researching suppliers online or scoring supplier performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated supplier profiles may include personal contact details, business identifiers, or confidential supplier information from user-provided files. <br>
Mitigation: Review Markdown or Word outputs before sharing and redact fields that are not needed outside the intended quality-management workflow. <br>
Risk: Scanned PDFs, incomplete source files, or nonstandard Excel columns may lead to missing or misread supplier information. <br>
Mitigation: Confirm extracted fields against the original documents and keep missing values clearly marked for follow-up. <br>
Risk: Optional conversion or organization-chart steps may fail when local Python dependencies are unavailable. <br>
Mitigation: Use the Markdown output or text-based organization description as the fallback when conversion or SVG generation cannot run. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-supplier-profile-arrangement) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-supplier-profile-arrangement) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown supplier profile, optional Word document guidance, optional SVG organization chart, and concise setup or fallback commands when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May mark missing supplier fields for follow-up and should keep sensitive supplier details scoped to the intended workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
