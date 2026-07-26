## Description: <br>
Use the zentao CLI to login and query ZenTao products and bugs. ZENTAO_URL usually includes /zentao. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and project teams use this skill to install and run the zentao CLI for logging in to ZenTao, listing products, querying bugs, viewing bug details, and checking assigned bugs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ZenTao login credentials are entered on the command line and saved in local CLI configuration. <br>
Mitigation: Avoid long-lived or highly privileged passwords when possible, and review or remove ~/.config/zentao/config.toml or $XDG_CONFIG_HOME/zentao/config.toml when stored credentials are no longer needed. <br>


## Reference(s): <br>
- [ClawHub zentao skill](https://clawhub.ai/leeguooooo/skills/zentao) <br>
- [@leeguoo/zentao-mcp npm package](https://www.npmjs.com/package/@leeguoo/zentao-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can request JSON output with --json and may read or write local ZenTao CLI configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
