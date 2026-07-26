## Description: <br>
Runs base64-encoded shell commands through a Python wrapper and returns command output and exit status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zww-v5](https://clawhub.ai/user/zww-v5) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill when a workflow specifically requires invoking a Python command wrapper instead of calling a shell directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad local shell-execution capability through an encoded command wrapper. <br>
Mitigation: Install only when command execution is the intended capability, review every command before use, and avoid passing untrusted input. <br>
Risk: The security summary notes weak scoping and incomplete disclosure for the command-running behavior. <br>
Mitigation: Prefer a narrower allowlisted skill for routine administrative tasks and document the exact commands or command families permitted in the deployment. <br>


## Reference(s): <br>
- [Command Runner Skill Page](https://clawhub.ai/zww-v5/skills/command-runner) <br>
- [Reference Documentation for Command Runner](references/api_reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands] <br>
**Output Format:** [Base64-encoded stdout text, stderr text, and numeric process exit code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Executes decoded commands locally with shell=True; stdout is base64-encoded by the wrapper.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
