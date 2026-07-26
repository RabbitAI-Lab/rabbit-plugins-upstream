## Description: <br>
A multifunction utility toolbox that helps agents provide image, PDF, video, data conversion, text, developer, education, everyday utility, and system tools, including v3.6 additions for file hashing, UUIDs, timestamps, IP tools, expanded unit conversion, and MD5/SHA/base conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill as a general-purpose toolbox for calculations, conversions, local file utilities, HTTP checks, media/PDF/image workflows, and system-resource inspection from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a broad local toolbox that can read and write user-selected files, inspect local system resources, and rename files after preview. <br>
Mitigation: Use it only in directories you intend to modify, review paths and previews before confirming operations, and keep backups for important files. <br>
Risk: The skill can make outbound requests to user-supplied and third-party URLs. <br>
Mitigation: Use trusted URLs, avoid sending sensitive data, and treat responses from third-party services as untrusted input. <br>
Risk: The security evidence says file-safety and network-safety promises are weaker than the included examples consistently enforce. <br>
Mitigation: Do not rely solely on the documented filters; review proposed file and network actions before execution, especially around protected or sensitive file types. <br>
Risk: Some features require optional dependencies or external tools such as Pillow, PyPDF2, rembg, jieba, qrcode, or FFmpeg. <br>
Mitigation: Confirm package names and install commands before running them, prefer isolated environments, and install only the dependencies needed for the requested task. <br>


## Reference(s): <br>
- [Dgngjx Skill on ClawHub](https://clawhub.ai/fyniujin/skills/dgngjx-skill) <br>
- [Online Mortgage Calculator](https://www.zhujisuanqi.com/) <br>
- [Tax Calculator](https://www.taxcalculator.com) <br>
- [Base64 Online](https://www.base64encode.org/) <br>
- [Photopea](https://www.photopea.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose optional dependency installation commands and file operations that require user confirmation.] <br>

## Skill Version(s): <br>
3.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
