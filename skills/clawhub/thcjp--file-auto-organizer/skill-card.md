## Description: <br>
File Auto Organizer helps an agent organize selected folders by file type or date, optionally identify duplicates, and produce a simple organization report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to ask an agent for shell-command-oriented guidance to organize explicitly selected folders such as Downloads or Desktop by file type or date and review reported results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: File organization and duplicate deletion can modify or remove user files. <br>
Mitigation: Use the skill only on explicitly chosen folders, create backups first, and require a reviewable deletion list plus confirmation before any duplicate removal. <br>
Risk: Command authority can perform file operations outside the intended scope if commands are not reviewed. <br>
Mitigation: Review proposed commands before execution and run them with the minimum filesystem access needed for the selected folder. <br>
Risk: The artifact mentions API key setup without documenting the external service or data flow. <br>
Mitigation: Do not provide an API key unless the publisher documents the exact service, why the key is needed, and what data will be sent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file-auto-organizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include file-operation recommendations and status/report data; execution should be reviewed before mutating files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
