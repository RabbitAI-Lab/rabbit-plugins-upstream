## Description: <br>
This skill helps agents inspect, edit, test, and validate remote Git projects over SSH while applying changes through reviewed Git patches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abhhfcgjk](https://clawhub.ai/user/abhhfcgjk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when a source repository is reachable only through SSH and the agent must work locally. It supports remote inspection, focused edits through checked Git patches, environment-aware test commands, and validation without requiring a remote agent runtime. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through the user's configured SSH access, so a mistaken host, project path, or task could affect the wrong remote repository. <br>
Mitigation: Require the SSH alias, absolute project path, environment selector, and task before connecting, then run a preflight check that reports the connected host, working directory, and Git root. <br>
Risk: Remote commands can perform high-impact actions if the user authorizes package installs, deployments, service restarts, database mutations, or destructive Git operations. <br>
Mitigation: Treat those actions as separate authorization boundaries and review them explicitly before execution. <br>
Risk: SSH credentials or application secrets could be exposed if pasted into prompts or files. <br>
Mitigation: Use preconfigured key-based or other non-interactive authentication and never request, store, or print passwords, private keys, API tokens, or environment secret contents. <br>
Risk: Remote edits may overwrite existing work or apply unintended file changes. <br>
Mitigation: Inspect Git status before editing, create focused local Git patches, review patch contents, and apply changes only after git apply --check succeeds. <br>


## Reference(s): <br>
- [Using Work Over SSH](references/usage.md) <br>
- [ClawHub skill page](https://clawhub.ai/abhhfcgjk/skills/work-over-ssh) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/abhhfcgjk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and patch guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local ssh and python3; remote project access depends on preconfigured non-interactive SSH authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
