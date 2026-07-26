## Description: <br>
PikaBoard helps agents interact with the PikaBoard task management API to create, update, list, and manage kanban tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[angelstreet](https://clawhub.ai/user/angelstreet) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use PikaBoard to connect agents to a local task board, manage task status, and map each agent to its own board. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A PikaBoard API token can expose task-board access if copied into shared files or logs. <br>
Mitigation: Use a dedicated token, keep it in private environment files or shell environment variables, and do not store the real token in shared documentation. <br>
Risk: Agent automation can create or change tasks and boards that PikaBoard treats as the source of truth. <br>
Mitigation: Configure MY_BOARD_ID before agent use and require confirmation for task or board changes that matter. <br>
Risk: Installation builds a Node.js application and npm dependencies from the configured repository. <br>
Mitigation: Install only after reviewing and trusting the PikaBoard repository and its npm dependency set. <br>


## Reference(s): <br>
- [PikaBoard ClawHub page](https://clawhub.ai/angelstreet/skills/pikaboard) <br>
- [PikaBoard repository from install metadata](https://github.com/angelstreet/pikaboard) <br>
- [API documentation pointer](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands, environment variables, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm; uses PIKABOARD_API, PIKABOARD_TOKEN, AGENT_NAME, and optional board variables.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
