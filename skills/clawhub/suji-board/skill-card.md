## Description: <br>
Suji Board is a zero-dependency, single-file browser app for collecting fragmented text and images, organizing notes and files, and exporting structured Word documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weijunz766-collab](https://clawhub.ai/user/weijunz766-collab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to collect pasted notes, images, and uploaded documents in a local browser page, organize them by folder or draft status, and export the resulting notes as a .docx file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The app makes an automatic ClawHub update-check request despite offline and no-network claims. <br>
Mitigation: Review before installing for offline or private workflows; make update checks manual, opt-in, or clearly disclosed. <br>
Risk: Notes, images, and uploaded files are retained in browser localStorage and IndexedDB on the user's device. <br>
Mitigation: Use an appropriate browser profile, clear local site data when records should be removed, and avoid shared devices for sensitive notes. <br>


## Reference(s): <br>
- [Product Introduction](references/product-intro.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/weijunz766-collab/skills/suji-board) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file paths, browser usage steps, and optional shell commands for packaging or distributing the HTML app] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The distributed app produces local browser state and downloadable .docx files.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
