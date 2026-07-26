## Description: <br>
Deploys TeslaMate on a local or remote Debian-family Linux host with pre-flight checks, bundled shell scripts, post-install health checks, and a generated usage document. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[martinbj2008](https://clawhub.ai/user/martinbj2008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and TeslaMate users use this skill to install TeslaMate, Grafana, PostgreSQL, and Mosquitto on an existing Debian-family host and verify that the deployment is reachable. It is scoped to installation, health checks, troubleshooting guidance, and a user-facing usage document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer makes broad server changes, including Docker installation, Docker daemon configuration, service restarts, and container deployment. <br>
Mitigation: Run it only on a dedicated Debian or Ubuntu host you are comfortable reconfiguring, and back up existing Docker configuration before deployment. <br>
Risk: Password-based SSH, sshpass, and relaxed host-key handling can expose credentials or connect to an unintended host. <br>
Mitigation: Prefer SSH keys with verified host keys, avoid password SSH where possible, and confirm the target host before running remote deployment. <br>
Risk: Default database/encryption values and exposed ports 3000, 4000, and 1883 can leave TeslaMate, Grafana, or MQTT accessible with weak protection. <br>
Mitigation: Generate unique TeslaMate encryption and database secrets, change Grafana defaults, and restrict service ports with a firewall, trusted IP allowlist, or reverse proxy before exposing the host. <br>
Risk: The GitHub image fallback downloads container image archives from a third-party repository when Docker pulls fail. <br>
Mitigation: Use the fallback only if the repository is independently trusted, and rely on the included checksum verification before loading images. <br>


## Reference(s): <br>
- [TeslaMate Deploy Troubleshooting](references/troubleshooting.md) <br>
- [TeslaMate Deploy Scripts README](scripts/README.md) <br>
- [Tesla Developer API Access](https://developer.tesla.com/) <br>
- [TeslaMate Backup Guide](https://docs.teslamate.org/docs/guides/backup) <br>
- [Docker Image Fallback Repository](https://github.com/martinbj2008/docker_images) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and deployment notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate a Markdown usage document with service URLs, credential-change reminders, and follow-up operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
