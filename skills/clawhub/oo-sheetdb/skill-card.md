## Description: <br>
SheetDB helps agents read, search, create, update, and delete SheetDB spreadsheet rows through an OOMOL-connected SheetDB account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect SheetDB schemas and safely read, search, create, update, or delete spreadsheet rows through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete spreadsheet rows in the connected SheetDB account. <br>
Mitigation: Confirm the exact payload, matching criteria, and expected effect with the user before any write or destructive action. <br>
Risk: The skill depends on the oo CLI and an OOMOL-connected SheetDB account. <br>
Mitigation: Install and use it only when SheetDB access through the connected account is intended, and review the oo CLI installation source before running installer commands. <br>
Risk: Incorrect action payloads or stale schema assumptions could affect the wrong data. <br>
Mitigation: Fetch the live action schema with `oo connector schema` before constructing each action payload. <br>


## Reference(s): <br>
- [SheetDB homepage](https://sheetdb.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub SheetDB skill page](https://clawhub.ai/oomol/skills/oo-sheetdb) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live schema inspection before action payloads and explicit user confirmation for write or destructive actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
