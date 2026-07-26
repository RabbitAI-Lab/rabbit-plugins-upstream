## Description: <br>
Use this skill any time a .pptx file is involved, including creating, reading, editing, combining, or splitting PowerPoint presentations and working with templates, layouts, speaker notes, or comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iceyliu](https://clawhub.ai/user/iceyliu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and presentation authors use this skill to have an agent create, inspect, edit, and validate PowerPoint decks with OfficeCLI while following presentation-quality standards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup directs agents to run remote OfficeCLI installer scripts directly in a shell, giving the installer local code-execution authority. <br>
Mitigation: Review the installer before running it, prefer a pinned release or verified binary from a trusted source, and install only when that execution authority is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iceyliu/skills/officecli-pptx) <br>
- [OfficeCLI releases](https://github.com/iOfficeAI/OfficeCLI/releases) <br>
- [OfficeCLI Linux and macOS installer](https://d.officecli.ai/install.sh) <br>
- [OfficeCLI Windows installer](https://d.officecli.ai/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with OfficeCLI shell commands and validation steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or modify .pptx files through OfficeCLI when used by an agent.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
