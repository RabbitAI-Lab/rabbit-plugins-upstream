## Description: <br>
Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivansslo](https://clawhub.ai/user/ivansslo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to decide when independent tasks can be delegated to specialized subagents in parallel and how to review their results before integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Launching several subagents at once can create conflicting edits or duplicated work if the tasks are not clearly independent. <br>
Mitigation: Use parallel dispatch only for clearly separate task domains, then review each summary, check for conflicts, and run the full suite before accepting changes. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/ivansslo/Supwrs/tree/main/skills/dispatching-parallel-agents) <br>
- [ClawHub skill page](https://clawhub.ai/ivansslo/skills/dispatching-parallel-agents-3) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown guidance with examples and prompt patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only coordination guidance; no tools, credentials, or API calls are declared.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
