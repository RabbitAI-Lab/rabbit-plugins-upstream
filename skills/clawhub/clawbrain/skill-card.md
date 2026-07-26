## Description: <br>
Claw Brain is a personal AI memory system for OpenClaw and ClawDBot that provides memory, personality, bonding, learning, encrypted secrets support, and automatic refresh on service restart. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawcolab](https://clawhub.ai/user/clawcolab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add persistent local memory, user profile context, personality state, and optional encrypted secret storage to OpenClaw or ClawDBot agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed package delegates sensitive setup to the external ClawBrain PyPI package or GitHub source. <br>
Mitigation: Install only after verifying the source version, reviewing the hook code, and confirming the setup behavior in an isolated environment. <br>
Risk: Memories, profiles, and conversation state may persist locally, and only entries marked as secrets are encrypted. <br>
Mitigation: Decide what data the agent may store, restrict access to the database files, and avoid storing sensitive content unless the secret-storage path is appropriate. <br>
Risk: Encryption keys and backups can expose stored secrets if mishandled. <br>
Mitigation: Protect the database, encryption key, and key backups like sensitive credentials, and verify permissions before production use. <br>
Risk: The package documentation no longer matches the packaged artifacts because it refers to a removed skill.json file. <br>
Mitigation: Do not rely on the removed manifest for installation or environment declarations; verify current package metadata and setup steps before use. <br>


## Reference(s): <br>
- [Security documentation](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown instructions with command examples and API usage examples.] <br>
**Output Parameters:** [Agent ID, session and user identifiers, current message, local storage backend, and optional BRAIN_* environment variables.] <br>
**Other Properties Related to Output:** [Can persist local memories and encrypted secrets through the external ClawBrain package; review setup behavior and stored data before deployment.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
