## Description: <br>
Auto Memory lets agents upload files and store permanent, CID-addressed memory chains on the Autonomys Network for later recall. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sindrenilsen](https://clawhub.ai/user/sindrenilsen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Auto Memory to persist files, decisions, identity, and agent context as a permanent memory chain. The skill supports later recall by walking the chain from the latest CID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored memories and files are permanent, public, and CID-addressed. <br>
Mitigation: Install only when permanent public storage is intended; do not upload secrets, API keys, private files, personal data, or regulated data unless it has been encrypted and minimized first. <br>
Risk: The Auto Drive API key can be exposed through local environment or OpenClaw configuration files. <br>
Mitigation: Protect local configuration files and rotate the Auto Drive API key if local files may have been exposed. <br>
Risk: Losing the latest memory-chain CID can prevent full recall from local state alone. <br>
Mitigation: Back up the latest CID or anchor it with the companion on-chain registry flow when that recovery posture is required. <br>


## Reference(s): <br>
- [ClawHub Auto Memory Skill Page](https://clawhub.ai/sindrenilsen/skills/auto-memory) <br>
- [Auto Drive API Reference](references/automemory-api.md) <br>
- [Autonomys Network Overview](references/autonomys-network.md) <br>
- [Memory Chain & Resurrection Pattern](references/memory-chain.md) <br>
- [Auto Drive API Docs](https://mainnet.auto-drive.autonomys.xyz/api/docs) <br>
- [Auto Drive SDK Docs](https://develop.autonomys.xyz/sdk/auto-drive/overview_setup) <br>
- [Autonomys Auto SDK](https://github.com/autonomys/auto-sdk) <br>
- [Autonomys Auto Drive](https://github.com/autonomys/auto-drive) <br>
- [Autonomys Agents Framework](https://github.com/autonomys/autonomys-agents) <br>
- [OpenClaw Memory Chain](https://github.com/autojeremy/openclaw-memory-chain) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON command output, CID strings, and downloaded or generated files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local Auto Memory state and update MEMORY.md when present; uploaded content returns CIDs for public, permanent storage.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter and _meta.json list 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
