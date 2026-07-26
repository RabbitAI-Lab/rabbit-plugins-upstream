## Description: <br>
Run arbitrary commands when files change. Useful for watching files and triggering builds or tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to set up file-watch workflows with entr, such as rerunning tests, rebuilds, or server processes when files change. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill helps run arbitrary development commands when files change, including shell-evaluated commands with entr -s. <br>
Mitigation: Review the exact command before running it and avoid shell-evaluated commands unless the inputs and working directory are trusted. <br>
Risk: entr can block the terminal or keep a watch process running longer than intended. <br>
Mitigation: Run watch sessions in a managed background process when other work must continue, and stop the process when it is no longer needed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are examples for the user or agent to review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
