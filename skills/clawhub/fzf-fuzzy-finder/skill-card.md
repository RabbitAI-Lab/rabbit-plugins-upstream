## Description: <br>
Command-line fuzzy finder for interactive filtering and selection - integrates with shell, vim, and other tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnarsson](https://clawhub.ai/user/arnarsson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and command-line users use this skill to get practical fzf command examples for interactive file selection, shell integration, git workflows, process management, and tool configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some optional shell examples can delete files, kill processes, or affect Docker and Kubernetes resources if copied without review. <br>
Mitigation: Review commands before execution, add confirmation or dry-run steps where available, and verify the active shell, Docker, and Kubernetes context. <br>
Risk: The history replay alias can execute a previously selected command unexpectedly. <br>
Mitigation: Avoid the history replay alias or inspect and edit the selected command before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arnarsson/skills/fzf-fuzzy-finder) <br>
- [fzf homepage](https://github.com/junegunn/fzf) <br>
- [fzf wiki](https://github.com/junegunn/fzf/wiki) <br>
- [fzf examples](https://github.com/junegunn/fzf/wiki/examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the fzf binary for the described command-line workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
