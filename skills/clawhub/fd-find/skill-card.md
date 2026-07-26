## Description: <br>
A fast and user-friendly alternative to 'find' - simple syntax, smart defaults, respects gitignore. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnarsson](https://clawhub.ai/user/arnarsson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and command-line users use this skill to find files and directories with fd, including common filters for name, extension, type, size, time, and ignored or hidden paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Examples that pipe fd results into rm, xargs rm, or use -x rm can delete unintended files if run from the wrong directory or with an overly broad pattern. <br>
Mitigation: Preview matched files first, verify the working directory and pattern, and only then run deletion commands in the intended directory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arnarsson/skills/fd-find) <br>
- [fd GitHub repository](https://github.com/sharkdp/fd) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the fd command-line binary; examples may be combined with tools such as ripgrep, fzf, bat, xargs, and rm.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
