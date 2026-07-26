## Description: <br>
Cross-platform statistical software CLI integration for AI agents, covering 34+ packages including R, Stata, SAS, SPSS, Python, Bayesian, and machine learning tools, with bilingual guidance for activating historical code assets in AI workflow automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and statisticians use this skill to detect, configure, and run local statistical software from an agent workflow. It helps reuse existing R scripts, SPSS syntax, SAS macros, Stata do-files, and related project assets as workflow steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup and detection flows can execute local statistical programs or third-party binaries. <br>
Mitigation: Review generated commands before execution, prefer a sandbox or disposable environment, and keep STATSOFT_VERIFY unset unless intentional verification is needed. <br>
Risk: Configuration changes can persist local software paths to config.json. <br>
Mitigation: Keep STATSOFT_AUTO_WRITE and STATSOFT_CONFIRM unset unless persistence is intended; rely on the documented backup and explicit authorization flow before writing. <br>
Risk: Running user scripts through R, Stata, SPSS, SAS, CmdStan, or similar tools can execute untrusted code. <br>
Mitigation: Inspect user scripts first, avoid sensitive projects, and keep STATSOFT_CMDSTAN_RUN unset unless compiling and running a supplied Stan model is intended. <br>
Risk: Scan and setup output can disclose local installation paths and version details. <br>
Mitigation: Keep STATSOFT_REVEAL unset unless path and version disclosure is necessary for the task. <br>


## Reference(s): <br>
- [Statsoft Cli on ClawHub](https://clawhub.ai/medstatstar/skills/statsoft-cli) <br>
- [Additional Statistical Software Support](ADDITIONAL_SOFTWARE.md) <br>
- [Command Examples](references/command-examples.md) <br>
- [Configuration Templates](references/config-templates.md) <br>
- [Platform Support](references/platform-support.md) <br>
- [Version Specifics](references/version-specifics.md) <br>
- [Trust and Safety](references/trust-and-safety.md) <br>
- [Workflow Gating Detail](references/workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local scan, setup, verification, and execution commands for third-party statistical software; persistence and disclosure controls are opt-in.] <br>

## Skill Version(s): <br>
2.7.1 (source: frontmatter, changelog, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
