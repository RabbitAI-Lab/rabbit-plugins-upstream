## Description: <br>
Generates hand-drawn Excalidraw-style diagrams from prompts, using a local Docker canvas service to create, export, save, and insert diagram images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhenyangze](https://clawhub.ai/user/zhenyangze) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to turn natural-language diagram requests into Excalidraw-style architecture diagrams, flowcharts, ER diagrams, and similar visuals, then export or insert them into workspace documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start a local Docker-based canvas service. <br>
Mitigation: Use it only where local Docker services are permitted, and stop the container when the canvas service is no longer needed. <br>
Risk: The skill can save or insert generated diagrams into workspace files, which may overwrite or alter files at unintended paths. <br>
Mitigation: Confirm destination and insertion paths before moving or inserting generated files, and review changed files before committing or publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhenyangze/skills/excalidraw-handdraw-skill) <br>
- [Server-resolved GitHub repository](https://github.com/zhenyangze/Excalidraw-Handdraw-Skill) <br>
- [Publisher profile](https://clawhub.ai/user/zhenyangze) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Markdown, Files] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command snippets; exported PNG/SVG diagram files and Markdown image links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May start a local Docker canvas service and write or insert generated diagram files at user-selected paths.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
