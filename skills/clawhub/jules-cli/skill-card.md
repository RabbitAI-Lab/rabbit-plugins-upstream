## Description: <br>
Interact with the Jules CLI to manage asynchronous coding sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajstafford](https://clawhub.ai/user/ajstafford) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create, monitor, and integrate remote Jules CLI coding sessions for complex, isolated tasks that benefit from a separate VM. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote Jules sessions may send selected coding tasks and repository context to a separate Jules environment. <br>
Mitigation: Use the skill only when the local Jules CLI is trusted and approve new sessions deliberately. <br>
Risk: Pulling or teleporting completed session changes can modify the local codebase. <br>
Mitigation: Require explicit approval for pull --apply and teleport, then review and test returned changes before relying on them. <br>


## Reference(s): <br>
- [Jules CLI Usage Reference](references/usage.md) <br>
- [ClawHub listing](https://clawhub.ai/ajstafford/skills/jules-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local jules and python3 binaries and the HOME environment variable.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
