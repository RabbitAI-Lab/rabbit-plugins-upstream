## Description: <br>
Manages WEEEK task-manager data through the WEEEK Public API, including listing, creating, updating, completing, reopening, and moving tasks across boards and columns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alex-indi](https://clawhub.ai/user/alex-indi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and WEEEK workspace users can use this skill to have an agent prepare or run task, board, and column operations through a local CLI backed by the WEEEK Public API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use WEEEK_TOKEN to read and modify WEEEK tasks. <br>
Mitigation: Install it only for intended WEEEK task-management work, keep WEEEK_TOKEN private, and use the narrowest token permissions available. <br>
Risk: Create, update, complete, uncomplete, and move commands can change workspace task state. <br>
Mitigation: Review mutating commands and their task, board, and column IDs before execution, especially in shared workspaces. <br>
Risk: Task date inputs may be sensitive to the WEEEK API date format expected for a given operation. <br>
Mitigation: Confirm date values before running commands; the included API notes document dd.mm.yyyy for date ranges and flag day-format ambiguity. <br>


## Reference(s): <br>
- [WEEEK Public API notes](references/api.md) <br>
- [WEEEK Public API base endpoint](https://api.weeek.net/public/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON] <br>
**Output Format:** [Agent-facing guidance and shell commands, with JSON responses from WEEEK API calls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided WEEEK_TOKEN environment variable; WEEEK_USER_ID is optional.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
