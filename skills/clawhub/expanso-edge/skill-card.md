## Description: <br>
Data processing pipelines for OpenClaw. Deploy skills from the Expanso marketplace to transform, analyze, and process data locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aronchick](https://clawhub.ai/user/aronchick) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and data teams use expanso to install Expanso Edge and CLI, connect a local Edge node to Expanso Cloud, and deploy marketplace data-processing pipelines for OpenClaw. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup runs remote installer scripts and starts a cloud-connected local runtime. <br>
Mitigation: Install only from trusted Expanso domains, review or verify installer scripts before running them, and run Expanso Edge with least local privilege. <br>
Risk: The bootstrap token connects a local Edge node to an Expanso Cloud organization. <br>
Mitigation: Protect the bootstrap token as a secret, avoid logging it, rotate it if exposed, and scope access through Expanso Cloud settings. <br>
Risk: Marketplace pipelines may process sensitive local data. <br>
Mitigation: Review each deployed pipeline before use and confirm it is appropriate for the data being processed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aronchick/skills/expanso-edge) <br>
- [Expanso Skills Marketplace](https://skills.expanso.io) <br>
- [Expanso Documentation](https://docs.expanso.io) <br>
- [Expanso Cloud](https://cloud.expanso.io) <br>
- [Expanso Edge installer](https://get.expanso.io/edge/install.sh) <br>
- [Expanso CLI installer](https://get.expanso.io/cli/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl plus EXPANSO_EDGE_BOOTSTRAP_URL and EXPANSO_EDGE_BOOTSTRAP_TOKEN.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
