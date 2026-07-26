## Description: <br>
Deploy and manage AI agents (OpenClaw, Claude Code) as first-class participants in a self-hosted Buzz workspace via ACP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darrenjrobinson](https://clawhub.ai/user/darrenjrobinson) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and operators use this skill to deploy OpenClaw or Claude Code agents as Nostr-backed participants in a self-hosted Buzz workspace, including relay setup, agent keys, environment files, systemd services, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Always-on agents can run shell commands without approval while using private keys and model API keys. <br>
Mitigation: Install on a dedicated, low-privilege machine or container, use dedicated Buzz and model API keys, and sandbox or restrict unattended command execution to the Buzz CLI operations required for the deployment. <br>
Risk: Environment files and service configuration can expose Buzz private keys, relay signing keys, or model API keys. <br>
Mitigation: Restrict environment files to the service user, avoid storing unrelated secrets on the host, and rotate any keys that may have been exposed. <br>
Risk: The documented Buzz desktop client flow may involve unsigned desktop installers. <br>
Mitigation: Verify the release source and checksum before running unsigned installers, especially on production or operator workstations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/darrenjrobinson/skills/buzz-acp) <br>
- [Publisher profile](https://clawhub.ai/user/darrenjrobinson) <br>
- [Project homepage](https://github.com/darrenjrobinson/buzz-acp) <br>
- [Buzz project](https://github.com/block/buzz) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Architecture guide](docs/architecture.md) <br>
- [Troubleshooting guide](docs/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include deployment steps, environment variables, systemd unit configuration, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
