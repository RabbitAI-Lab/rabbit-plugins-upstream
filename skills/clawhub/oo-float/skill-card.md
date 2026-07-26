## Description: <br>
Float (float.com). Use this skill for ANY Float request - searching and reading data. Whenever a task involves Float, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to query a connected Float workspace through OOMOL for accounts, clients, people, projects, and allocations. It is intended for read-only Float search and retrieval workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read-only Float connector calls may expose business data such as people, clients, projects, and allocations. <br>
Mitigation: Install only for agents that should query the connected Float workspace, and clarify ambiguous Float requests before running connector calls. <br>
Risk: Connector execution depends on a signed-in OOMOL account, an active Float connection, sufficient scopes, and available billing credit. <br>
Mitigation: Use the documented first-time setup only after a command fails for the matching reason, then retry after the account, connection, scope, expiration, or billing issue is resolved. <br>


## Reference(s): <br>
- [Float homepage](https://www.float.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-float) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
