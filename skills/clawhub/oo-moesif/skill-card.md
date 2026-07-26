## Description: <br>
Moesif (moesif.com) lets an agent search and read Moesif workspace, app, template, and workspace-list data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to inspect Moesif workspace, app, template, and workspace-list data through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Moesif data through the user's OOMOL-connected account when connector access is available. <br>
Mitigation: Install and invoke it only when Moesif account data access is intended, and review OOMOL CLI sign-in and connection behavior before use. <br>
Risk: Connector commands may fail or use the wrong payload if the live Moesif action contract changes. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before constructing each connector payload. <br>
Risk: Although the listed Moesif actions are read-only, future write or destructive connector actions would carry state-change risk. <br>
Mitigation: Require explicit user confirmation for any action tagged `[write]` or `[destructive]` before running it. <br>


## Reference(s): <br>
- [Moesif homepage](https://www.moesif.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-moesif) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs read-only Moesif connector actions through the oo CLI after inspecting the live action schema.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
