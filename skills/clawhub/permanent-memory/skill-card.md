## Description: <br>
Auto Memory stores selected agent decisions, identity, files, and context as permanent memory chains on the Autonomys Network and can recall them from a CID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xautonomys](https://clawhub.ai/user/0xautonomys) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Auto Memory when they want an agent to upload selected files or memory entries to Autonomys Auto Drive, receive CIDs, and later reconstruct a linked memory chain. It is intended for deliberate permanent storage workflows, not for private or sensitive data by default. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded memories and files are permanent and public on decentralized storage. <br>
Mitigation: Review each upload before execution, do not store secrets or sensitive personal, regulated, or proprietary data, and encrypt sensitive content before upload if storage is required. <br>
Risk: The Auto Drive API key is stored in local plaintext configuration files. <br>
Mitigation: Restrict file permissions, avoid sharing local config files, and rotate or revoke the key if the workspace or machine may have been exposed. <br>
Risk: Agents can preserve incorrect or unintended context in a long-lived memory chain. <br>
Mitigation: Save only intentional memory entries, inspect generated JSON where practical, and keep the latest CID under user control. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/0xautonomys/skills/permanent-memory) <br>
- [Auto Drive API Reference](references/automemory-api.md) <br>
- [Autonomys Network Overview](references/autonomys-network.md) <br>
- [Memory Chain Reference](references/memory-chain.md) <br>
- [Auto Drive dashboard and API key management](https://ai3.storage) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns CIDs for uploaded content and can update local memory state plus MEMORY.md when saving chain entries.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
