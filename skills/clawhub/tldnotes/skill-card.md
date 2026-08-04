## Description: <br>
用 tldraw 离线画板制作整洁、清晰、有框架感的学神风格板书，包含外框围栏、分区排版、文字、公式、插图、标注和截图验收 guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fslong520](https://clawhub.ai/user/fslong520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide an agent through creating and editing tldraw Desktop canvases for structured teaching notes, study boards, and knowledge-organization visuals. It is intended for local tldraw workflows where the user has explicitly started the desktop canvas server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose a local tldraw bearer token and open-canvas context to the agent. <br>
Mitigation: Treat server.json and injected token values as sensitive, avoid sharing logs or prompts that contain them, and install only when local tldraw API access is acceptable. <br>
Risk: The skill gives the agent broad ability to run editing JavaScript against tldraw documents. <br>
Mitigation: Use it only on documents the user intends to modify, verify document identity before batch or destructive edits, and prefer explicit per-document consent where available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fslong520/skills/tldnotes) <br>
- [tldraw Offline](https://offline.tldraw.com/) <br>
- [tldraw Offline releases](https://github.com/tldraw/tldraw-offline/releases/latest) <br>
- [API reference module](artifact/modules/02-api.md) <br>
- [Server configuration module](artifact/modules/01-server.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent instructions for local tldraw document creation, editing, visual validation, and recovery workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
