## Description: <br>
Advanced filesystem operations - listing, searching, batch processing, and directory analysis for Clawdbot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to list, search, copy, visualize, and analyze files and directories while applying configurable filters and safety controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad filesystem read-write capability and is intended to inspect and copy files. <br>
Mitigation: Install only when the workspace and trust boundary are appropriate, and review paths and copy operations before execution. <br>
Risk: The submitted artifact appears incomplete because the declared executable is missing, so it may not work as advertised. <br>
Mitigation: Confirm the runtime implementation is present in the package actually installed before relying on the commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/filesystem) <br>
- [Node.js runtime](https://nodejs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with command examples and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON-formatted listings or analysis summaries when requested.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
