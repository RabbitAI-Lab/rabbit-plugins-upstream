## Description: <br>
SheetDB lets an agent read, create, update, and delete SheetDB spreadsheet data through an OOMOL-connected SheetDB account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected SheetDB spreadsheet from an agent, including inspecting metadata and rows, searching records, and performing confirmed row creation, updates, or deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete rows in the connected SheetDB spreadsheet. <br>
Mitigation: Confirm the exact payload, target rows, and expected effect with the user before running write or destructive actions. <br>
Risk: First-time setup can require installing the oo CLI or connecting the user's OOMOL account. <br>
Mitigation: Only perform installation or account connection after an auth or connection failure and with explicit user approval. <br>


## Reference(s): <br>
- [SheetDB homepage](https://sheetdb.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [OOMOL SheetDB connection](https://console.oomol.com/app-connections?provider=sheetdb) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sheetdb) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [State-changing actions require user confirmation; connector responses are JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
