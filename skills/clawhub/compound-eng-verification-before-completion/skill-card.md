## Description: <br>
Enforces fresh verification evidence before any completion claim. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this discipline skill to require immediate, command-backed verification before claiming work is complete. It also helps agents confirm ambiguous change scope before editing and select verification strategies suited to the change type. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause agents to propose or run broad verification commands on large projects or long-running suites. <br>
Mitigation: Review proposed verification commands when they touch large projects, long-running test suites, or broad filesystem scope. <br>
Risk: Incorrect or stale verification guidance could lead an agent to overstate completion confidence. <br>
Mitigation: Require fresh command output and explicit failure reporting before accepting any completion claim. <br>


## Reference(s): <br>
- [Isolated Verification](references/isolated-verification.md) <br>
- [System-Wide Test Check](references/system-wide-test-check.md) <br>
- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured completion reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts the agent to provide fresh verification evidence, scope confirmation, and command results before completion claims.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
