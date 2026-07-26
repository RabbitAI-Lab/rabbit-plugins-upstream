## Description: <br>
Quipteams (quipteams.com). Use this skill for ANY Quipteams request: searching and reading data through the OOMOL Quipteams connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and agents use this skill to search and read Quipteams employees, assets, device actions, kits, products, and hardware procurement quotes through an OOMOL-connected account. It is suited for business-data lookup tasks where the agent should inspect the connector schema before running read actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Quipteams business data, including employee HRIS metadata, quote recipients, comments, and inventory records. <br>
Mitigation: Use the connected account with the minimum necessary scope and ask the agent to retrieve only the records needed for the task. <br>
Risk: Connector payloads may be incorrect if the agent guesses action parameters. <br>
Mitigation: Have the agent run the connector schema command before constructing each action payload. <br>
Risk: Authentication, connection, scope, credential, or billing errors can interrupt execution. <br>
Mitigation: Follow the first-time setup and recovery guidance only after a matching command failure occurs. <br>


## Reference(s): <br>
- [Quipteams homepage](https://www.quipteams.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quipteams) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides an agent to inspect live connector schemas and run read-oriented Quipteams connector actions with JSON payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
