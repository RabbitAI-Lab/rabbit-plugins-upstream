## Description: <br>
Scrape documents from Notion, DocSend, PDFs, and other sources into local PDF files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrisling-dev](https://clawhub.ai/user/chrisling-dev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to download, archive, or convert web documents from sources such as Notion, DocSend, direct PDF links, and other pages into local PDF files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may handle sensitive credentials and web-session cookies for protected documents. <br>
Mitigation: Use it only on machines where storing web-session cookies is acceptable, avoid shared systems, and confirm profile purge or logout behavior before providing credentials. <br>
Risk: Generated PDFs and retained sessions may persist locally longer than expected. <br>
Mitigation: Review the storage and cleanup paths before use, run cleanup after sensitive jobs, and confirm retention controls match the user's requirements. <br>
Risk: The release evidence flags unclear package source and background process behavior. <br>
Mitigation: Verify the npm package source before installing and review daemon behavior before running it on systems with sensitive documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrisling-dev/skills/links-to-pdfs) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and local PDF file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs local PDF paths on success and job IDs with required credential types when access is blocked.] <br>

## Skill Version(s): <br>
0.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
