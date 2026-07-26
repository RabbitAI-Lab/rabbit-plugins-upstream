## Description: <br>
定时守护 helps agents harden cron jobs and unattended background scripts by applying script-first execution, explicit environment setup, quiet-success behavior, cross-platform templates, and troubleshooting patterns for common scheduled-task failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review, write, and harden cron jobs, CI scheduled tasks, background workers, and long-running agent scripts so they behave predictably across POSIX and Windows environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated cron or background-job scripts may be run unattended and can affect scheduled execution, environment variables, filesystem cleanup, or git push behavior. <br>
Mitigation: Review generated scripts before running them, test in a cron-like minimal environment, document required environment variables, avoid force-push, and keep cleanup commands narrowly scoped. <br>
Risk: The skill may trigger on broad shell or reliability requests outside cron or unattended-script hardening. <br>
Mitigation: Use it for cron jobs, scheduled tasks, background workers, and unattended-script reliability work; verify relevance before applying its checklists to unrelated shell tasks. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell, Python, and PowerShell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include checklists, hardening templates, and troubleshooting guidance for scheduled jobs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
