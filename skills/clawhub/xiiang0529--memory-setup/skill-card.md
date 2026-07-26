## Description: <br>
Enables and configures Moltbot/Clawdbot memory search for persistent context, including memorySearch settings, MEMORY.md, daily logs, and vector search setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure persistent memory search, set up MEMORY.md and daily logs, and troubleshoot memory recall in Moltbot/Clawdbot workspaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory search can index sensitive local files, sessions, or private transcripts. <br>
Mitigation: Review exactly which files and sessions are indexed, exclude secrets and private transcripts, and avoid shared or organizational content unless affected users approve the indexing and retention model. <br>
Risk: Third-party embedding providers may receive sensitive context when memory search uses remote embeddings. <br>
Mitigation: Prefer a local embedding provider for sensitive work and review provider configuration before enabling API-backed embeddings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiiang0529/skills/memory-setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides creation of local memory files, agent instructions, and memorySearch settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
