## Description: <br>
Automatically monitors CI/CD pipeline status for GitHub and GitLab after repository pushes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okoddcat](https://clawhub.ai/user/okoddcat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use GitFlow to push local commits, monitor GitHub and GitLab CI pipelines, inspect run status and logs, and rerun failed jobs from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can push code or rerun CI using the user's credentials, which may affect remote branches or pipelines if used without confirmation. <br>
Mitigation: Require explicit confirmation before every push or rerun, verify the remote and branch, and avoid broad access tokens. <br>
Risk: CI logs and pipeline output can contain sensitive information. <br>
Mitigation: Treat CI logs as sensitive, review output before sharing it, and redact secrets or internal details. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and git alias configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose commands that push commits, monitor CI logs, or rerun failed jobs; users should confirm repository, branch, and credentials first.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
