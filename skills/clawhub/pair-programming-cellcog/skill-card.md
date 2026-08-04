## Description: <br>
AI pair programming powered by CellCog Desktop for coding, debugging, refactoring, and building directly on a user's machine with terminal access and file operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cellcog](https://clawhub.ai/user/cellcog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to delegate coding, debugging, refactoring, DevOps, data pipeline, and documentation work to CellCog cloud agents connected through CellCog Desktop in a chosen local project directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CellCog cloud agents can run local commands and read or write project files autonomously through CellCog Desktop. <br>
Mitigation: Use a narrowly chosen project directory and avoid workspaces that contain secrets, production data, customer logs, private databases, or unrelated repositories. <br>
Risk: Auto-approved command execution may expose sensitive local context or make unintended project changes. <br>
Mitigation: Review CellCog's desktop, privacy, and retention behavior before enabling co-work, and keep each chat scoped to the intended working directory. <br>


## Reference(s): <br>
- [CellCog SDK and Desktop Documentation](https://cellcog.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/pair-programming-cellcog) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; ClawHub metadata lists darwin, linux, and windows support.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
