## Description: <br>
Guides users through opening a local HTML file scanner, selecting files, and packaging selected files into a ZIP backup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwei03804-a11y](https://clawhub.ai/user/wwei03804-a11y) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to get operating-system-specific guidance for opening a local file-scanning HTML page, reviewing file metadata, selecting files, and downloading a ZIP backup. Use should be limited to files the user owns or is explicitly authorized to export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is framed around pre-resignation file collection, which can encourage unauthorized export of employer, customer, confidential, or regulated data. <br>
Mitigation: Use only with files the user owns or has explicit written permission to export, and avoid employer, customer, confidential, regulated, or offboarding data unless authorization is documented. <br>
Risk: The HTML scanner claims local-only handling but loads third-party CDN scripts. <br>
Mitigation: Review the CDN dependencies before use and disclose that opening the scanner requires network-loaded browser scripts, so the local-only privacy claim is incomplete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwei03804-a11y/skills/shanku-paolu-1-0-0) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Files] <br>
**Output Format:** [Markdown guidance with references to a bundled HTML file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled HTML page can scan local file metadata and package selected browser-accessible files into a ZIP archive.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
