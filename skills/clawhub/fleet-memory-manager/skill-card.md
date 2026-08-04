## Description: <br>
Set up privacy-first continuity for an OpenClaw agent using private long-term memory, short-lived daily notes, and review-gated consolidation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vswarm-ai](https://clawhub.ai/user/vswarm-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to add explicit-consent, private memory files to an OpenClaw workspace so an agent can preserve durable project context without loading it in shared or untrusted sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory can retain private project or user context beyond the current session. <br>
Mitigation: Enable memory only after explicit consent, define retained categories and retention, and keep daily notes private with a default 30-day review window. <br>
Risk: Private memory could be exposed if loaded in group, shared, public, delegated, or untrusted sessions. <br>
Mitigation: Load MEMORY.md, USER.md, and private daily notes only in approved private direct sessions; use only task-specific context in shared or untrusted sessions. <br>
Risk: Secrets, authentication material, or raw conversation archives could be written into durable memory. <br>
Mitigation: Do not store credentials, tokens, private keys, raw conversations, sensitive personal profiles, or speculative personal traits. <br>
Risk: Setup changes could be applied to the wrong workspace or overwrite existing local content. <br>
Mitigation: Require an absolute private workspace path, review dry-run output first, and create only missing files without overwriting or patching existing files. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/vswarm-ai/skills/fleet-memory-manager) <br>
- [Project homepage](https://github.com/sentien-labs/openclaw-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and generated plain-text memory templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local files only after explicit apply mode; existing files are left unchanged.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
