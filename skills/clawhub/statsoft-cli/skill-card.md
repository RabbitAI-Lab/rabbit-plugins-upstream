## Description: <br>
Statsoft-CLI helps agents detect, configure, and invoke local statistical software across R, Stata, SAS, SPSS, Python, Bayesian, machine learning, and related tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to connect AI workflows to local statistical tools, reuse existing scripts, convert datasets, and run confirmed analyses through supported command-line interfaces. It is best suited for trusted local workspaces where the user can review commands before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local statistical binaries and user-provided scripts, which may execute code in the user's environment. <br>
Mitigation: Use trusted workspaces, inspect generated commands, and require explicit confirmation before execution or setting verification/run opt-in flags. <br>
Risk: Some setup flows can run local statistical binaries during verification without the documented verification opt-in. <br>
Mitigation: Review setup commands before running them and avoid verification flows in sensitive environments unless local binary execution is acceptable. <br>
Risk: Configuration writes and dependency downloads can change local state or use the network. <br>
Mitigation: Keep default detect-only behavior, authorize config writes only when intended, rely on backups for config changes, and confirm any downloads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/statsoft-cli) <br>
- [Project homepage](https://github.com/medstatstar/statsoft-cli) <br>
- [README](README.md) <br>
- [Advanced reference](ADVANCED.md) <br>
- [Platform support matrix](references/platform-support.md) <br>
- [Workflow gating details](references/workflow.md) <br>
- [Trust and safety](references/trust-and-safety.md) <br>
- [Command examples](references/command-examples.md) <br>
- [Configuration templates](references/config-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with proposed shell or PowerShell commands and configuration summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Detection is default; persistent config writes, network installs, binary verification, and user-script execution require explicit user opt-in.] <br>

## Skill Version(s): <br>
2.8.2 (source: frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
