## Description: <br>
Guides agents to produce defensive GNU Bash 4.4+ scripts for Linux, including safe foundations, argument parsing, production patterns, and ShellCheck/shfmt validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when asking an agent to write or review Linux Bash scripts, shell scripts, cron jobs, deployment automation, backup rotation, or CLI tooling. It emphasizes defensive scripting practices, safe handling of untrusted input, and validation with ShellCheck and shfmt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Bash scripts may include destructive file operations, network calls, cron usage, or system changes. <br>
Mitigation: Review generated scripts before execution, especially commands that delete files, modify system state, make network requests, or schedule recurring work. <br>
Risk: Incorrect Bash guidance can lead to unsafe handling of untrusted input or brittle automation. <br>
Mitigation: Prefer the skill's defensive patterns, avoid eval and shell-built heredocs from external data, and run ShellCheck and shfmt before relying on generated scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-linux-bash-scripting) <br>
- [Runtime instructions](artifact/SKILL.md) <br>
- [Skill specification](artifact/SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Bash code blocks and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets GNU Bash 4.4+ on Linux and recommends ShellCheck plus shfmt validation before use.] <br>

## Skill Version(s): <br>
4.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
