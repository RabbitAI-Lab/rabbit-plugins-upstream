## Description: <br>
QA QuickCheck is an AI-assisted daily testing skill for PR static review, dynamic functional testing, Git diff regression planning, and structured test reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[houyang995](https://clawhub.ai/user/houyang995) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to run quick or standard QA checks before pull requests, merges, and routine code changes. It guides static audit, HTTP functional testing, security header checks, regression scoping, and generation of a structured test report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run project startup commands, execute helper scripts, send HTTP requests, and create or overwrite test-report.md. <br>
Mitigation: Run it only in a controlled workspace, review generated commands and configured URLs first, and preserve any existing report files that must not be overwritten. <br>
Risk: The data factory supports custom template expressions and can post generated records to configured URLs. <br>
Mitigation: Use only trusted templates, avoid custom expressions unless reviewed, and restrict POST targets to local or confirmed test services. <br>
Risk: Dynamic testing can interact with services using environment-derived values or configured endpoints. <br>
Mitigation: Avoid running with sensitive environment variables and keep tests pointed at local, staging, or otherwise authorized environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/houyang995/skills/qa-quickcheck) <br>
- [README](README.md) <br>
- [Scheduler and mode mapping](references/00-调度器.md) <br>
- [Static code audit](references/01-静态代码审计.md) <br>
- [Dynamic functional testing](references/02-动态功能测试.md) <br>
- [Regression testing strategy](references/00-D-回归测试策略.md) <br>
- [Report template and traceability mapping](references/00-B-报告模板与追溯映射.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, structured execution summaries, and terminal output from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may create or overwrite test-report.md and may run helper scripts that send HTTP requests to configured local or test URLs.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
