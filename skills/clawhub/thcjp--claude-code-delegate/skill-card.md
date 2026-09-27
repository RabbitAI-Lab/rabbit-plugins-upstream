## Description: <br>
Delegates coding, debugging, testing, and development tasks to a local ai-assistant CLI while guiding the host agent to relay results back to the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to delegate programming tasks, code review, debugging, test execution, and iterative fixes to a local coding CLI. It is intended for clear technical tasks with an identified project directory and constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The delegated local CLI may read or modify files broadly when permission bypass is enabled. <br>
Mitigation: Run it only in an isolated project directory, enable a real write guard or sandbox, and keep it away from home directories, system configuration, and repositories containing secrets. <br>
Risk: Automatic delegation can execute unclear or overly broad coding tasks against the wrong path. <br>
Mitigation: Confirm the exact task, target directory, and constraints before delegation, and review the delegated output before acting on it. <br>
Risk: Delegated code or test results may be incomplete or incorrect. <br>
Mitigation: Use a fresh independent verification run and review changed files, test output, and reported errors before accepting the result. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with shell command examples and delegated CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Delegated runs may return session identifiers, status updates, test results, error summaries, and file-change summaries.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 0.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
