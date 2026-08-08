## Description: <br>
速记板——一个零依赖、纯前端的「碎片化文字收集 + 图片管理 + 整理 + 导出 Word」单文件网页应用。当用户需要：收集/摘录散落各处的文字、自动编号整理要点、按主题用文件夹归档文档、粘贴或拖拽管理图片、把零散文字一键导出成标准 .docx 文件，或要求"做个文字收集板/速记工具/剪贴板整理器/资料归档页"时使用。也适用于"把一段 HTML 做成可安装的 skill"这类交付需求。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weijunz766-collab](https://clawhub.ai/user/weijunz766-collab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to provide a browser-based note board for collecting fragmented text, organizing notes and files, managing pasted or dragged images, and exporting structured notes as Word documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact is presented as local-only, but server security evidence reports user-triggered outbound update and feedback links. <br>
Mitigation: Review before installing in strictly offline environments, disclose the outbound links to users, and avoid clicking update or feedback controls when network isolation is required. <br>
Risk: Notes, images, and uploaded files persist in browser LocalStorage and IndexedDB, which may retain sensitive material on the device. <br>
Mitigation: Avoid storing highly sensitive content unless users understand browser-local persistence and know how to clear the app's LocalStorage and IndexedDB data. <br>


## Reference(s): <br>
- [Product Introduction](references/product-intro.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/weijunz766-collab/skills/suji-board) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Files] <br>
**Output Format:** [Markdown guidance referencing a single-file HTML application and Word document export] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces or directs use of a local browser HTML app that stores notes in LocalStorage and images or uploaded files in IndexedDB.] <br>

## Skill Version(s): <br>
1.7.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
