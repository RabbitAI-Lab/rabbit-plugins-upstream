## Description: <br>
Local Markdown preview skill for opening a browser-based editor and previewer when the user explicitly asks to preview a Markdown file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[webkixi](https://clawhub.ai/user/webkixi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content authors use this skill to preview and edit local Markdown through a localhost browser interface with theme switching, rich-text copy, live refresh, and pasted-image support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The localhost preview server can overwrite the selected Markdown file through unauthenticated local browser-accessible endpoints. <br>
Mitigation: Use the skill only with files you are comfortable editing, keep backups for important Markdown, and close or kill the preview server when the preview session is finished. <br>
Risk: Sensitive or untrusted Markdown may be exposed to the local browser preview workflow and its file-modifying endpoints. <br>
Mitigation: Avoid opening sensitive or untrusted Markdown with this skill unless the local preview behavior and write-back risk are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/webkixi/skills/claw-markdown-preview) <br>
- [clawMarkDown homepage](https://webkixi.github.io/clawmarkdown-home/) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, markdown, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and a localhost browser preview] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Starts a localhost-only preview server; file mode can autosave changes to the selected Markdown file and save pasted images under an images directory.] <br>

## Skill Version(s): <br>
1.4.15 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
