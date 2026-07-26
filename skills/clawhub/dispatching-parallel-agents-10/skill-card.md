## Description: <br>
Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivansslo](https://clawhub.ai/user/ivansslo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to split independent debugging or implementation work into focused parallel subagent tasks, then review and integrate the results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Parallel agents can interfere with each other when tasks share files, state, or sequential dependencies. <br>
Mitigation: Dispatch only clearly independent domains, constrain each agent scope, review returned changes for conflicts, and run the full relevant test suite before integration. <br>
Risk: The security review notes broad repository reading and optional edits to documentation or agent-governance files. <br>
Mitigation: Use a narrow file scope or report-only mode when broad documentation review or instruction edits are not desired, and review proposed changes before deployment. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/ivansslo/Supwrs/tree/main/skills/dispatching-parallel-agents) <br>
- [ClawHub skill page](https://clawhub.ai/ivansslo/skills/dispatching-parallel-agents-10) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance with examples and prompt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No external tools, credentials, or code execution required.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
