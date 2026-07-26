## Description: <br>
Auto Memory lets an agent upload files, save permanent linked-list memory entries, download CIDs, and recall memory chains from the Autonomys Network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jim-counter](https://clawhub.ai/user/jim-counter) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they intentionally want durable agent memory, file uploads, CID downloads, or recovery of a memory chain from decentralized storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish memory or selected files to public, irreversible storage. <br>
Mitigation: Use it only for data intended for permanent public storage, and verify exactly what will be uploaded before each save or upload. <br>
Risk: Secrets, credentials, private conversation history, personal data, regulated data, or broad workspace snapshots could be exposed if uploaded. <br>
Mitigation: Do not upload sensitive data; narrow inputs to explicit files or memory strings and review content before execution. <br>
Risk: The skill uses persistent local credential handling for AUTO_DRIVE_API_KEY. <br>
Mitigation: Store and rotate the API key according to local credential policy, and avoid sharing workspaces or logs that may expose configuration. <br>


## Reference(s): <br>
- [Auto Memory ClawHub Page](https://clawhub.ai/jim-counter/skills/auto-memory) <br>
- [Auto Drive API Reference](references/automemory-api.md) <br>
- [Autonomys Network Overview](references/autonomys-network.md) <br>
- [Memory Chain & Resurrection Pattern](references/memory-chain.md) <br>
- [Auto Drive Dashboard](https://ai3.storage) <br>
- [Autonomys Auto Drive API Docs](https://mainnet.auto-drive.autonomys.xyz/api/docs) <br>
- [Autonomys Auto Drive SDK Docs](https://develop.autonomys.xyz/sdk/auto-drive/overview_setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, file, outbound HTTPS, and AUTO_DRIVE_API_KEY for uploads, memory saves, and chain recall.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
