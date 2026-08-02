## Description: <br>
libtv-cli guides agents to install and use the LibTV CLI for LibTV canvas, workspace, project, node, model, asset, and workflow operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kgm327](https://clawhub.ai/user/kgm327) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when they need command-line guidance for LibTV canvas workflows, including login, workspace/project binding, node and group operations, uploads, model schema lookup, and pipeline-style automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can download and run remote code without checksum or signature verification. <br>
Mitigation: Use the bundled local installer when possible, install only from trusted LibTV distribution endpoints, and pin `LIBTV_CLI_VERSION` for repeatable installs. <br>
Risk: Remote install examples include piping downloaded scripts directly into a shell or PowerShell session. <br>
Mitigation: Review downloaded installer scripts before execution and avoid direct pipe-to-shell execution in sensitive environments. <br>
Risk: LibTV commands can affect the active account, project, uploaded assets, node graph, or generation runs. <br>
Mitigation: Confirm the active account, workspace, project, and group binding before uploads, deletes, or generation commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kgm327/skills/libtv-cli-skill) <br>
- [LibTV web app](https://www.liblib.art/tv/zh) <br>
- [LibTV install channel endpoint](https://api2.liblib.art/api/www/landing-activities/getById?id=240) <br>
- [Installation guide](scripts/install.md) <br>
- [Command reference map](SKILL.md) <br>
- [Workflow examples](examples/README.md) <br>
- [Pipe and NDJSON conventions](examples/pipes/README.md) <br>
- [Model schema reference](model-schema/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command output expectations such as JSON, NDJSON, stdout/stderr conventions, and local configuration paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
