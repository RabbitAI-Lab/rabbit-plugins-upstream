## Description: <br>
Interact with the system clipboard (text only) using `xclip` from any OpenClaw session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to copy text, paste clipboard contents, and copy file contents through xclip in Linux environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clipboard contents may overwrite existing clipboard data or remain available to other local applications, including sensitive text. <br>
Mitigation: Avoid copying secrets unless necessary, and clear or replace the clipboard after handling sensitive data. <br>
Risk: The skill depends on xclip being installed and available in the local Linux environment. <br>
Mitigation: Install xclip before use and review clipboard commands before executing them. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Text-only clipboard operations; requires xclip.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
