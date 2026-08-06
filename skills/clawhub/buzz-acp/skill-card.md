## Description: <br>
Deploy and manage AI agents (OpenClaw, Claude Code) as first-class participants in a self-hosted Buzz workspace via ACP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darrenjrobinson](https://clawhub.ai/user/darrenjrobinson) <br>

### License/Terms of Use: <br>
Apache License <br>


## Use Case: <br>
Developers and engineers use this skill to connect OpenClaw, Claude Code, or other ACP-compatible agents to a self-hosted Buzz workspace with separate agent identities, relay membership, and message posting paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can post immediate AI replies into shared Buzz channels and DMs. <br>
Mitigation: Deploy only in workspaces where immediate agent replies are acceptable; use dedicated agent identities and consider channel allowlists or an approval mode before production use. <br>
Risk: Credentials and Nostr private keys are required in service environment files. <br>
Mitigation: Protect env files with strict permissions, use dedicated agent keys, and keep service environments under operator control. <br>
Risk: Message content may be logged locally by services. <br>
Mitigation: Restrict journal access and retention, and remove raw message logging for production deployments. <br>
Risk: The configured OpenClaw endpoint controls the model path for OpenClaw-backed agents. <br>
Mitigation: Keep OPENCLAW_URL and related service configuration under trusted operator control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/darrenjrobinson/skills/buzz-acp) <br>
- [Project homepage](https://github.com/darrenjrobinson/buzz-acp) <br>
- [Buzz project](https://github.com/block/buzz) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Architecture](docs/architecture.md) <br>
- [Troubleshooting](docs/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, Python, TypeScript, systemd, and environment-file examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are deployment and operations guidance for a self-hosted Buzz relay and agent services.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
