## Description: <br>
Generate Mindmap helps agents create interactive mind maps from Markdown outlines or JSON input and export them as HTML, PNG, JPG, SVG, PDF, or XMin files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and knowledge workers use this skill to turn structured outlines or JSON data into interactive mind maps and exportable visual files for planning, documentation, and learning workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad file processing, command execution, API use, and API-key handling beyond the core mind map task. <br>
Mitigation: Review the skill before installation, use it only for explicit mind map generation, and avoid unrelated file-processing or command-execution requests. <br>
Risk: The artifact mentions API-key configuration without documenting a specific provider or data flow. <br>
Mitigation: Do not provide API keys unless the publisher documents the exact provider, purpose, and handling path. <br>
Risk: Mind map generation may read from and write to local files. <br>
Mitigation: Run with least-privilege file access and review requested paths before allowing file writes or exports. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/generate-mindmap) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON-guided mind map outputs, including HTML, PNG, JPG, SVG, PDF, and XMin files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require local file read/write and command execution permissions; scope execution to the requested mind map task.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
