## Description: <br>
Code Analyzer helps agents inspect codebases for architecture, execution flow, data flow, business rules, dependencies, data models, and DDD patterns across common programming languages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to generate Markdown codebase analysis reports for onboarding, architecture documentation, code review preparation, technical debt assessment, and DDD pattern recognition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads the project path selected by the user, which could expose unrelated private files if pointed at a broad directory. <br>
Mitigation: Run it only on the intended project path and use --exclude for sensitive folders that are not needed for analysis. <br>
Risk: The skill writes a Markdown report to the output path selected by the user, which could overwrite an existing file. <br>
Mitigation: Choose a new report filename or confirm the destination before running the analyzer. <br>


## Reference(s): <br>
- [Code Analysis Best Practices](artifact/references/best-practices.md) <br>
- [OpenClaw Documentation](https://docs.openclaw.ai) <br>
- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/code-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown reports with analysis summaries, metrics, findings, recommendations, and Mermaid architecture diagrams.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes reports to a user-selected output path; supports excluding selected directories from analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
