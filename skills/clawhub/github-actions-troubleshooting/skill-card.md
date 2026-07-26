## Description: <br>
Troubleshoot GitHub Actions workflows, particularly for Go projects. Diagnose failing workflows, distinguish between code and environment issues, interpret logs, and apply fixes for common CI/CD problems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[irook661](https://clawhub.ai/user/irook661) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to investigate failing GitHub Actions runs, inspect logs and artifacts, and apply targeted fixes for Go CI/CD failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitHub CLI commands may act on the wrong account or repository if authentication or repository arguments are incorrect. <br>
Mitigation: Confirm `gh` is authenticated to the intended account and run commands only against repositories in scope for the task. <br>
Risk: Downloaded workflow artifacts may contain sensitive build output or logs. <br>
Mitigation: Review downloaded artifacts before sharing or committing any content derived from them. <br>
Risk: Troubleshooting may propose dependency or configuration changes that affect CI behavior. <br>
Mitigation: Inspect changes to files such as `go.mod`, `go.sum`, workflow files, and linter configuration before committing. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GitHub CLI and Git commands, diagnostic steps, and proposed configuration or dependency-file changes for user review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
