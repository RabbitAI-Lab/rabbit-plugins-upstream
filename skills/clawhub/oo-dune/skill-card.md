## Description: <br>
Dune (dune.com). Use this skill for ANY Dune request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to let an agent inspect Dune connector schemas, run saved Dune queries through an OOMOL-connected account, poll execution status, and retrieve query results or metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can access Dune query SQL, ownership, metadata, and results through the connected OOMOL/Dune account. <br>
Mitigation: Install and use the skill only for accounts and workspaces where agent access to that Dune data is intended. <br>
Risk: First-time setup may require installing the oo CLI and signing in to OOMOL. <br>
Mitigation: Use the documented OOMOL setup flow only when the command fails for a missing CLI, authentication, or connection reason. <br>
Risk: Saved Dune queries can be executed under the connected account. <br>
Mitigation: Review the live action schema and JSON payload before running query executions that could expose sensitive parameters or results. <br>


## Reference(s): <br>
- [Dune homepage](https://dune.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dune) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when an execution is started.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
