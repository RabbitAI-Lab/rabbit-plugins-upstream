## Description: <br>
Installs TeslaMate on a local machine or remote Linux server by guiding target selection, pre-flight checks, deployment, post-install health checks, and a generated usage document. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[martinbj2008](https://clawhub.ai/user/martinbj2008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and self-hosting operators use this skill to perform a fresh TeslaMate install on an existing Debian or Ubuntu host, then verify the deployment and receive operating notes. It is scoped to installation and documentation, not VM provisioning, upgrades, HTTPS setup, backup, restore, or high-availability operation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release asks the agent to run deployment scripts that are not included in the submitted artifact. <br>
Mitigation: Review the skill before installing and confirm the expected scripts and compose file from the source before running it on any host. <br>
Risk: The deployment can expose TeslaMate, Grafana, and MQTT services and may start with default credentials or keys. <br>
Mitigation: Run on a non-sensitive host first, change default credentials and encryption keys, and firewall ports 3000, 4000, and 1883 to trusted clients. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/martinbj2008/my_teslamate) <br>
- [ClawHub skill page](https://clawhub.ai/martinbj2008/skills/my-teslamate) <br>
- [TeslaMate initial setup guide](https://docs.teslamate.org/docs/guides/initial_setup) <br>
- [TeslaMate backup guide](https://docs.teslamate.org/docs/guides/backup) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and a generated usage document] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes access URLs, service health-check output, operating commands, and security notes for the deployed stack.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
