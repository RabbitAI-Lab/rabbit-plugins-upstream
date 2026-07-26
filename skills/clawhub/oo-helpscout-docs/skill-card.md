## Description: <br>
Help Scout Docs lets an agent search and read Help Scout Docs through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support teams use this skill to let an agent list, search, and retrieve Help Scout Docs sites, collections, categories, and articles through an OOMOL-connected Help Scout account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads Help Scout Docs through an OOMOL-connected account, which can expose private documentation available to that account. <br>
Mitigation: Install and use it only in trusted contexts, confirm the OOMOL connection is approved, and review returned content before sharing it externally. <br>
Risk: CLI installation, login, billing, or account-connection steps can affect the user's local environment or OOMOL account state. <br>
Mitigation: Treat setup and recovery commands as user-approved actions, and run them only after a command fails with the matching setup, auth, connection, or billing error. <br>
Risk: Connector payloads can fail or query the wrong scope if they are built from stale assumptions. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before building payloads and keep routine use to the documented read, list, and search actions. <br>


## Reference(s): <br>
- [Help Scout](https://www.helpscout.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Help Scout Docs actions; inspect the live connector schema before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
