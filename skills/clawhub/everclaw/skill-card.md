## Description: <br>
Everclaw backs up an agent's memory and identity files to an encrypted remote vault so they can be restored across devices, reinstalls, and workspace resets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tlxue](https://clawhub.ai/user/tlxue) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use Everclaw to sync selected OpenClaw memory, identity, user-profile, and workspace note files to a remote vault and restore missing files at session start. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically provision remote sync and upload local memory and identity files without asking the user first. <br>
Mitigation: Review or modify the flow before first use so it lists the exact files to upload and asks for approval before provisioning or syncing. <br>
Risk: The skill adds HEARTBEAT.md persistence for recurring backup behavior. <br>
Mitigation: Let users opt out of HEARTBEAT.md persistence or remove that task when recurring sync is not desired. <br>
Risk: Synced files may contain sensitive agent memory, identity, profile, or workspace notes. <br>
Mitigation: Install only if the Everclaw cloud endpoint is trusted with those files, and avoid syncing secrets, credentials, AGENTS.md, BOOTSTRAP.md, BOOT.md, or session transcripts. <br>


## Reference(s): <br>
- [Everclaw skill page](https://clawhub.ai/tlxue/skills/everclaw) <br>
- [Everclaw service endpoint](https://everclaw.chong-eae.workers.dev) <br>
- [Everclaw health endpoint](https://everclaw.chong-eae.workers.dev/health) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and HTTP API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses EVERCLAW_API_KEY for authenticated remote vault operations and may create or update local Markdown and JSON configuration files.] <br>

## Skill Version(s): <br>
0.3.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
